import os.path

from src.utils import read_file, write_file, append_file, load_config, save_config
from src.llm.LLMFactory import LLMFactory, AbstractLLM


def remove_markdown(text):
    if text.startswith('```python'):
        text = text[len('```python'):]
    elif text.startswith('```'):
        text = text[len('```'):]

    if text.endswith('```'):
        text = text[:-len('```')]
    return text


# def remove_markdown_req(text):
#    if text.startswith('requirements.txt:'):
#        text = text[len('requirements.txt:'):]
#    if text.startswith('\n'):
#        text = text[len('\n'):]
#    if text.startswith('```'):
#        text = text[len('```'):]
#    if text.endswith('```'):
#        text = text[:-len('```')]
#    return text

def init_changelog(changelog_fn: str):
    content = "# Changelog\n\nAll evolution will be documented in this file"
    content += "\n\nThe format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),"
    content += "\n\nand this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).\n"
    write_file(changelog_fn, content)


def run(llm: AbstractLLM, iteration_num: int, temperature: float):
    prompt_start = "Answer only with code, without extra formatting."
    prompt_evolve = "Add a new feature, improve the following Python script for better efficiency and write full resulting code:\n```python\n{script_content}\n```"
    # prompt_requirements = "Now update the requirements.txt file. Current requirements looks like following, and please answer only with the content of requirementx.txt file.\n{requirements}\n"
    prompt_summary = "Now write me a small description of the updates you have made in CHANGELOG format. We are currently at iteration {iteration_num}"

    messages = [{"role": "system", "content": prompt_start}]

    script_content = read_file("app.py")
    prompt = prompt_evolve.format(script_content=script_content)
    messages.append({"role": "user", "content": prompt})
    improved_script = llm.ask(messages, temperature)
    messages.append({"role": "assistant", "content": improved_script})

    improved_script = remove_markdown(improved_script)

    write_file("app.py", improved_script)

    # with open("requirements.txt", "r") as f:
    #    requirements = f.read()

    # prompt = prompt_requirements.format(requirements=requirements)
    # messages.append({"role": "user", "content": prompt})
    # new_requirements = call_llm(messages, 0.5)

    # new_requirements = remove_markdown_req(new_requirements)

    # with open("requirements.txt", "w") as f:
    #    f.write(new_requirements)

    prompt = prompt_summary.format(iteration_num=iteration_num)
    messages.append({"role": "user", "content": prompt})
    updates_summary = llm.ask(messages, 0.5)

    changelog_fn = "CHANGELOG_EVOLUTION.md"
    if not os.path.exists(changelog_fn):
        init_changelog(changelog_fn)
    append_file(changelog_fn, f"\n\n##Evolution {iteration_num}:\n\n" + updates_summary)

    readme_lines = read_file("README.md").split('\n')

    remove_index = None
    for i, line in enumerate(readme_lines):
        if line.startswith("## How it's going (auto updated)"):
            remove_index = i
            break

    if remove_index is not None:
        readme_lines = readme_lines[:remove_index]

    readme_lines.extend([
        f"\n\nSTART:{iteration_num}\n\n",
        updates_summary,
        f"\n\nEND:{iteration_num}",
    ])

    write_file("README.md", "".join(readme_lines))


def main():
    # {"llm": "cohere", "model": "", "temperature": 0.5}
    params_path = "config.json"
    config = load_config(params_path)
    llm = LLMFactory().build_llm(config["llm"])
    if "model" in config and config["model"] != "":
        llm.set_model(config["model"])
    if "iteration" not in config:
        config["iteration"] = 1

    run(llm, config["iteration"], config["temperature"])

    config["iteration"] += 1
    write_file("iteration_num.txt", f"Evolved iteration {config['iteration']}")
    save_config(params_path, config)


if __name__ == "__main__":
    main()

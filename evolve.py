import logging
import os.path

from src.utils import read_file, write_file, append_file, load_config, save_config, copy_files
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


def evolve_once(llm: AbstractLLM, code_path: str, iteration_num: int, temperature: float):
    prompt_start = "Answer only with code, without extra formatting."
    prompt_evolve = "Add a new feature, improve the following Python script for better efficiency"
    prompt_evolve += " and write full resulting code:\n```python\n{script_content}\n```"
    # prompt_requirements = "Now update the requirements.txt file. Current requirements looks like following"
    # prompt_requirements += ", and please answer only with the content of requirementx.txt file.\n{requirements}\n"
    prompt_summary = "Now write me a small description of the updates you have made in CHANGELOG format"
    prompt_summary += " with current iteration"
    prompt_summary += " as evolution number"
    prompt_summary += " and all Added, Removed, Changed and Fixed lists."
    prompt_summary += " We are currently at iteration {iteration_num}."
    prompt_summary += "\nExample of a changelog output for iteration 12:"
    prompt_summary += "\n## Evolution 12\n\n### Added\n\n- new api feature\n- new GET for user name"
    prompt_summary += "\n\n### Changed\n\n- none\n\n### Fixed\n\n- parding function for GET\n\n### Removed\n\n- none"

    messages = [{"role": "system", "content": prompt_start}]

    script_content = read_file(code_path)
    prompt = prompt_evolve.format(script_content=script_content)
    messages.append({"role": "user", "content": prompt})
    improved_script = llm.ask(messages, temperature)
    messages.append({"role": "assistant", "content": improved_script})

    improved_script = remove_markdown(improved_script)

    write_file(code_path, improved_script)

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
    append_file(changelog_fn, f"\n\n" + updates_summary)

    readme_lines = read_file("README.md").split('\n')

    remove_index = None
    for i, line in enumerate(readme_lines):
        if line.startswith("## How it's going (auto updated)"):
            remove_index = i + 1
            break

    if remove_index is not None:
        readme_lines = readme_lines[:remove_index]

    readme_lines.extend([
        f"\n\nIteration {iteration_num}:\n\n",
        updates_summary
    ])

    write_file("README.md", "\n".join(readme_lines))


def main() -> int:
    logging.debug("Starting a step evolution")
    params_path = "config_local.json"

    # Create local evolution
    if not os.path.exists(params_path):
        copy_files("config.json", params_path)

    config = load_config(params_path)

    # Check fields
    required_fields = ["llm", "code_path"]
    for field in required_fields:
        if field not in config:
            raise Exception(f"Field {field} not in config")

    if "iteration" not in config:
        config["iteration"] = 1
    if "max" not in config:
        config["max"] = 5

    if config['max'] == 0:
        print("Ending evolution")
        return 1

    # Init starting script evolution
    if "evolution_path" not in config:
        logging.info("Copying script for evolution...")
        code_path = config["code_path"]

        filename = os.path.basename(code_path)

        _dir = os.path.dirname(code_path)

        _fld = os.path.join(_dir, "evolution_0")
        i = 0
        while os.path.exists(_fld):
            _fld = os.path.join(_dir, f"evolution_{i:2d}")
            i += 1
        os.mkdir(_fld)
        evolution_path = os.path.join(_fld, filename)
        copy_files(code_path, evolution_path)
        copy_files("config.json", os.path.join(_fld, "config.json"))
        config["evolution_path"] = evolution_path

    # Start config
    logging.info(f"Evolution step {config['iteration']}")

    llm = LLMFactory().build_llm(config["llm"])
    if "model" in config and config["model"] != "":
        llm.set_model(config["model"])

    # Evolve
    evolve_once(llm, config["evolution_path"], config["iteration"], config["temperature"])

    config["iteration"] += 1
    config["max"] -= 1
    write_file("iteration_num.txt", f"Evolved iteration {config['iteration']}")
    save_config(params_path, config)
    return 0


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)
    return_code = main()
    exit(return_code)

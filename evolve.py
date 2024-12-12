import os
import cohere


def generate_prompt(script_content):
    # Generate a prompt based on the current script content
    prompt = f"Add a new feature and improve the following Python script for better efficiency:\n```python\n{script_content}\n```"
    return prompt


def call_llm(messages, temperature=0.7):
    co = cohere.ClientV2(os.environ.get("COHERE_API_KEY"))
    response = co.chat(
        model="command-r",
        messages=messages,
        temperature=temperature
    )
    return response.message.content[0].text


def remove_markdown(text):
    if text.startswith('```python'):
        text = text[len('```python'):]
    elif text.startswith('```'):
        text = text[len('```'):]

    if text.endswith('```'):
        text = text[:-len('```')]
    return text

#def remove_markdown_req(text):
#    if text.startswith('requirements.txt:'):
#        text = text[len('requirements.txt:'):]
#    if text.startswith('\n'):
#        text = text[len('\n'):]
#    if text.startswith('```'):
#        text = text[len('```'):]
#    if text.endswith('```'):
#        text = text[:-len('```')]
#    return text

def main():
    messages = [
        {"role": "system", "content": "Answer only with code, without extra formatting."},
    ]

    with open("app.py", "r") as f:
        script_content = f.read()

    prompt = generate_prompt(script_content)
    messages.append({"role": "user", "content": prompt})
    improved_script = call_llm(messages, 0.5)
    messages.append({"role": "assistant", "content": improved_script})

    improved_script = remove_markdown(improved_script)

    with open("app.py", "w") as f:
        f.write(improved_script)

    #with open("requirements.txt", "r") as f:
    #    requirements = f.read()

    #prompt = f"Now update the requirements.txt file. Current requirements looks like following, and please answer only with the content of requirementx.txt file.\n{requirements}\n"
    #messages.append({"role": "user", "content": prompt})
    #new_requirements = call_llm(messages, 0.5)

    #new_requirements = remove_markdown_req(new_requirements)

    #with open("requirements.txt", "w") as f:
    #    f.write(new_requirements)

    prompt = f"Now write me a small description of the updates you have made."
    messages.append({"role": "user", "content": prompt})
    updates_summary = call_llm(messages, 0.5)

    with open("update_result.txt", "w") as f:
        f.write(updates_summary)

    with open("README.md", "r") as f:
       readme = f.readlines()

    last_iteration = int(readme[-1].split(':')[-1])
    iteration = last_iteration + 1

    with open("README.md", "a") as f:
        f.write(f"\n\nSTART:{iteration}\n\n")
        f.write(updates_summary)
        f.write(f"\n\nEND:{iteration}")

    with open("iteration_num.txt", "w") as f:
        f.write(f"Evolved iteration {iteration}")


if __name__ == "__main__":
    main()

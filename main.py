from setup import datasets, prompt, parser, blacklist, quantity, model
from utils import clean, lint, create_dataset_file, write

running_list = []

prompt_and_model = prompt | model

def invoke(prompt):
    output = prompt_and_model.invoke({"query": prompt})
    try:
        parsed_output = parser.parse(output)
    except Exception as e:
        raise e

    cleaned_output = clean(parsed_output.name)

    try:
        lint(cleaned_output, running_list, blacklist)
        running_list.append(cleaned_output)
        return cleaned_output
    except Exception as e:
        raise e 

def generate_item(item):
    outfile = datasets[item]['outfile']
    prompt = datasets[item]['prompt']
    print("==== Generating dataset for:", outfile)

    try:
        with open(f'datasets/{outfile}.txt', 'w') as f:
            pass
    except FileNotFoundError:
        create_dataset_file(outfile)

    for i in range(quantity):
        def generate():
            try:
                print(f"Generating {i+1}/{quantity} for {outfile}")
                output=invoke(prompt)
                print(f"Generated: {output}")
                write(output, outfile)
            except Exception as e:
                print(f"An error occurred: {e}")
                generate()
        generate()

def main():
    for item in datasets:
        print("Starting generation for:", item)
        generate_item(item)

main()
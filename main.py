from dataclasses import dataclass
import openai, sys

running_list = []
blacklist = []
datacounter = int(sys.argv[3])
outfile = sys.argv[1]
prompt = sys.argv[2]

@dataclass
class AIManager:
    ada: str = 'text-ada-001'
    davinci: str = 'text-davinci-001'
    curie: str = 'text-curie-001'

    def make_request(self, prompt) -> str:
        response = openai.Completion.create(
            model=self.davinci,
            prompt=prompt,
            temperature=1,
        )
        return response.choices[0].text

def lint(response:str) -> bool:
        if response == None or '':
            return False
        elif len(response) < 4:
            return False
        elif len(response) > 30:
            return False
        elif "'s" in response:
            return False
        elif response in running_list:
            print('**response duplicated**')    
            return False
        elif response in blacklist:
            print('**blacklisted response**')
            return False
            
        return True

def clean(response: str) -> str:
        characters_to_remove = ['.', ',', '!', '?', ';', ':', '(', ')', '{', '}', '[', ']', '*', "'", '"']
        for char in characters_to_remove:
            response = response.replace(char, '')
        return response

def write(item: str):
    with open(f'datasets/{outfile}.txt', 'a') as fp:
        item = item.strip() # assign the stripped value back to the variable
        fp.write(item + "\n")

def create_dataset_file(outfile:str):
    with open(f'datasets/{outfile}.txt', 'w') as f:
        pass 

def main(outfile:str, prompt:str, datacounter:int):

    try:
        with open(f'datasets/{outfile}.txt', 'w') as f:
            pass
    except FileNotFoundError:
        create_dataset_file(outfile)

    while datacounter > 0:
        print(datacounter)
        # prompt = '''Return a name for a jewelcrafting shop in a medieval fantasy setting'''
        prompt = prompt
        ai_manager = AIManager()
        response = ai_manager.make_request(prompt)
        cleaned_response = clean(response)
        linted = lint(cleaned_response)
        if linted:
            running_list.append(cleaned_response)
            datacounter -= 1
            write(cleaned_response)



main(outfile, prompt, datacounter)
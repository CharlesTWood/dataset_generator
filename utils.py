def lint(response:str, running_list:list, blacklist:list) -> bool:
    if response == None or '':
        raise Exception("Invalid response")
    elif len(response) < 4:
        raise Exception("Invalid response")
    elif len(response) > 40:
        raise Exception("Invalid response")
    elif response in running_list:
        print('**response duplicated**')
        raise Exception("Invalid response")
    elif response in blacklist:
        print('**blacklisted response**')
        raise Exception("Invalid response")
    return True

def clean(response: str) -> str:
    characters_to_remove = ['.', ',', '!', '?', ';', ':', '(', ')', '{', '}', '[', ']', '*', '"']
    for char in characters_to_remove:
        response = response.replace(char, '')
    return response

def create_dataset_file(outfile:str):
    with open(f'datasets/{outfile}.txt', 'w') as f:
        pass 

def write(item: str, outfile: str):
    with open(f'datasets/{outfile}.txt', 'a') as fp:
        item = item.strip() # assign the stripped value back to the variable
        fp.write(item + "\n")

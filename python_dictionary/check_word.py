import json

data=json.load(open('dictionary.json'))

def retrieve_definition(word):
    
    # Convert all letters into lowercase
    word=word.lower()

    # check for non-existent words
    if word in data:
        return data[word]
    
    # Ensure dict return words with the first letter capital
    elif word.title() in data:
        return data[word.title()]
    
    # Ensure dict returns meanings of acronyms
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return('That word does not exist in the dictionary. Please double check it.')

word=input('Enter a word: ')

print(retrieve_definition(word))

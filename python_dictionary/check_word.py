import difflib

import json

from difflib import get_close_matches

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
    
    elif len(get_close_matches(word, data.keys())) > 0:
        return ('Did you mean %s?' % get_close_matches(word, data.keys())[0])
    
    else:
        return('That word does not exist in the dictionary. Please double check it.')

word=input('Enter a word: ')

print(retrieve_definition(word))

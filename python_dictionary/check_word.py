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
    
    # Find closest word to what is input
    elif len(get_close_matches(word, data.keys())) > 0:
        action=input('Did you mean %s, y/ n? ' % get_close_matches(word, data.keys())[0])
        
        if (action=='y' or 'Y'):
            return data[get_close_matches(word, data.keys())[0]]
        
        elif (action=='n' or 'N'):
            return ('That word does not exist in the dictionary. Please double check it.')
    
    else:
        return('Entry not understood... Exiting.')

word=input('Enter a word: ')

output=retrieve_definition(word)

# remove square braces from the outputted definition

# multiple definitions
if type(output)==list:
    for item in output:
        print('-', item)
# single definition
else:
    print('-', output)


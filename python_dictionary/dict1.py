import json

data=json.load(open('dictionary.json'))

def retrieve_definition(word):

    # check for non-existent words
    if word in data:
        return data[word]
    else:
        return('That word does not exist in the dictionary.')

word=input('Enter a word: ')

print(retrieve_definition(word))

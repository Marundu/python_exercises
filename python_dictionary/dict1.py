import json

data=json.load(open('dictionary.json'))

def retrieve_definition(word):
    return data[word]

word=input('Enter a word: ')

print(retrieve_definition(word))

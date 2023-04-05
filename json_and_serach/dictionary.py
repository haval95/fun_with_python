import json

data = json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    else:
        return "The Word doesn't exist, please double check it."


word = input("Enter a Word: ")
print((translate(word)))
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif get_similar_matches(word):
        similar_word = get_similar_matches(word)[0]
        while True:
            is_it_the_similar = input(f"did you mean ( {similar_word} ) Yes / No? ") 
            if "y" in is_it_the_similar:
                return data[similar_word]
            elif "n" in is_it_the_similar:
                return ["Please double check your spelling."]
            print("we didn't understand your query! ")
    else:
        return ["The Word doesn't exist, please double check it."]

def get_similar_matches(word):
    close_matches = get_close_matches(word,data.keys(),1,0.8)
    return close_matches
    

user_word = input("Enter a Word: ")
for definition in translate(user_word):
    print("- " + definition)


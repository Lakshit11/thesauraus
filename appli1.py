import json
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s? Press Y for yes or N for no:"%get_close_matches(word,data.keys())[0])
        if yn in ("Y","y"):
            return data[get_close_matches(word,data.keys())[0]]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            yn=input("Did you mean %s? Press Y for yes or N for no:"%get_close_matches(word,data.keys())[0])
            return data[word.upper()]
        elif yn in ("N","n"):
            yn=input("Did you mean %s? Press Y for yes or N for no:"%get_close_matches(word,data.keys())[1])
            if yn in ("Y","y"):
                return data[get_close_matches(word,data.keys())[1]]
            elif yn in ("N","n"):
                yn=input("Did you mean %s? Press Y for yes or N for no:"%get_close_matches(word,data.keys())[2])
                if yn in ("Y","y"):
                    return data[get_close_matches(word,data.keys())[2]]
                # elif yn in ("N","n"):
                #     yn=input("Did you mean %s? Press Y for yes or N for no:"%get_close_matches(word,data.keys())[3])
                #     if yn in ("Y","y"):
                #         return data[get_close_matches(word,data.keys())[3]]
                #     else:
                #         return "Sorry Match Not Found!"
                else:
                    return "Match Not Found!Please Try Again"
            else:
                return "Match Not Found!Please Try Again"
        else:
            return "Please Select Appropriate Option."
    else:
        return "Word does not exist.Please Recheck It!!"
word=input("Enter Word:")
result=translate(word)
if type(result)==list:
    for val in result:
        print(val)
else:
    print(result)    
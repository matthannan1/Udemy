import json
from difflib import get_close_matches

dictionary = json.load(open("dict.json"))


def define_word(term):
    if term in dictionary:
        return dictionary[term]
    elif len(get_close_matches(term, dictionary.keys())) > 0:
        yn = input("Did you mean %s instead? Y/N "
                   % get_close_matches(term, dictionary.keys())[0])
        if yn == 'Y' or yn == 'y':
            return dictionary[get_close_matches(term, dictionary.keys())[0]]
        else:
            return "Word not found."
    else:
        return "Word not found."


print()
term = input("What word would you like to look up? ")
output = define_word(term)
if type(output) is list:
    for definition in output:
        print(definition)
else:
    print(output)
print()

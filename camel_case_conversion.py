import re
from re import sub


def to_camel_case(text):
    if not text:
        return text
    words = sub(r"(_|-)+", " ", text).split()  #searches for any "-" or "_" and removes then and splits up the string
    first_word = words[0]  #seperates the first word of the string
    camel_cased = first_word + ''.join(word.capitalize() for word in words[1:]) #add the untouched firstt word back to the capitalised string
    return camel_cased  #return the result

value = input("Please enter a string to convert to camel case: ")

result = to_camel_case(value)

print(result)
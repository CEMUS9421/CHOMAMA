from typing import Type


print("Welcome to the Morse-Code tranlator")
print("Write your sentence: ")
user_input = input("")
dictionary = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "ä": ".-.-",
    "ö": "---.",
    "ü": "..--",
    " ": " ",
}
for index in user_input.lower():
    if index in dictionary:
        print(dictionary[index], end="")
    else:
        print("Character not found in dictionary")

print("\n")
print("Type (exit) to exit the program or Type (more) to continue translating")
while True:
    user_input = input("")
    if user_input == "exit":
        break
    elif user_input == "more":
        exec(open(__file__).read())
    else:
        print("Invalid input, please try again")
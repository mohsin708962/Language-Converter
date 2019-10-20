import os
import languages
from googletrans import Translator

translator = Translator()

'''
    for covertion printiong use .text and for real text use .origin
'''


def insert_text():
    text_to_convert = input("Enter Your Text to convert in any language: ")
    with open("convert_me.txt", "w") as f:
        text = f.write(text_to_convert)

def translate_text():
    if os.path.exists("convert_me.txt"):
        with open("convert_me.txt", "r") as file:
            f = file.read()
            file.close()
    else:
        exit()
    for key, value in languages.LANGUAGES.items():
        print(key + " - " + value)

    language = input("choose language: ")
    try:
        translations = translator.translate(f, dest=language)
        print(translations.origin + " = " + translations.text)
    except:
        print("Invalide Input")
       
insert_text()
translate_text()
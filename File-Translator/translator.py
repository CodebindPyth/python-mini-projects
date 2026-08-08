from auto_translate import AutoTranslate


selection = input('Enter the language you want to translate to (e.g., "el", "en", "de"): ')
translate = AutoTranslate(str(selection))
try:

    with open('text.txt', mode='r') as file:

        text = file.read()
        pap = translate.translate(text)
        with open(f'translate.{selection}.txt', 'w') as file2:
            file2.write(pap)
except FileNotFoundError:
    print("The file could not be found.")    

print(pap)


    

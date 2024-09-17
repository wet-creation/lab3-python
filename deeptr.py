from lab3 import deep_trans as dt


text = input("Input text: ")

result = dt.LangDetect(text)
print(result)

target_lang = input("Input the language you want to translate: ")

translation = dt.TransLate(text, target_lang)
print(f"Translated text: {translation}")
print("Proceed language list")
print(dt.LanguageList(text = text))

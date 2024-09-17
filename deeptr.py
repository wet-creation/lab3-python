from lab3 import deep_trans as dt


text = input("Input text: ")

result = dt.LangDetect(text)
print(result)
lang = "ukrainian"
code_lang = dt.CodeLang(lang)
print(f"code = {code_lang} lang = {lang}")

translation = dt.TransLate(text, code_lang)
print(f"Translated text: {translation}")
print("Proceed language list")
print(dt.LanguageList(text = text))

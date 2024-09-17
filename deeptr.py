from lab3 import deep_trans as dt


text = input("Input text: ")

result = str(dt.LangDetect(text)).split(":")
print(f"code = {result[0]} confidence = {round(float(result[1]),2)*100}%")
lang = "ukrainian"
code_lang = dt.CodeLang(lang)
print(f"code = {code_lang} lang = {lang}")

translation = dt.TransLate(text, code_lang)
print(f"Translated text: {translation}")
print("Proceed language list")
print(dt.LanguageList(text = text))

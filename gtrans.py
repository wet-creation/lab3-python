from lab3 import google_trans as gt

text = input("Input text: ")

result = gt.LangDetect(text)
if isinstance(result, tuple) and len(result) == 2:
    detected_lang, confidence = result
    if confidence is not None:
        print(f"Language: {gt.CodeLang(detected_lang)} (confidence: {confidence * 100:.2f}%)")
    else:
        print(f"Language: {gt.CodeLang(detected_lang)} (confidence not determined)")
else:
    print(result)
lang = "ukrainian"
code_lang = gt.CodeLang(lang)
print(f"code = {code_lang} lang = {lang}")

translation = gt.TransLate(text, lang)
print(f"Translated text: {translation}")
print("Proceed language list")
print(gt.LanguageList(text = text))
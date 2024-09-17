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

target_lang = input("Input the language you want to translate: ")

translation = gt.TransLate(text, target_lang)
print(f"Translated text: {translation}")
print("Proceed language list")
print(gt.LanguageList(text = text))
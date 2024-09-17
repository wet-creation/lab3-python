from deep_translator import GoogleTranslator
from langdetect import detect_langs, DetectorFactory

LANGUAGES = GoogleTranslator().get_supported_languages(as_dict = True)
LANGUAGES = dict((v,k) for k,v in LANGUAGES.items())
DetectorFactory.seed = 8734763

def TransLate(text, lang):
    try:
        lang_code = CodeLang(lang.lower())
        translated = GoogleTranslator(source='auto', target=lang_code).translate(text)
        return translated
    except Exception as e:
        return f"Translation error: {str(e)}"

def LangDetect(txt):
    try:
        res = (detect_langs(txt))[0]
        if res:
            return res
        else:
            return "Couldn\'t determine language"
    except Exception as e:
        return f"Translation error: {str(e)}"

def CodeLang(lang):
    if lang.lower() in LANGUAGES.values():
        for code, name in LANGUAGES.items():
            if name.lower() == lang.lower():
                return code.lower()
    elif lang.lower() in LANGUAGES.keys():
        return LANGUAGES[lang.lower()].lower()
    else:
        raise ValueError("Not existing language or code")


def LanguageList(out="screen", text=""):
    headers = ['N', 'Language', 'ISO-639 code']
    table = []
    col_widths = [5, 30, 15]
    if text:
        headers.append('Text')
        col_widths.append(50)

    header_row = [header.ljust(width) for header, width in zip(headers, col_widths)]
    table.append(header_row)
    separator = ('-' * width for width in col_widths)
    table.append(separator)

    for i, (lang_code, name) in enumerate(LANGUAGES.items(), 1):
        row = [str(i).ljust(col_widths[0]),
               name.ljust(col_widths[1]),
               lang_code.ljust(col_widths[2])]

        if text:
            try:
                translated_text = TransLate(text, lang_code)
            except Exception as e:
                return f"Translation error {name}: {e}"

            row.append(translated_text.ljust(col_widths[3]))
        table.append(row)


    output_str = '\n'.join(''.join(row) for row in table)

    if out == 'file':
        try:
            with open('language_list_dt.txt', 'w', encoding='utf-8') as f:
                f.write(output_str + "\n")
        except Exception as e:
            return f"File writing error: {e}"

    else:
        print(output_str)
        print("…" * 50)

    return 'Ok'




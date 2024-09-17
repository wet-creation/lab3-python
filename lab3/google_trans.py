from googletrans import Translator, LANGUAGES

translator = Translator()

def TransLate(text, lang):
    try:
        lang_code = CodeLang(lang)
        translated = translator.translate(text, dest=lang_code)
        return translated.text
    except Exception as e:
        return f"Translation error: {str(e)}"


def LangDetect(txt):
    try:
        detections = translator.detect(txt)
        if detections:
            detection = detections
            return detection.lang, detection.confidence
        else:
            return "Couldn\'t determine language", None
    except Exception as e:
        return f"Translation error: {str(e)}", None


def CodeLang(lang):
    if lang.lower() in LANGUAGES.values():
        for code, name in LANGUAGES.items():
            if name == lang.lower():
                return code
    elif lang.lower() in LANGUAGES.keys():
        return LANGUAGES[lang.lower()]
    else:
        raise ValueError("Not existing language or code")

def LanguageList(out = "screen", text = ""):
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

    for i, (code, language) in enumerate(LANGUAGES.items(), 1):
        row = [str(i).ljust(col_widths[0]),
               language.ljust(col_widths[1]),
               code.ljust(col_widths[2])]
        if text:
            try:
                translated_text = TransLate(text, code)
            except Exception as e:
                return f"Translation error {language}: {e}"
            row.append(translated_text.ljust(col_widths[3]))
        table.append(row)

    output_str = '\n'.join(''.join(row) for row in table)
    if out == 'file':
        try:
            with open('language_list_gt.txt', 'w', encoding='utf-8') as f:
                f.write(output_str + "\n")
        except Exception as e:
            return f"File writing error: {e}"
    else:
        print(output_str)
        print("…" * 50)

    return 'Ok'
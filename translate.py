#!/home/patrickpragman/PycharmProjects/models/translate/venv/bin/python
import argparse
from argostranslate import translate
from langdetect import detect, detect_langs
import pyttsx3


def change_voice(engine, language, gender='male'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))


def main(args):
    if not args.from_lang:
        detected = detect(args.input_string)
        args.from_lang = detected
        probs = detect_langs(args.input_string)
        probs = {l.lang: l.prob for l in probs}

        if args.verbose:
            print('language flag not used, attempting to detect language, internet required...')
            print(f'detected: {detected}')
            print('Probabilities:')
            print(probs)
    else:
        probs = {args.from_lang: 1.0}

    installed_languages = {
        lang.code: lang for lang in translate.load_installed_languages()
    }
    for from_lang in probs:
        if from_lang not in installed_languages:
            print(f'unable to translate from {from_lang}, not installed')
            break
        if args.to_lang not in installed_languages:
            print(f'unable to translate to {args.to_lang}, not installed')
            break
        else:
            from_language = installed_languages[from_lang]
            to_language = installed_languages[args.to_lang]
            translation = from_language.get_translation(to_language)
            if translation is None:
                print(f"No translation installed from {from_language} to {to_language}")

            translation_output = translation.translate(args.input_string)
            out = f"""Input Text:
{args.input_string} 

({from_language}) -> ({to_language})

Translation:
{translation_output}
"""
            print(out)

        if args.speak:
            try:
                engine = pyttsx3.init()
                if args.to_lang == "en":
                    args.to_lang = "en-us"
                    speaking_lang = f"\x02{args.to_lang}".encode()
                else:
                    speaking_lang = f"\x05{args.to_lang}".encode()
                change_voice(engine, speaking_lang, )
                engine.setProperty('rate', 110)
                engine.say(translation_output, )
                engine.runAndWait()
            except RuntimeError as runtime_error:
                print('Runtime error:')
                print(runtime_error)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Command Line Tool')
    parser.add_argument('--from_lang', "-f", type=str, required=False, help='Source Language')
    parser.add_argument('--to_lang', "-t", type=str, required=False, default="en", help='Target Language')
    parser.add_argument("--verbose", '-v', required=False, default=False, action='store_true', help="Verbose mode.")
    parser.add_argument('input_string', type=str, help='Input string')
    parser.add_argument('--speak', '-s', required=False, default=False, action='store_true', help='Speak aloud')

    args = parser.parse_args()
    main(args)

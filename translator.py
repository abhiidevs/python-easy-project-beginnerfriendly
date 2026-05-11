from deep_translator import GoogleTranslator
import pyttsx3

language = {
    "bn": "Bengali",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    "ml": "Malayalam",
    "mr": "Marathi",
    "pa": "Punjabi",
    "ru": "Russian",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

engine = pyttsx3.init()

def display_languages():
    print("\nAvailable Languages:")
    
    for code, lang in language.items():
        print(f"{code} : {lang}")

while True:

    display_languages()

    to_lang = input("\nEnter target language code: ").strip().lower()

    if to_lang not in language:
        print("Invalid language code.")
        continue

    text = input("Enter text to translate: ").strip()

    if not text:
        print("Text cannot be empty.")
        continue

    try:
        translator = GoogleTranslator(source='auto', target=to_lang)
        translated_text = translator.translate(text)

        print("\nTranslated Text:", translated_text)

        speak = input("Do you want pronunciation? (yes/no): ").strip().lower()

        if speak in ["yes", "y"]:
            engine.say(translated_text)
            engine.runAndWait()

    except Exception as e:
        print("Error:", e)

    again = input("\nTranslate another text? (yes/no): ").strip().lower()

    if again not in ["yes", "y"]:
        print("Goodbye!")
        break
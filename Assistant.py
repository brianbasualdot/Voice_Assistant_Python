import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id) # el valor 0 y 1 es para establecer el tono de voz
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak ("Buen Día!")
    elif hour >= 12 and hour < 18:
        speak("Buenas tardes!")
    else:
        speak("Buenas noches!")

    speak("Soy su asisténte virtual, En que lo puedo ayudar?")

def takeCommand():  
    # Toma el sonido del microfono del usuario y retorna en audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recording...")
        query = r.recognize_google(audio, language='es-es')
        print(f"Digame Usted: {query}\n")

    except Exception as e:
        print(e)
        print("Disculpe, No le oigo, Repita por favor...")
        speak("Disculpe, No le oigo, Repita por favor")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Buscando en Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("De acuerdo con Wikipedia ")
            print(results)
            speak(results)

        elif 'Abrir Youtube' in query:
            webbrowser.open("youtube.com")

        elif 'Abrir Google' in query:
            webbrowser.open("google.com")

        elif 'Abrir Twitter' in query:
            webbrowser.open("twitter.com")

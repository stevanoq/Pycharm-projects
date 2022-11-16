import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Hello i am justin your personal virtual assistant')
talk('what can i do for you ?')

def take_command():

    try:
        command = ''
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

        if 'justin' in command:
            command = command.replace('justin', '')
            print(command)

    except:
        talk('i am not hear you')
    return command

def run_va():

    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('let me play' + song + 'for you stevano')
        print('let me play' + song + 'evan')
        print('playing')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        talk('searching for' + person)
        print(person)
        result = wikipedia.summary(person, 5)
        talk(result)

    elif 'how are you' in command:
        talk('i am good')
        talk('how are you ?')

    elif 'love' in command:
        talk('i love you too')

    elif 'turn on' in command:
        talk('okay boss')
        talk('turnning on')

    elif 'what is' in command:
        something = command.replace('what is', '')
        talk('searching for' + something)
        print(something)
        result = wikipedia.summary(something, 5)

        talk(result)

    elif 'joke' in command:
        jokes = pyjokes.get_joke('en', 'all')
        talk(jokes)
        print(jokes)


    else:
        talk('i am dont understand you')


while True:
    run_va()
    talk('any think else sir ?')
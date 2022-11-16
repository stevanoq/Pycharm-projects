import speech

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listenign')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    pass
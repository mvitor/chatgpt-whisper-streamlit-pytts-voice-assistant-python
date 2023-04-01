import speech_recognition as sr

# create a recognizer instance
r = sr.Recognizer()

# define the callback function
def callback(recognizer, audio):
    try:
        # recognize speech using Google Speech Recognition
        recognized_speech = recognizer.recognize_google(audio)
        print(f"Recognized Speech: {recognized_speech}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# create a microphone instance
mic = sr.Microphone()

# start listening in the background
stop_listening = r.listen_in_background(mic, callback)

# keep the program running
while True:
    pass

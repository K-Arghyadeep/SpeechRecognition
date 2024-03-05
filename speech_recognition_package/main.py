# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

try:
    print("inside try block")
    # use the microphone as source for input.
    with sr.Microphone() as source2:

        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.adjust_for_ambient_noise(source2, duration=5)

        # listens for the user's input
        print("listening")
        audio2 = r.record(source2, offset=0.4)
        print("listening complete")

        # Using google to recognize audio
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()

        print_messsage = "Did you say " + MyText
        print(print_messsage)
        SpeakText(print_messsage)

except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

except sr.UnknownValueError:
    print("unknown error occurred")

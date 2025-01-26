import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

def greeting():
    engine.say("Good morning Mohammed.\nWelcome to your virtual application. My name is Barbara and I will be your Virtual Assistance")
    engine.runAndWait()

def tranform_audio_into_text():
        # Store recognizer in variable
    r = sr.Recognizer()
    
    # Set microphone
    with sr.Microphone() as source:  # Fix: Instantiate sr.Microphone
        # Waiting time
        r.pause_threshold = 0.8
        
        # Report that recording is in progress
        print('You can now speak...')
        
        # Save speech in audio variable
        audio = r.listen(source)
        
        try:
            # Recognize audio (replace Azure with Google for default recognizer)
            request = r.recognize_google(audio, language="en-US").lower()
            
            # Print the recognized text
            print("You said: " + request)
            
            # Return the recognized text
            return request
        except sr.UnknownValueError:
            # When the speech was not recognized
            print("No Service found")
            return 'I am still waiting'
        except sr.RequestError:
            # When the speech service is unreachable
            print("Unable to understand Audio")
            return 'I am still waiting'
        except Exception as e:
            # Catch any other errors
            print(f"Service Error: {e}")
            return 'I am still waiting'

def speak(message):
    engine.say(message)
    engine.runAndWait()
    engine.stop()

def my_assistant():
    greeting()
    
    # pointer 
    end_ai = True
    
    while end_ai:
        # activate Microphone and save request
        my_request = tranform_audio_into_text()
        
        if 'open youtube' in my_request:
            speak('Sure, let me open up Youtube on your Chrome.')
            webbrowser.open('https://www.youtube.com')
        elif 'open browser':
            speak('Of course, I am on it.')
            webbrowser.open('https://www.google.com')
        else:
            speak("No request were made")


my_assistant()
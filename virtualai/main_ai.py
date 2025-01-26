import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Hear the microphone and return the audio as text
def convert_audio_into_text():
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
            request = r.recognize_google(audio, language="en-US")
            
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

if __name__ == '__main__':
    convert_audio_into_text()

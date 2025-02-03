#this is voice activated calculateor, for voice activated calculations :) 

import speech_recognition as sr
recognizer = sr.Recognizer()

def calculate(sentence):
    t = sentence.replace(",", "").split(" ")
    if "by" in t:
        t.remove("by")           
    if t[1] == "+":
        return float(t[0]) + float(t[2])
    elif t[1] == "-":
        return float(t[0]) - float(t[2])
    elif t[1] =="x":
        return float(t[0]) * float(t[2])
    else:
        return float(t[0]) / float(t[2])
    
voice_in = ""
with sr.Microphone() as source: #starts picing up audio from the microphone
    while voice_in != "done":
        recognizer.adjust_for_ambient_noise(source) #proceses it and strips unwanted sounds
        try: # in case any errors (like no internet) code will not fail
            print("say something .. ")
            audio = recognizer.listen(source)
            voice_in = recognizer.recognize_google(audio)
            print(voice_in)
            print(calculate(voice_in))
            
        except IndexError:    #this line and 5 below handle errors :)
            print("index error")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")     
import pyttsx3





# start engine of pyttsx3
engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
 print(voice)
        

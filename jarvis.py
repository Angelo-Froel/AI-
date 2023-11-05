import wolframalpha
import wikipedia
import pyttsx3
client = wolframalpha.Client("ALGWYH-5Y8U4A5263")
engine = pyttsx3.init()


# hello_psg.py

import PySimpleGUI as sg

sg.theme('DarkBlue')
layout = [  
            [sg.Text('HELLO!, What would you like to know?'), sg.InputText()],
            [sg.Button('Ok'),sg.Button('Speak'),sg.Button('Cancel')] ]
window = sg.Window('Jarvis', layout)

while True:
    event, values = window.read()
    if event in (None,'Cancel'): 
        break
    
    if event in ('Speak'):
        try:
             res = client.query(values[0])
             wolfram_res=next(res.results).text
             result=wikipedia.summary(values[0],sentences=2)
             engine.say(wolfram_res)
             engine.say(result)
             engine.runAndWait()
             exit
        except:
             engine.say("Please Input a Valid Text")
             engine.runAndWait()   
             sg.popup("I'm Sorry,I Can't Understand That")
             exit
       

    try:
        res = client.query(values[0])
        wolfram_res=next(res.results).text
        result=wikipedia.summary(values[0],sentences=2)
        engine.say("This is What I Found")
        engine.runAndWait()
        sg.Popup("Wolframaplha result: "+wolfram_res,"Wikipedia result: "+result)
        
       
    except:
        engine.say("Please Input a Valid Text")
        engine.runAndWait()   
        sg.popup("I'm Sorry,I Can't Understand That") 
        

window.close()




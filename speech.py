import speech_recognition as SR
import random
mic= SR.Microphone()


recog= SR.Recognizer()

def oyente ():
    with mic as source: 
        recog.adjust_for_ambient_noise(source, duration=1)
        print("please say something in french")
        audio = recog.listen(source)

        texto=  recog.recognize_google(audio,language="fr-FR")

        return texto 
    
def oyente2 ():
    with mic as source: 
        recog.adjust_for_ambient_noise(source, duration=1)
        print("please say something in spanish")
        audio = recog.listen(source)

        texto=  recog.recognize_google(audio,language="es-ES")

        return texto 
    
    

def duo_pirata():

    palabras  = {

    "facil": ["agenda", "ami", "souris"],
    "intermedio": ["ordinateur", "algorithme", "développeur"],
    "dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
    }

    nivel= input ("escoge nivel: facil, intermedio o dificil").lower

    if nivel== "facil": 
        palabra= random.choice(nivel[palabras])
        print ("debes pronunciar:", palabra)
        respuesta= audio()
        if respuesta== audio(): 
            print("buena pronunciacion!")
        else: 
            print("pronunciaste mal")

    if nivel== "intermedio": 
        palabra= random.choice(nivel[palabras])
        print ("debes pronunciar:", palabra)
        respuesta= audio()
        if respuesta== audio(): 
            print("buena pronunciacion!")
        else: 
            print("pronunciaste mal")

    if nivel== "dificil": 
        palabra= random.choice(nivel[palabras])
        print ("debes pronunciar:", palabra)
        if respuesta== audio(): 
            print("buena pronunciacion!")
        else: 
            print("pronunciaste mal")

    else:
        print ("este nivel no existe")


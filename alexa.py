import speech_recognition as sr
import pyttsx3

def reconhecer_fala():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Deseja continuar? ")
        audio = microfone.listen(source)
        frase = microfone.recognize_google(audio, language='pt-BR')

        while frase == "sim":
            try:
                print("Diga o que você quer?")
                audio = microfone.listen(source)
                frase = microfone.recognize_google(audio, language='pt-BR')
                print("Você disse: " + frase)
                    
            except:
                print("Não entendi!!")
            return frase        

reconhecer_fala()


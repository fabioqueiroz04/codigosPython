import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyttsx3
import time

def reconhecer_fala():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("Ouvindo: ")
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            print(frase)
        except:
            print("Não entendi!!")
        return str(frase)        



voz = reconhecer_fala()

pyautogui.PAUSE = 1.5


pyautogui.press('winleft')#Aperta a tecla windows
pyautogui.write(voz)#Escreve no menu do windows a palavra chrome
pyautogui.press('enter')#Pressiona enter
time.sleep(5)
pyautogui.press('enter')#Pressiona enter
time.sleep(5)
pyautogui.press('enter')#Pressiona enter
time.sleep(5)
pyautogui.alert("Fale que eu digito!")
time.sleep(5)
pyautogui.press('enter')#Pressiona enter
voz = reconhecer_fala()
pyautogui.write(voz)#Escreve no menu do windows a palavra chrome
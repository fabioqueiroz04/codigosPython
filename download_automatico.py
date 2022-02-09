import pyautogui
import time

pyautogui.alert("O código vai começar!! Não mexa no seu computador!!")
pyautogui.PAUSE = 1.5
pyautogui.press('winleft')#Aperta a tecla windows
pyautogui.write('chrome')#Escreve no menu do windows a palavra chrome
pyautogui.press('enter')#Pressiona enter
time.sleep(5)
pyautogui.write('https://www.yumpu.com/pt/document/read/62792429/machine-learning-introducao-a-classificacao')
pyautogui.press('enter')#Pressiona enter
time.sleep(5)
#Clica na tela com o botão direito do mouse
for i in range(211):
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('right')

pyautogui.alert("O computador está livre, pode utilizar!!")    
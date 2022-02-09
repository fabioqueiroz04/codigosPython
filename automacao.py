import pyautogui
import time

pyautogui.alert("O código vai começar!! Não mexa no seu computador!!")
pyautogui.PAUSE = 1.5
#Abrir o google drive no computador
pyautogui.press('winleft')#Aperta a tecla windows
pyautogui.write('chrome')#Escreve no menu do windows a palavra chrome
pyautogui.press('enter')#Pressiona enter
time.sleep(3)
pyautogui.write('docs.google.com')

#pyautogui.moveTo(611, 398)

#pyautogui.write('http://alfabetizarpiaui.seduc.pi.gov.br/auth.php')
pyautogui.press('enter')
time.sleep(6)
#pyautogui.hotkey('alt', 'f4')
#entrar na minha área de trabalho
#pyautogui.hotkey('winleft','d')#Mantem as teclas pressionadas
#Clica no arquivo que quero copiar
#pyautogui.press('winleft')
#3pyautogui.write('word')
#pyautogui.press('enter')
#time.sleep(2)
#pyautogui.press('enter')
#pyautogui.hotkey('ctrl', 'shift', 'p')
#time.sleep(1)
#pyautogui.write('25')
#pyautogui.press('enter')
#pyautogui.hotkey('ctrl', 'n')
#time.sleep(1)
#pyautogui.write('Ola')
#pyautogui.press('enter')
#pyautogui.write('p')
#pyautogui.press('enter')
#time.sleep(1)
#pyautogui.press('enter')
#pyautogui.write('Sou uma automacao escrita em python!!')
#Abrir o google drive no computador
#pyautogui.press('winleft')#Aperta a tecla windows
#pyautogui.write('chrome')#Escreve no menu do windows a palavra chrome
#pyautogui.press('enter')#Pressiona enter
#time.sleep(1)
#pyautogui.write('o que e python')
#pyautogui.press('enter')
#time.sleep(2)
pyautogui.moveTo(850, 401)
pyautogui.click()
#time.sleep(4)
#pyautogui.hotkey('alt', 'f4')
#pyautogui.press('enter')
#pyautogui.write('Ate logo!!')
#pyautogui.press('enter')
#pyautogui.write('#forabolsonaro')
#time.sleep(0.5)
#pyautogui.hotkey('alt','f4')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')

pyautogui.press('enter')

pyautogui.alert("O computador está livre, pode utilizar!!")

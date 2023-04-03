import pyautogui
import time
#aq tu vai preencher os dados essenciais

destino = "teste@gmail.com "
assunto = "teste123"
msg = "teste321"


#deixa o email aberto ja, tu tem 5 segundos pra mudar do editor de code pra o navegador na parte do email

time.sleep(5)

#n mexa no contador
pyautogui.click(x=90, y=150)
time.sleep(7)
pyautogui.write(destino)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(assunto)
pyautogui.press('tab')
pyautogui.write(msg)
time.sleep(2)
pyautogui.hotkey('ctrl', 'enter')
import pyautogui
from time import sleep


with open('cadastro.txt','r') as cadastro:
    for line in cadastro:
        product = line.split(',')[0]
        price = line.split(',')[1]
        description = line.split(',')[2]
        
        pyautogui.click(716, 280, duration=2)  #cadastrar produto
        
        pyautogui.click(160, 340, duration=1)
        pyautogui.write(product)
        
        pyautogui.click(500, 350, duration=1)
        pyautogui.write(price)
        
        pyautogui.click(337, 264, duration=1)
        pyautogui.click(1580, 445, duration=1)
        pyautogui.write(description)
        
        pyautogui.click(1865, 995, duration=1)



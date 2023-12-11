import csv
import pyperclip
import pyautogui
import time

def cadastrar_produto(nome_produto, valor, descricao):
    pyautogui.click(718,277, duration= 1)
    pyautogui.click(144,347, duration= 1)
    
    # Etapa 1: Nome do Produto
    pyperclip.copy(nome_produto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')

    # Etapa 2: Valor
    pyperclip.copy(valor)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.click(357,262, duration=1)
    pyautogui.click(1573,453, duration=1)

    # Etapa 3: Descrição
    pyperclip.copy(descricao)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

def cadastrar_produtos_arquivo(arquivo):
    with open(arquivo, newline='') as csvfile:
        leitor_csv = csv.DictReader(csvfile)
        for linha in leitor_csv:
            nome = linha['nome'].encode('latin-1').decode('utf-8')

            valor = linha['preco'].encode('latin-1').decode('utf-8')

            descricao = linha['descricao'].encode('latin-1').decode('utf-8')


            cadastrar_produto(nome, valor, descricao)
            time.sleep(1)  # Espera um segundo entre cada cadastro para evitar problemas de velocidade

# Nome do arquivo CSV
arquivo_csv = 'products.csv'

# Chama a função para cadastrar os produtos do arquivo CSV
cadastrar_produtos_arquivo(arquivo_csv)

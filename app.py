# Para instalar: pip install pyautogui pandas
import pyautogui
from time import sleep
import pandas as pd

pyautogui.PAUSE = 0.5

# Abrir navegador (Chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Entrar no site do sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
sleep(2)  # Esperar carregar o site

# Realizar login
pyautogui.click(x=766, y=461)
pyautogui.write('pythonautogui@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(2)  # Esperar a próxima página carregar

# Carregar base de dados de produtos
tabela = pd.read_csv('produtos.csv')
print(tabela)

# Cadastrar produtos
for linha in tabela.index:
    codigo = str(tabela.loc[linha, 'codigo'])

    pyautogui.click(x=642, y=327)
    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.scroll(5000)

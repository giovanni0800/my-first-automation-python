import pyautogui
import time

pyautogui.PAUSE = 0.5

#Acessa o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Espera 3 segundos e acessa o host da hashtag para cadastrar os itens
time.sleep(2)
pyautogui.write("file:///C:/Users/Samsung/Documents/Estudos/Python/02.%20Python%20Scripts/Jupyter/Aula%2001/front-end/index.html")
pyautogui.press("enter")

#Espera 3 segundos e clica no primeiro input pra entrar com e-mail, usa o tab para colocar a senha e dar o submit
time.sleep(2)
pyautogui.click(x=319, y=338)
pyautogui.write("admin@admin.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("tab")
pyautogui.press("enter")

#Acesso a base de dados csv
import pandas as pd

tabela_dados = pd.read_csv("produtos.csv")

#index representa a linha da tabela e column a coluna
for linha_atual in tabela_dados.index:
    
    codigo = str(tabela_dados.loc[linha_atual, "codigo"])
    marca = str(tabela_dados.loc[linha_atual, "marca"])
    tipo = str(tabela_dados.loc[linha_atual, "tipo"])
    categoria = str(tabela_dados.loc[linha_atual, "categoria"])
    preco = str(tabela_dados.loc[linha_atual, "preco_unitario"])
    custo = str(tabela_dados.loc[linha_atual, "custo"])

    obs = str(tabela_dados.loc[linha_atual, "obs"])
    if ( str.upper(obs) == str.upper("nan") ):
        obs = ""

    pyautogui.click(x=320, y=334)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(marca)
    pyautogui.press("tab")
    pyautogui.write(tipo)
    pyautogui.press("tab")
    pyautogui.write(categoria)
    pyautogui.press("tab")
    pyautogui.write(preco)
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")
    pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(7777)

print("---------------------")
print("---------------------")
print("------- Fim -------")
print("---------------------")
print("---------------------")
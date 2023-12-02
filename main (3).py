# APIS
# from collections.abc import MutableSet
# import requests
# import tkinter

# # # URL da API que queremos acessar
# # url = 'https://api.kanye.rest'

# # # Fazendo uma solicitação GET para a API
# # response = requests.get(url)

# # # Verificando se a solicitação foi bem-sucedida
# # if response.status_code == 200:
  
# # # A resposta da API está em formato JSON, então podemos analisá-la para obter os dados
# #     data = response.json()

# # # Agora, você pode processar e trabalhar com os dados conforme necessário
# #     for user in data:
# #         print(f"Nome: {user['name']}, Email: {user['email']}")
# # else:
# #     print(f"A solicitação falhou com código de status {response.status_code}")


# Criando a janela principal
import tkinter as tk
#Criar uma função para fazer a soma de 2 numeros
def soma():
  n1 = float(entrada1.get())
  n2 = float(entrada2.get())
  resultado = n1 + n2
  resultado_label.config(text = f'resultado: {resultado}')


def sub():
  n1 = float(entrada1.get())
  n2 = float(entrada2.get())
  resultado = n1 - n2
  resultado_label.config(text = f'resultado: {resultado}')

def div():
  n1 = float(entrada1.get())
  n2 = float(entrada2.get())
  if n2 != 0:
      resultado = n1 / n2
      resultado_label.config(text = f'Resultado da divisão: {resultado:.2f}')
  else:
      resultado_label.config(text="Erro: Divisão por zero")
  
def mult():
  n1 = float(entrada1.get())
  n2 = float(entrada2.get())
  resultado = n1 * n2


#criar label com nome calculadora
janela = tk.Tk()
janela.title('Calculadora')
label1 = tk.Label(janela,font ="Tahoma", text = "Digite o nº 1: ")
label1.pack()
entrada1 = tk.Entry(janela,font ="Arial", width= 6, bg = 'blue', fg = 'black')
entrada1.pack()

label2 = tk.Label(janela,font ="Arial", text = "Digite o nº 2: ")
label2.pack()
entrada2 = tk.Entry(janela,font ="Arial", width= 6, bg = 'blue', fg = 'black')
entrada2.pack()

#criar um botao para somar
bt = tk.Button(janela,font ="Arial",bg = 'red', text ="+", command = soma)
bt.pack()
resultado_label = tk.Label(janela)
resultado_label.pack()

# Criar um botao de subtração
bt = tk.Button(janela,font ="Arial",bg = 'green', text ="-", command = sub)
bt.pack()
resultado_label = tk.Label(janela)
resultado_label.pack()

# Criar um botao de Multiplicação
bt = tk.Button(janela,font ="Arial", bg = 'white', text ="*", command = mult)
bt.pack()
resultado_label = tk.Label(janela)
resultado_label.pack()

# Criar um botao de Divisão
bt = tk.Button(janela,bg = 'orange', text ="/", command = div)
bt.pack()
resultado_label = tk.Label(janela)
resultado_label.pack()
resultado_label.config(text="Erro: Divisão por zero")

janela.mainloop()


import tkinter as tk

janela = tk.Tk()
janela.title("calculadora")
janela.geometry("300x400")

entrada = tk.Entry(janela, font=("arial", 20),bd=5, relief="ridge", justify="right")
entrada.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

def clicar(valor):
    entrada.insert(tk.END, valor)

def limpar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str (resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "erro")

botoes = [
    "7", "8", "9", "/",
    "4","5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
    ]
linha = 0
coluna = 0

for botao in botoes:
    if botao == "C":
        comando = limpar
    elif botao == "=":
        comando = calcular
    else:
        comando = lambda x=botao: clicar(x)

    tk.Button(janela, text=botao, font=("arial", 18),
              command=comando, width=5, height=2).place(x=coluna*70, y=100+linha*60)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

janela.mainloop()
    

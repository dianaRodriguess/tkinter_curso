from tkinter import *

# configurações da tela
root = Tk()
root.title("Calculadora simples")
root.resizable(0, 0)


# funções
def clicarButao(num):
    atual = entrada.get()  # pega o que tá la
    entrada.delete(0, END)  # deleta o que tá la para não haver repetição
    entrada.insert(0, str(atual) + str(num))  # concatena com o numero inserido

def limpar():
    entrada.delete(0, END)

def somar():
    numero = entrada.get()
    global n1
    global opr
    opr = "soma"
    n1 = int(numero)
    entrada.delete(0, END)

def subtrair():
    numero = entrada.get()
    global n1
    global opr
    opr = "sub"
    n1 = int(numero)
    entrada.delete(0, END)

def multiplicar():
    numero = entrada.get()
    global n1
    global opr
    opr = "multi"
    n1 = int(numero)
    entrada.delete(0, END)

def dividir():
    numero = entrada.get()
    global n1
    global opr
    opr = "div"
    n1 = int(numero)
    entrada.delete(0, END)

def resultado():
    n2 = entrada.get()
    entrada.delete(0, END)
    
    match opr:
        case "soma":
            entrada.insert(0, n1 + int(n2))
        case "sub":
            entrada.insert(0, n1 - int(n2))
        case "multi":
            entrada.insert(0, n1 * int(n2))
        case "div":
            entrada.insert(0, n1 / int(n2))
            

# campo de entrada
entrada = Entry(root, width=45, borderwidth=3)
entrada.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# definir os botões
butao_1 = Button(root, text="1", padx=40, pady=20, command=lambda: clicarButao(1))
butao_2 = Button(root, text="2", padx=40, pady=20, command=lambda: clicarButao(2))
butao_3 = Button(root, text="3", padx=40, pady=20, command=lambda: clicarButao(3))
butao_4 = Button(root, text="4", padx=40, pady=20, command=lambda: clicarButao(4))
butao_5 = Button(root, text="5", padx=40, pady=20, command=lambda: clicarButao(5))
butao_6 = Button(root, text="6", padx=40, pady=20, command=lambda: clicarButao(6))
butao_7 = Button(root, text="7", padx=40, pady=20, command=lambda: clicarButao(7))
butao_8 = Button(root, text="8", padx=40, pady=20, command=lambda: clicarButao(8))
butao_9 = Button(root, text="9", padx=40, pady=20, command=lambda: clicarButao(9))
butao_0 = Button(root, text="0", padx=40, pady=20, command=lambda: clicarButao(0))
butao_mais = Button(root, text="+", padx=40, pady=20, command=somar)
butao_menos = Button(root, text="-", padx=40, pady=20, command=subtrair)
butao_multi = Button(root, text="*", padx=40, pady=20, command=multiplicar)
butao_div = Button(root, text="/", padx=40, pady=20, command=dividir)
butao_igual = Button(root, text="=", padx=40, pady=20, command=resultado)
butao_limpar = Button(root, text="C", padx=40, pady=20, command=limpar)

# colocar os botões na grade
butao_9.grid(row=1, column=2)
butao_8.grid(row=1, column=1)
butao_7.grid(row=1, column=0)

butao_6.grid(row=2, column=2)
butao_5.grid(row=2, column=1)
butao_4.grid(row=2, column=0)

butao_3.grid(row=3, column=2)
butao_2.grid(row=3, column=1)
butao_1.grid(row=3, column=0)

butao_0.grid(row=4, column=0)
butao_mais.grid(row=1, column=4)
butao_menos.grid(row=2, column=4)
butao_multi.grid(row=3, column=4)
butao_div.grid(row=4, column=4)

butao_limpar.grid(row=4, column=1)
butao_igual.grid(row=4, column=2)

# manter a janela aberta
root.mainloop()

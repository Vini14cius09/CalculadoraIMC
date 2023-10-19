from tkinter import *
from tkinter import Tk

def calcular():
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())
    IMC = peso / altura**2
    resultado = IMC
    if resultado < 18.5:
     seu_imc['text'] = ('Seu IMC é: Abaixo do peso')
    elif resultado >= 18.5 and IMC < 25:
     seu_imc['text'] = ('Seu IMC é: Normal')
    elif resultado >= 25 and IMC < 30:
     seu_imc['text'] = ('Seu IMC é: Sobrepeso')
    else:
     seu_imc['text'] = ('Seu IMC é: Obsidade')
    resultado_label['text'] = "{:.{}f}".format(resultado,2)


janela = Tk()
janela.title('')
janela.geometry('295x230')

peso_imc = Label(janela, text= 'Insira seu peso: ',font=10)
peso_imc.pack()
peso_entry = Entry(font=10)
peso_entry.pack()

altura_imc = Label(janela, text='Insira sua altura: ',font=10)
altura_imc.pack()
altura_entry = Entry(font=10)
altura_entry.pack()

calcular_btn = Button(janela, text="CALCULAR", command=calcular)
calcular_btn.pack()

resultado_label = Label(janela, width=10, height=2,font=11)
resultado_label.pack()

seu_imc = Label(janela, text='',font=10)
seu_imc.pack()

janela.mainloop()
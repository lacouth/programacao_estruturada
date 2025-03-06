import tkinter as tk
from tkinter import ttk

def contar():
    texto = entrada.get()
    print(type(texto))
    letras = len(texto)
    palavras = len(texto.split())
    resultado = f'O texto informado tem {letras} letras e {palavras} palavras'
    mensagem.config(text=resultado)
    entrada.delete(0,'end')

app = tk.Tk()
app.title('Contador')
app.geometry('500x150')
app.grid_columnconfigure(0,weight=1)

titulo = ttk.Label(app,text='Contador de Letras e Palavras', font=('Times',28))
titulo.grid(row=0,column=0,padx=10,pady=10,columnspan=2)


entrada = ttk.Entry(app,width=40)
entrada.grid(row=1,column=0)

botao = ttk.Button(app,text='Contar',command=contar)
botao.grid(row=1,column=1,padx=10,pady=10)

mensagem = ttk.Label(app,text="")
mensagem.grid(row=2,column=0,columnspan=2)


app.mainloop()
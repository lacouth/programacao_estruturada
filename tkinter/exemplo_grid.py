import tkinter as tk
from tkinter import ttk

def trocar_texto():
    label.config(text='Botão Clicado!',foreground='red')

def trocar_cor():
    label.config(foreground='green')

app = tk.Tk()
app.title('Formulário')
app.geometry('600x200')
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)

label = ttk.Label(app,text='Formulário de Inscrição',font=('Times',32))
label.grid(row=0,column=0,columnspan=5,padx=10,pady=40)

botao = ttk.Button(app,text='Clique aqui!',command=trocar_texto)
botao.grid(row=1,column=0)

botao2 = ttk.Button(app,text='Clique Aqui Também', command=trocar_cor)
botao2.grid(row=1,column=1)


app.mainloop()
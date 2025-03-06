import tkinter as tk
from tkinter import ttk

dados = {}
def cadastrar():
    nome = entrada_nome.get()
    matricula = entrada_matricula.get()
    if len(nome) and len(matricula):
        if nome not in dados:
            dados[nome] = matricula
            etiqueta_mensagem.config(text='Cadastro efetuado com sucesso!',foreground='green')
            entrada_nome.delete(0,'end')
            entrada_matricula.delete(0,'end')

            tabela.insert('','end',values=(len(dados),nome,dados[nome]))
        else:
            etiqueta_mensagem.config(text='Nome já cadastrado!',foreground='red')
    else:
        etiqueta_mensagem.config(text='Nome ou Matrícula vazios',foreground='red')
    

app = tk.Tk()
app.title('App')
app.geometry('800x600')

menu_bar = tk.Menu(app)
app.config(menu=menu_bar)

arquivo_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
arquivo_menu.add_command(label="Novo", command=lambda: print("Novo"))
arquivo_menu.add_command(label="Abrir", command=lambda: print("Abrir"))
arquivo_menu.add_command(label="Salvar", command=lambda: print("Salvar"))
arquivo_menu.add_separator()  # Adiciona um separador
arquivo_menu.add_command(label="Sair", command=app.quit)

# Cria o menu "Editar"
editar_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Editar", menu=editar_menu)
editar_menu.add_command(label="Cortar", command=lambda: print("Cortar"))
editar_menu.add_command(label="Copiar", command=lambda: print("Copiar"))
editar_menu.add_command(label="Colar", command=lambda: print("Colar"))

# Cria o menu "Ajuda"
ajuda_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Ajuda", menu=ajuda_menu)
ajuda_menu.add_command(label="Sobre", command=lambda: print("Exemplo de Menu com Tkinter"))

app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)


titulo = ttk.Label(app,text='Formulário de Inscrição',font=('Times',32)).grid(row=0,column=0,columnspan=2,padx=40,pady=40)

etiqueta_nome = ttk.Label(app,text='Nome:', font=('Times',14)).grid(row=1,column=0,sticky='W',padx=20,pady=20)
entrada_nome = ttk.Entry(app,width=50)
entrada_nome.grid(row=1,column=1,padx=20,pady=20,stick='W')

etiqueta_matricula = ttk.Label(app,text='Matrícula:',font=('Times',14)).grid(row=2,column=0,sticky='W',padx=20,pady=20)
entrada_matricula = ttk.Entry(app,width=50)
entrada_matricula.grid(row=2,column=1,padx=20,pady=20,sticky='W')

botao_cadastrar = ttk.Button(app,text='Cadastrar',width=50,command=cadastrar).grid(row=3,column=0,columnspan=2)
etiqueta_mensagem = ttk.Label(app,text='',font=('Times',14))
etiqueta_mensagem.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

tabela = ttk.Treeview(app,columns=('#','Nome','Matrícula'),show='headings')
tabela.grid(row=5,column=0,columnspan=2)
tabela.heading('#',text='#')
tabela.heading('Nome',text='Nome')
tabela.heading('Matrícula',text='Matrícula')

app.mainloop()
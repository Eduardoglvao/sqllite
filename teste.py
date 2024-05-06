from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

def criar_banco_dados():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

def adicionar_cliente(nome, email):
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO clientes (nome, email) VALUES (?, ?)''', (nome, email))
    conn.commit()
    conn.close()

def remover_cliente():
    try:
        id_cliente = int(userEntryId.get())
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM clientes WHERE id = ?''', (id_cliente,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "ID do cliente deve ser um número inteiro.")

def atualizar_cliente():
    try:
        id_cliente = int(userEntryId.get())
        novo_nome = userEntryNovoNome.get()
        novo_email = userEntryNovoEmail.get()
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()
        cursor.execute('''UPDATE clientes SET nome = ?, email = ? WHERE id = ?''', (novo_nome, novo_email, id_cliente))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "ID do cliente deve ser um número inteiro.")

def cadastrar():
    nome = userEntryNome.get()
    email = userEntryEmail.get()
   
    if nome == '' or email == '':
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return
   
    adicionar_cliente(nome, email)
    messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")

janela = Tk()
janela.title('Odonto Locchi - Página de Cadastro')
janela.geometry('600x400')
janela.configure(background='WHITE')
janela.resizable(width=False, height=False)
janela.attributes('-alpha', 0.9)

leftFrame = Frame(janela, width=200, height=400, bg='#3696A3', relief='raise')
leftFrame.pack(side=LEFT)

rightFrame = Frame(janela, width=395, height=400, bg='#3696A3', relief='raise')
rightFrame.pack(side=RIGHT)

tituloLabel = Label(rightFrame, text='Odonto Locchi', font=('Century Gothic', 24),bg='#3696A3', fg='WHITE' )
tituloLabel.place(x=75, y=35)

userLabelNome = Label(rightFrame, text='Nome:', font=('Century Gothic', 20), bg='#3696A3', fg='WHITE')
userLabelNome.place(x=40, y=100)

userEntryNome = ttk.Entry(rightFrame, width=30)
userEntryNome.place(x=150, y=113)

userLabelEmail = Label(rightFrame, text='Email:', font=('Century Gothic', 20), bg='#3696A3', fg='WHITE')
userLabelEmail.place(x=50, y=140)

userEntryEmail = ttk.Entry(rightFrame, width=30)
userEntryEmail.place(x=150, y=153)

loginButton = ttk.Button(rightFrame, text='Cadastre-se', width=20, command=cadastrar)
loginButton.place(x=124, y=190)

userLabelId = Label(rightFrame, text='ID do cliente:', font=('Century Gothic', 20), bg='#3696A3', fg='WHITE')
userLabelId.place(x=40, y=250)

userEntryId = ttk.Entry(rightFrame, width=10)
userEntryId.place(x=200, y=263)

userLabelNovoNome = Label(rightFrame, text='Novo nome:', font=('Century Gothic', 20), bg='#3696A3', fg='WHITE')
userLabelNovoNome.place(x=40, y=290)

userEntryNovoNome = ttk.Entry(rightFrame, width=30)
userEntryNovoNome.place(x=200, y=303)

userLabelNovoEmail = Label(rightFrame, text='Novo email:', font=('Century Gothic', 20), bg='#3696A3', fg='WHITE')
userLabelNovoEmail.place(x=40, y=330)

userEntryNovoEmail = ttk.Entry(rightFrame, width=30)
userEntryNovoEmail.place(x=200, y=343)

removerButton = ttk.Button(rightFrame, text='Remover cliente', width=20, command=remover_cliente)
removerButton.place(x=60, y=380)

atualizarButton = ttk.Button(rightFrame, text='Atualizar cliente', width=20, command=atualizar_cliente)
atualizarButton.place(x=250, y=380)

criar_banco_dados()

janela.mainloop()
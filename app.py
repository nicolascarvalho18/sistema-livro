import tkinter as tk
from tkinter import messagebox

livros = []

class Livro:
    def __init__(self, nome, autor, genero):
        self.nome = nome
        self.autor = autor
        self.genero = genero

    def __str__(self):
        return f"{self.nome} - {self.autor} ({self.genero})"

def cadastrar_livro():
    nome = entry_livro_nome.get()
    autor = entry_livro_autor.get()
    genero = entry_livro_genero.get()

    if nome == "" or autor == "" or genero == "":
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    livro = Livro(nome, autor, genero)
    livros.append(livro)
    messagebox.showinfo("Sucesso", f"Livro '{nome}' cadastrado com sucesso!")
    atualizar_lista_livros()

def atualizar_lista_livros():
    lista_livros.delete(0, tk.END)
    for livro in livros:
        lista_livros.insert(tk.END, str(livro))


def excluir_livro():
    try:
        selecionado = lista_livros.curselection()[0]
        livro = livros[selecionado]
        livros.remove(livro)
        messagebox.showinfo("Sucesso", f"Livro '{livro.nome}' excluído com sucesso!")
        atualizar_lista_livros()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione um livro para excluir.")


def editar_livro():
    try:
        selecionado = lista_livros.curselection()[0]
        livro = livros[selecionado]

        novo_nome = entry_livro_nome.get()
        novo_autor = entry_livro_autor.get()
        novo_genero = entry_livro_genero.get()

        if novo_nome == "" or novo_autor == "" or novo_genero == "":
            messagebox.showwarning("Aviso", "Preencha todos os campos para editar.")
            return

        livro.nome = novo_nome
        livro.autor = novo_autor
        livro.genero = novo_genero

        messagebox.showinfo("Sucesso", f"Livro '{livro.nome}' editado com sucesso!")
        atualizar_lista_livros()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione um livro para editar.")


root = tk.Tk()
root.title("Sistema de Cadastro de Livros e Leitores")
root.geometry("600x400")


tk.Label(root, text="Cadastro de Livro").pack(pady=5)
tk.Label(root, text="Nome do Livro").pack()
entry_livro_nome = tk.Entry(root)
entry_livro_nome.pack()

tk.Label(root, text="Autor do Livro").pack()
entry_livro_autor = tk.Entry(root)
entry_livro_autor.pack()

tk.Label(root, text="Gênero do Livro").pack()
entry_livro_genero = tk.Entry(root)
entry_livro_genero.pack()

tk.Button(root, text="Cadastrar Livro", command=cadastrar_livro).pack(pady=5)


tk.Label(root, text="Livros Cadastrados").pack(pady=5)
lista_livros = tk.Listbox(root, height=6, width=50)
lista_livros.pack()


tk.Button(root, text="Excluir Livro", command=excluir_livro).pack(pady=5)
tk.Button(root, text="Editar Livro", command=editar_livro).pack(pady=5)


atualizar_lista_livros()
root.mainloop()

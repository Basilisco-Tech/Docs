import tkinter as tk
from tkinter import messagebox

def exit(): 
    nova_janela.destro


def cadastro_usuario():
    novo_usuario = novo_usuario_entry.get().strip()
    nova_senha = nova_senha_entry.get().strip()
    
    # Abra os arquivos de usuários e senhas em modo de escrita (append)
    with open('Users.txt', 'a') as users_file, open('Password.txt', 'a') as password_file:
        # Escreva o novo usuário e senha nos arquivos
        users_file.write(f'\n{novo_usuario}')
        password_file.write(f'\n{nova_senha}')
    
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!") 
        exit()
    
class NovaJanela(tk.Toplevel):

    def __init__(self, master):

        super().__init__(master)

        self.title("Cadastro")

        largura_tela = self.winfo_screenwidth()

        altura_tela = self.winfo_screenheight()

        self.geometry(f"{largura_tela}x{altura_tela}")

        novo_usuario_label = tk.Label(self, text="Novo Usuário:")

        novo_usuario_label.pack()

        global novo_usuario_entry

        novo_usuario_entry = tk.Entry(self)

        novo_usuario_entry.pack()

        nova_senha_label = tk.Label(self, text="Senha:")

        nova_senha_label.pack()

        global nova_senha_entry

        nova_senha_entry = tk.Entry(self, show="*")

        nova_senha_entry.pack()

        new_login = tk.Button(self, text="Cadastrar usuário", command=cadastro_usuario)

        new_login.pack()

        
#Definimos verificar_login para o sistema de verificação dos txt.
def verificar_login():

    nome_login = nome_usuario_entry.get().strip() #Atribui nome_usuario ao nome_login

    senha_login = senha_entry.get().strip()#Atribui o senha ao senha_login

    user = open('Users.txt','r')#Abre o txt de usuários e faz a leitura

    password = open('Password.txt','r')#Abre o txt de senhas e faz a leitura

    user_file = user.read().splitlines()#Atribui a leitura dinâmica a variável user_file

    password_file = password.read().splitlines()#Atribui a leitura dinâmica a variável password_file

    if nome_login in user_file: #Se o nome_login estiver em user_file, ele seguirá com o código

        index = user_file.index(nome_login) #O uso de index é para fazer a verificação dentro de listas, nesse caso, dentro do nome_login

        if senha_login == password_file[index]: #Se senha_login for exatamente igual a password_file (que por consequencia precisa estar verificada com o nome), ele aprovará

            messagebox.showinfo("Login", "Login bem-sucedido!")

            global nova_janela

            nova_janela = NovaJanela(root) #Atribuimos o nome de nova_janela a classe criada acima.
            
            root.withdraw() #Comando para ocultar a janela principal quando a janela secundária for aberta

        else:
            messagebox.showerror("Erro no Login", "Nome de usuário ou senha incorretos, tente novamente!")
    else:
        messagebox.showerror("Erro no Login", "Nome de usuário ou senha incorretos, tente novamente!")

#Cria a página 
root = tk.Tk()
root.title("Login")

#Definindo tamanho da janela
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
root.geometry(f"{largura_tela}x{altura_tela}")

#Definindo a entrada de dados de nome e suas respectivas descrições
nome_usuario_label = tk.Label(root, text="Nome de Usuário:")
nome_usuario_label.pack()
nome_usuario_entry = tk.Entry(root, width=80%largura_tela)
nome_usuario_entry.pack()
#Definindo a entrada de dados de senha e suas respectivas descrições
senha_label = tk.Label(root, text="Senha:")
senha_label.pack()
senha_entry = tk.Entry(root,width= 80%largura_tela, show="*")
senha_entry.pack()

#Definindo para onde o botão vai e o que está escrito nele.
login_button = tk.Button(root, text="Login", command=verificar_login)
login_button.pack()

#Mantém a página aberta
root.mainloop()

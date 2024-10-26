import tkinter as tk
from tkinter import RIGHT, PhotoImage, ttk, messagebox
from PIL import Image, ImageTk 
import customtkinter as ctk
import sqlite3 as lite
import DataBaseLogin
 
#aparencia da janela
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

#criando a janela 
janela =ctk.CTk()
janela.geometry ("700x400")
janela.title ("Sistema de Login - Controle de Produtos")
janela.resizable(False, False)
janela.attributes("-alpha", 0.9)

#Add ícone
icone= Image.open("img.png")
icone.save("img.ico", format="ICO", sizes=[(32,32)])
janela.iconbitmap(default="img.ico")

#adicionando imagem
img_path = 'img.png'
imagem = Image.open(img_path)
imagem_redimensionada=imagem.resize((350,400))
imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
label_imagem = tk.Label(janela, image=imagem_tk)
label_imagem.place(x=0, y=0)

#frame
frame = ctk.CTkFrame(
    master=janela,
      width=350,
        height=396)
frame.pack(side=RIGHT)

#frame widgets
label= ctk.CTkLabel(
    master=frame,
      text="Controle de Produtos",
        font=("Roboto", 30),
          text_color="white")
label.place (x=25, y=5)

label2= ctk.CTkLabel(
    master=frame,
      text="Login",
        font=("Roboto", 20),
          text_color="#A9A9A9"
          )
label2.place (x=25, y=70)

label3=ctk.CTkLabel(
    master=frame,
      text="*Username obrigatório.",
        text_color="#2F4F4F",
          font=("Roboto",10)
          )
label3.place(x=25, y=135)


label4=ctk.CTkLabel(
    master=frame,
      text="*Senha obrigatória.",
        text_color="#2F4F4F",
          font=("Roboto",10)
          )
label4.place(x=25, y=205)

checkbox=ctk.CTkCheckBox(
    master=frame,
      text="Lembrar-se de mim sempre"
      )
checkbox.place(x=25, y=235)

#criando Entrys
usuario_entry = ctk.CTkEntry(
    master=frame,
      placeholder_text="Nome de usuário",
        width=300,
          font=("Roboto",14)
          )
usuario_entry.place(x=20, y=105)

senha_entry = ctk.CTkEntry(
    master=frame,
      placeholder_text="Senha de usuário",
        width=300,
         show="*",
          font=("Roboto",14)
          )
senha_entry.place(x=20, y=175)

#criando funções

def login():
    user= usuario_entry.get()
    senha=senha_entry.get()

    cursor= DataBaseLogin.get_cursor()
    cursor.execute(
        '''SELECT * FROM Login
        WHERE (usuario=? and senha=?)
        ''', (user, senha) )

    verify_login=cursor.fetchone()
    
    if verify_login:
            messagebox.showinfo(title="Login info", message="Acesso confirmado. Bem-vinde!")
    else:
            messagebox.showerror(title="Login info", message="Acesso Negado. Usuario não cadastrado.")
            usuario_entry.delete(0,'end')
            senha_entry.delete(0,'end')

def deslocar_widgets():
    label2.place(x=5000)
    label3.place(x=5000)
    label4.place(x=5000)
    log_button.place(x=5000)
    cadastro_button.place(x=5000)
    checkbox.place(x=5000)

def cadastrar ():
   label_cadastrar = ctk.CTkLabel (
          master=frame,
           text="Cadastre-se aqui!",
            text_color="#2F4F4F",
             font=("Roboto",18),
          )
   label_cadastrar.place(x=85, y=100)
   deslocar_widgets()
   usuario_entry.place(x=20, y=150)
   senha_entry.place(x=20, y=200)

   def backToMain():
    usuario=usuario_entry.get()
    senha= senha_entry.get() 
    

    if (usuario == '' or senha == ''):
         messagebox.showerror(
              title="Cadastro info",
                message="Defina todos os campos."
                )
    else:
         DataBaseLogin.insert_table(usuario, senha)

         label2.place(x=25, y=70)
         label4.place(x=25, y=205)
         label3.place(x=25, y=135)
         checkbox.place(x=25, y=235)
         usuario_entry.place(x=20, y=105)
         senha_entry.place(x=20, y=175)
         label_cadastrar.place(x=5000)
         backToMain_button.place_forget()
         cadastro_button.place(x=25, y=320)
         log_button.place(x=25, y=285)

   backToMain_button = ctk.CTkButton(
    master=frame,
      text="Salvar",
        width=150,
          hover_color="#2F4F4F",
           command= backToMain
             
          )
   backToMain_button.place(x=85, y=270)  


    
#criando botões    
log_button = ctk.CTkButton(
    master=frame,
      text="Login",
        width=300,
          hover_color="#2F4F4F",
           command=login
          )
log_button.place(x=25, y=285)

cadastro_button = ctk.CTkButton(
    master=frame,
      text="Cadastrar",
        width=300,
          hover_color="#2F4F4F",
            command= cadastrar
          )
cadastro_button.place(x=25, y=320)

#looping obrigatório para funcionamento
janela.mainloop()


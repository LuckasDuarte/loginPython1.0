from os import close, name
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD
import DataBaseUsers


#-----Atributos a janela --------#
janloguin = Tk()

janloguin.title('WMS')
janloguin.geometry('700x500')
janloguin.configure(background='gray')
janloguin.resizable(height=False, width=False)
janloguin.iconbitmap(default="icons/logistica.ico")

#---------------------------------#

#logo imagem
logo = PhotoImage(file='icons/logo.png')



LeftFrame = Frame(janloguin, width=200, height= 300, background='MIDNIGHTBLUE', relief = 'raise' )
LeftFrame.pack(side=LEFT)

RightFrame = Frame(janloguin, width=200, height=300, background='MIDNIGHTBLUE', relief='raise')
RightFrame.pack(side=RIGHT)

RightFrameCenter = Frame(janloguin, width=300, height= 400, background='LIGHTGRAY', relief = 'raise' )
RightFrameCenter.pack(side=RIGHT)

FaixaCentralCima = Frame(janloguin, width=300, height=10, background='MIDNIGHTBLUE', relief='raise')
FaixaCentralCima.place(x=200, y=50)

FaixaCentralBaixa = Frame(janloguin, width=300, height=10, background='MIDNIGHTBLUE', relief='raise')
FaixaCentralBaixa.place(x=200, y=450)

Logolabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
Logolabel.place(x=40, y=100)
#lightgray

logotext = Label(RightFrame, text='Logística\nExpress', font=('Arial', 20, BOLD), background='MIDNIGHTBLUE', fg='white')

logotext.place(x=40, y=100)

#-------- Entradas de texto ----------#

Usertext = Label(RightFrameCenter, text= 'Usuário', font=('arial', 15, BOLD), background='LIGHTGRAY', fg='Black')
Usertext.place(x=109, y=100)

Userentry = ttk.Entry(RightFrameCenter, width=30)
Userentry.place(x=55, y=130)

Passtext = Label(RightFrameCenter, text= 'Senha', font=('arial', 15, BOLD), background='LIGHTGRAY', fg='Black')
Passtext.place(x=115, y=170)

Passentry = ttk.Entry(RightFrameCenter, width=30, show='•')
Passentry.place(x=55, y=200)

#processo de login
def loguin():
    user = Userentry.get()
    Pass = Passentry.get()
    DataBaseUsers.cursor.execute("""
    SELECT * FROM Users
    WHERE (Usuário = ? AND Senha = ?)
    """, (user, Pass))  
    print('SELECIONOU')
    verificarloguin = DataBaseUsers.cursor.fetchone()
    try:
        if (user in verificarloguin and verificarloguin):
            messagebox.showinfo(title='Sucesso', message='Acesso Confirmado!')
    except:
        messagebox.showerror(title='Negado', message='Acesso negado, verifique os dados')


LoguinButton = ttk.Button(RightFrameCenter, width=20 ,text='Login', command=loguin)
LoguinButton.place(x=80, y=250)


def Register():
    #removendo os componentes
    LoguinButton.place(x=5000, y=5000)
    RegisterButton.place(x=5000,y=5000)
    #inserindo componentes
    ConfirmarSenha = ttk.Label(RightFrameCenter, text='Confirme a Senha', font=('arial', 15,BOLD), background='LIGHTGRAY', foreground='Black')
    ConfirmarSenha.place(x=65, y=240)

    def confirmarsenha():
        senha = Passentry.get()
        confirmar = ConfirmarSenhaEntry.get()
        if ( senha and confirmar ==  senha and confirmar):
            print('Senhas Conferem!')
        else:
            messagebox.showerror(title='Erro', message='As senhas não conferem!')

    ConfirmarSenhaEntry = ttk.Entry(RightFrameCenter, width=30, show='•' )
    ConfirmarSenhaEntry.place(x=55, y=270)

    def RegistrarUsers():
        User = Userentry.get()
        senha = Passentry.get()

        if (User == "" or senha == ""):
            messagebox.showerror(title='Erro', message='Preencha todos os campos!')
        else:
            DataBaseUsers.cursor.execute("""
            INSERT INTO Users(Usuário, Senha)VALUES(?, ?)
            """, (User, senha))
            DataBaseUsers.conn.commit()
            messagebox.showinfo(title='Cadastrado', message='Usuário cadastrado com sucesso!')

    registertodata = ttk.Button(RightFrameCenter, width=20, text='Registrar', command=RegistrarUsers and confirmarsenha)
    registertodata.place(x=80, y=360)

    #planejar informação de usuario já existente!!!!


    def Voltar():
        #removendo os componentes
        RegisterButton.place(x=5000, y=5000)
        ConfirmarSenha.place(x=5000, y=5000)
        ConfirmarSenhaEntry.place(x=5000, y=5000)
        registertodata.place(x=5000, y=5000)
        #inserindo os componentes
        LoguinButton.place(x=80, y=250)
        RegisterButton.place(x=80, y=290)

    BackButton = ttk.Button(RightFrameCenter, width=20, text='Voltar', command=Voltar)
    BackButton.place(x=80, y=325)

RegisterButton = ttk.Button(RightFrameCenter, width=20 ,text='Registrar', command=Register)
RegisterButton.place(x=80, y=290)



janloguin.mainloop()







import tkinter as tk
from tkinter import messagebox

# Dados de exemplo (substitua por um banco de dados real)
usuarios = {
    'admin': 'senha123',
    'usuario1': 'senha456'
}

agendas = {
    'admin': [],
    'usuario1': []
}

clinicas = [
    'Clínica A',
    'Clínica B',
    'Clínica C'
]

# Função para fazer login
def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo('Login', 'Login bem-sucedido!')
        abrir_menu(usuario)
    else:
        messagebox.showerror('Login', 'Usuário ou senha incorretos.')

# Função para abrir o menu
def abrir_menu(usuario):
    login_window.destroy()

    menu_window = tk.Tk()
    menu_window.title('Menu')

    label_menu = tk.Label(menu_window, text='Selecione uma opção:')
    label_menu.pack()

    button_agenda = tk.Button(menu_window, text='Agenda de Horários', command=lambda: abrir_agenda(usuario))
    button_agenda.pack()

    button_consulta = tk.Button(menu_window, text='Consulta de Agenda', command=lambda: consultar_agenda(usuario))
    button_consulta.pack()

    button_clinicas = tk.Button(menu_window, text='Clínicas', command=abrir_clinicas)
    button_clinicas.pack()

    button_rede_social = tk.Button(menu_window, text='Rede Social', command=abrir_rede_social)
    button_rede_social.pack()

    button_fechamento = tk.Button(menu_window, text='Fechamento', command=menu_window.destroy)
    button_fechamento.pack()

# Função para abrir a agenda de horários
def abrir_agenda(usuario):
    agenda_window = tk.Tk()
    agenda_window.title('Agenda de Horários')

    label_agenda = tk.Label(agenda_window, text='Agenda de Horários')
    label_agenda.pack()

    # Lógica para exibir e agendar horários
    # ...

# Função para consultar a agenda
def consultar_agenda(usuario):
    consulta_window = tk.Tk()
    consulta_window.title('Consulta de Agenda')

    label_consulta = tk.Label(consulta_window, text='Consulta de Agenda')
    label_consulta.pack()

    # Lógica para exibir a agenda do usuário
    # ...

# Função para abrir as clínicas
def abrir_clinicas():
    clinicas_window = tk.Tk()
    clinicas_window.title('Clínicas')

    label_clinicas = tk.Label(clinicas_window, text='Lista de Clínicas')
    label_clinicas.pack()

    for clinica in clinicas:
        label_clinica = tk.Label(clinicas_window, text=clinica)
        label_clinica.pack()

# Função para abrir a rede social
def abrir_rede_social():
    messagebox.showinfo('Rede Social', 'Funcionalidade de Rede Social em desenvolvimento.')

# Janela de login
login_window = tk.Tk()
login_window.title('Login')

label_usuario = tk.Label(login_window, text='Usuário:')
label_usuario.pack()
entry_usuario = tk.Entry(login_window)
entry_usuario.pack()

label_senha = tk.Label(login_window, text='Senha:')
label_senha.pack()
entry_senha = tk.Entry(login_window, show='*')
entry_senha.pack()

button_login = tk.Button(login_window, text='Login', command=fazer_login)
button_login.pack()

login_window.mainloop()
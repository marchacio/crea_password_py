from sys import version_info
import string

if version_info.major == 2:
    # Python 2.x
    from Tkinter import *
elif version_info.major == 3:
    # Python 3.x
    from tkinter import *

root = Tk()
root.geometry('700x500')
root.title('Crea Password UI')
root.resizable(False, False)

def show_info():
    pass

# def genera_password(caratteri, lunghezza = 1):
#     tipo_caratteri = ''
#
#     if int(caratteri) == 1:
#         tipo_caratteri = string.ascii_lowercase #26
#
#     elif int(caratteri) == 2:
#         tipo_caratteri = string.ascii_lowercase + string.ascii_uppercase #52
#
#     elif int(caratteri) == 3:
#         tipo_caratteri = string.ascii_lowercase + string.ascii_uppercase + string.digits  #62
#
#     elif int(caratteri) == 4:
#         tipo_caratteri = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation #94
#
#     password = ''
#     lung_str_diff = len(tipo_caratteri) - 1
#
#     for i in range(float(lunghezza)):
#         password += tipo_caratteri[randint(0, lung_str_diff)]
#
#     print(password)

rbVar = IntVar()

intro_label = Label(root, text='Benvenuto nel programma di generazione di password', font=('Helvetica', 16))
intro_label.grid(row=0, column=0, sticky=W)
intro2_label = Label(root, text='Creato da Marchacio\n', font=('Helvetica', 13))
intro2_label.grid(row=1, column=0, sticky=W)
info_button = Button(text='Info', command=show_info)
info_button.grid(row=1, column=2, sticky=E)
lunghezza_label = Label(root, text='Quanto dev\'essere lunga la password?')
lunghezza_label.grid(row=8 , column=0, sticky=W)
lunghezza_field = Entry(root)
lunghezza_field.grid(row=8,column = 0)
stampa_password_bottone = Button(root, text='Genera Password!') #command=genera_password(rbVar.get(), float(lunghezza_field.get()))
stampa_password_bottone.grid(row=9, column=0)

def richiama():
    varLabel.set("Radiobutton: " + str(rbVar.get()))

rb1 = Radiobutton(root, text="Semplice (solo lettere minuscle)", variable=rbVar, value=1, command=richiama, pady=5)
rb1.grid(row=3, column=0, sticky=W)

rb2 = Radiobutton(root, text="Media (lettere maiuscole e minuscle)", variable=rbVar, value=2, command=richiama, pady=5)
rb2.grid(row=4, column=0, sticky=W)

rb3 = Radiobutton(root, text="Difficile (lettere maiusc, minusc e numeri)", variable=rbVar, value=3, command=richiama, pady=5)
rb3.grid(row=5, column=0, sticky=W)

rb3 = Radiobutton(root, text="Impossibile (lettere maiusc, minusc, numeri e simboli)", variable=rbVar, value=4, command=richiama, pady=5)
rb3.grid(row=6, column=0, sticky=W)

varLabel = StringVar()
tkLabel = Label(root, textvariable=varLabel)
tkLabel.grid(row=7, column=0)

root.mainloop()

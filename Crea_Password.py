# coding=utf-8

from os import system as command

try:
    from termcolor import cprint
except:
    command('pip install termcolor')
    from termcolor import cprint

try:
    from clipboard import copy
except:
    command('pip install clipboard')
    from clipboard import copy


from subprocess import check_output
import readline
from random import randint
from sys import argv
import string

parametri_sys = argv

def genera_password(tipo_caratteri, lunghezza):
    password = ''
    lung_str_diff = len(tipo_caratteri) - 1
    print('\n') #CREA SPAZIO

    for i in range(lunghezza):
        password += tipo_caratteri[randint(0, lung_str_diff)]

    cprint(' ' + password, 'yellow')

    try:
        seconda_scelta = int(input(
    '''\n\nCosa vuoi fare adesso?

 1 - Scriverla su un file.txt
 2 - Creane un\'altra
 3 - Copiarlo nella clipboard
 4 - Cancellare i comandi del terminale e uscire dal programma

 0 - Uscire dal programma

 '''))

        if seconda_scelta == 1:

            nome = input('\n Scegli il nome del file (senza estenzione): ')
            home = check_output(['xdg-user-dir', 'DESKTOP'])
            # print(home[0:-1] + '/' + nome + '.txt')
            path = home[0:-1] + '/' + nome + '.txt'

            try:
                f = open(path , 'w')
                f.write(path + '\n\nLa tua password è: ' + password)
                f.close()
                cprint('\n La tua password è stata salvata in ' + path, 'green')
                print('\n Grazie e arrivederci!\n\n**********************************************************')
            except:
                cprint('\n Qualcosa è andato storto...', 'red')
                decisione_tipo_password()


        elif seconda_scelta == 2:
            print('\n**********************************************************\n')
            decisione_tipo_password()
        elif seconda_scelta == 3:
            copy(password)
            cprint('Password salvata negli appunti!\n\n Grazie e arrivederci!\n', 'blue')

        elif seconda_scelta == 4:
            command('clear')

        elif seconda_scelta == 0:
            cprint('\n Grazie e arrivederci!\n', 'blue')

        else:
            cprint('\nHAI INSERITO UN NUMERO NON VALIDO!\n', 'red')

    except KeyboardInterrupt:
        cprint('\n Grazie e arrivederci!\n', 'blue')


def decisione_tipo_password():

    try:
        selez = int(input('''
Quanto dev\'essere complicata la nuova password?

 1 - facile        (solo lettere minuscole)
 2 - media         (lettere min e maiuscole)
 3 - difficile     (lettere min, maiusc e numeri)
 4 - impossibile   (lettere min, maiusc, numeri e caratteri speciali)

 5 - Ottieni informazioni e aiuti
 0 - Esci dal programma

 '''))

        command('clear') #Cancella lo schermo per averlo pulito

        if selez != 0 and selez != 5:
            lungh = int(input('\n Dimmi quanto dev\'essere lunga la password... '))
        
        if selez == 1:
            genera_password(string.ascii_lowercase, lungh) #26

        elif selez == 2:
            genera_password(string.ascii_lowercase + string.ascii_uppercase, lungh) #52

        elif selez == 3:
            genera_password(string.ascii_lowercase + string.ascii_uppercase + string.digits, lungh) #62

        elif selez == 4:
            genera_password(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, lungh) #94

        elif selez == 5:
            input('''

  Programma creato da Marchacio

  Ogni livello di complessità della password corrisponde ad un insieme di lettere che è
  progressivamente più ampio;

  Grazie per avermi provato! (ᵔᴥᵔ)

  Il codice: https://github.com/marchacio/crea_password_py
  Premi invio per uscire della scermata d'aiuto
''')
            command('clear')
            decisione_tipo_password()

        elif selez == 0:
            cprint('\n Grazie e arrivederci!\n', 'blue')

        else:
            command('clear')
            cprint('\n HAI INSERITO UN NUMERO NON VALIDO!', 'red')
            decisione_tipo_password()

    except KeyboardInterrupt:
        cprint('\n Grazie e arrivederci!\n', 'blue')

    except Exception:
        command('clear')
        cprint('\n*********DEVI INSERIRE UN NUMERO PER CONTINUARE*********', 'red')
        decisione_tipo_password()

def intro():  #la scritta d'inizio del programma
    print('********************************************************************')
    cprint('''
 Benvenuto nel programma di creazione di password creato da Marchacio;
 Iniziamo!''', 'yellow')
    decisione_tipo_password()

if __name__ == '__main__':  #inizia il programma quando eseguito
    if len(parametri_sys) == 1 :
        intro()
    else:
        tipo = ''
        if parametri_sys[1] == '1':
            tipo = string.ascii_lowercase
            genera_password(tipo, int(parametri_sys[2]))
        elif parametri_sys[1] == '2':
            tipo = string.ascii_lowercase + string.ascii_uppercase
            genera_password(tipo, int(parametri_sys[2]))
        elif parametri_sys[1] == '3':
            tipo = string.ascii_lowercase + string.ascii_uppercase + string.digits
            genera_password(tipo, int(parametri_sys[2]))
        elif parametri_sys[1] == '4':
            tipo = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            genera_password(tipo, int(parametri_sys[2]))
        else:
            cprint("\n HAI INSERITO UN NUMERO NON VALIDO (" + str(parametri_sys[1])) + ')'
            intro()


from cgitb import reset
from gettext import install
from random import randint
from socket import timeout
from turtle import delay
import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
j = -1
Konto = 1
r = 1
while int (j) != 0:
    
    Einsatz_variable = 0
    x = randint (1,5)
    y = randint (1,5)
    z = randint (1,5)
    u = randint (1,5)
    i = randint (1,5)
    o = randint (1,5)
    p = 20
    r = 1
    print ('Herzlich Wilkommwn bei Bens Spieleautomaten')
    time.sleep (0.5)

    print ('Ihr Kontostand beträgt aktuell',Konto,'Euro')
    time.sleep (0.5)

    while r != 0 :
        Einsatz   = input ('Wie hoch ist dein Einsatz:')

        if float (Einsatz) > float (Konto):
            print ('So viel Geld haben Sie leider nicht, sie können maximal',Konto,'Euro ausgeben')
            r= r+ 1

        else :
            r = 0

    print ('Es wird mit',Einsatz,'Euro gespielt' )
    time.sleep (0.5)

    Eingabe   = input('Bitte deine 1. Glückszahl eingeben 1 bis 5 !: ') 
    Eingabe_2 = input('Bitte deine 2. Glückszahl eingeben 1 bis 5 !: ') 
    Eingabe_3 = input('Bitte deine 3. Glückszahl eingeben 1 bis 5 !: ') 

    while p >= 1 :
        print ('Gewinnzahlen laden:',u,'  ',i,'  ',o)
        p = p-1 
        time.sleep (0.1)
        u = randint (1,9)
        i = randint (1,9)
        o = randint (1,9)
    p = 5
    
    while p >= 1:
        print (bcolors.OKBLUE + 'Gewinnzahlen: ',str (x) ,'  ',str (y),'  ', str (z) + bcolors.ENDC)
        time.sleep(0.1)
        print ( 'Gewinnzahlen: ',str (x) ,'  ',str (y),'  ', str (z))
        time.sleep(0.1)
        p = p-1 
        
    time.sleep (1)
    print ( bcolors.WARNING +'Eingabezahlen:', str(Eingabe),'  ',str(Eingabe_2),'  ',str (Eingabe_3)+ bcolors.ENDC )
    time.sleep (1)

    if int (Eingabe) == int (x) :
        Einsatz_variable = Einsatz_variable + 1
        j = 6
        while int (j) >= 1 :
            print (bcolors.WARNING + 'Eingabezahlen:'+ bcolors.ENDC,bcolors.OKGREEN + str(Eingabe)+ bcolors.ENDC,'  ',bcolors.WARNING + str(Eingabe_2),'  ',str (Eingabe_3)+ bcolors.ENDC)
            time.sleep (0.1)
            print (bcolors.WARNING + 'Eingabezahlen:'+ bcolors.ENDC,str(Eingabe),'  ', bcolors.WARNING +str(Eingabe_2),'  ',str (Eingabe_3)+ bcolors.ENDC)
            time.sleep (0.1)
            j = j-1
        
    if int (Eingabe_2) == int (y) :
        Einsatz_variable = Einsatz_variable + 1
        j = 6
        while int (j) >= 1 :
            print (bcolors.WARNING + 'Eingabezahlen:', str(Eingabe)+ bcolors.ENDC,'  ',bcolors.OKGREEN + str(Eingabe_2)+ bcolors.ENDC,'  ',bcolors.WARNING +str (Eingabe_3)+ bcolors.ENDC)
            time.sleep (0.1)
            print (bcolors.WARNING + 'Eingabezahlen:', str(Eingabe)+ bcolors.ENDC,'  ',str(Eingabe_2),'  ',bcolors.WARNING +str (Eingabe_3)+ bcolors.ENDC)
            time.sleep (0.1)
            j = j-1
    
    if int (Eingabe_3) == int (z) :
        Einsatz_variable = Einsatz_variable + 1
        j = 6
        while int (j) >= 1 :
            print (bcolors.WARNING + 'Eingabezahlen:', str(Eingabe),'  ', str(Eingabe_2)+ bcolors.ENDC,'  ',bcolors.OKGREEN +str (Eingabe_3)+ bcolors.ENDC)
            time.sleep (0.1)
            print (bcolors.WARNING + 'Eingabezahlen:', str(Eingabe),'  ', str(Eingabe_2)+ bcolors.ENDC,'  ',str (Eingabe_3))
            time.sleep (0.1)
            j = j-1


    if int (Einsatz_variable) == 1 :
        Gewinn = float (Einsatz) * 1.5
        print(bcolors.OKGREEN +'Du hast eine Zahl richtig'+ bcolors.ENDC)
    
    if int (Einsatz_variable) == 2 :
        Gewinn = float (Einsatz) * 2
        print(bcolors.OKGREEN +'Du hast zwei Zahl richtig'+ bcolors.ENDC)

    if int (Einsatz_variable) == 3 :
        Gewinn = float (Einsatz) * 2.5
        print(bcolors.OKGREEN +'Du hast drei Zahl richtig'+ bcolors.ENDC)

    if int (Einsatz_variable) == 0 :
        Gewinn = 0
        print(bcolors.FAIL +'Du hast verloren'+ bcolors.ENDC)
    
    time.sleep (0.5)

    print (bcolors.HEADER +'Du hast',Gewinn,'Euro Gewinn gemacht'+ bcolors.ENDC)

    Konto = float(Konto) - float (Einsatz)

    Konto = float(Konto) + float (Gewinn)

    print ('Ihr aktueller Kontostand liegt bei',Konto,'Euro')

    if float(Konto) == 0:
        print ('Du hast leider kein Geld mehr')
        time.sleep (0.5)
        exit()



    time.sleep (0.5)

    j = input ('Möchtetst du noch mal spielen (Ja = 1 /Nein = 0) :')


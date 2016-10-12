# SWP - Simple Write Program 2.0

war = 0 # Not 'war' but 'Write, Append, Read'
signOff = 'signing off........'

def skriv():
    print()
    # Skal skrive (legge til) tekst til fil
    skriv_var = open(war, 'a')
    inn = input('Skriv inn det som skal lagres i fil: ')
    skriv_var.write(inn + '\n')
    skriv_var.close()
    print()
    velg()

def les():
    print()
    # Skal lese fra fil bk1t.txt
    lese = open(war, 'r')
    print('\n' + '##### Utskrift kommer #####' + '\n')
    print(lese.read())
    print('##### Utskrift avsluttet #####')
    lese.close()
    print()
    velg()

def skriv_over():
    print()
    # Skriver over det som er i tekst-filen
    skrivO_var = open(war, 'w')
    innO = input('Skriv inn det som skal OVERSKRIVE til fil: ')
    skrivO_var.write(innO + '\n')
    skrivO_var.close()
    print()
    velg()

def velg():
    print()
    print('Nåværende fil:', war)
    # Velger hvilken funksjon som skal kjøres
    print('w = "write", r = "read", a = "append", rl = "read line"(experimental)')
    print('q = "quit", o = "open file"')
    x = input('w/r/a, rl/o/q? ')
    if x == 'w':
        skriv_over()
    elif x == 'r':
        les()
    elif x == 'a':
        skriv()
    elif x == 'rl':
        les_linje()
    elif x == 'o':
        velg_fil()
    elif x == 'q':
        avslutt()
    print()

def avslutt():
    print()
    for i in range(1, 10, 1): # Det her er mest for å gjere den fancy!
            if i < 8:
                print(signOff[:-i])
            elif i == 8 :
                print('<<signed off!>>')
                    

def les_linje():
    # Testing av å lese spesifikke linjer
    lesL = open(war, 'r')
    print(lesL.readline())
    print()
    lesL.close()
    velg()

def velg_fil():
    print()
    print('Skriv inn filnavn. Finnes ikke filen vil det bli opprettet en ny fil!')
    war = input('Ønsket filnavn: ')
    war += '.txt'
    global war
    print()
    velg()

print('Første gang programmet kjører siden oppstart, spesifiser fil! (o)')
velg()

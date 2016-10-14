# SWP - Simple Write Program v2.5
# Author:
# Joakim Rønneberg Nilsen
# 2016-10-14


# Patch notes:
# Programmet bruker ikke lengre globale variabler, slik det gjorde i v2.0
# Noe endring i rekkefølgen på det som presenteres i oppstarten

# Ellers skal funksjonaliteten til programmet være som før
# Det er fortsatt UTF-8 og Python 3.5 som gjelder 
   
    
def skriv(filnavnS):
    print()
    # Skal skrive (legge til) tekst til fil
    skriv_var = open(filnavnS, 'a')
    inn = input('Skriv inn det som skal lagres i fil: ')
    skriv_var.write(inn + '\n')
    skriv_var.close()
    print()
    velg(filnavnS)

def les(filnavnL):
    print()
    # Skal lese fra fil bk1t.txt
    lese = open(filnavnL, 'r')
    print('\n' + '##### Utskrift kommer #####' + '\n')
    print(lese.read())
    print('##### Utskrift avsluttet #####')
    lese.close()
    print()
    velg(filnavnL)

def skriv_over(filnavnSO):
    print()
    # Skriver over det som er i tekst-filen
    skrivO_var = open(filnavnSO, 'w')
    innO = input('Skriv inn det som skal OVERSKRIVE til fil: ')
    skrivO_var.write(innO + '\n')
    skrivO_var.close()
    print()
    velg(filnavnSO)

def velg(filnavnV):
    print('Nåværende fil:', filnavnV)
    # Velger hvilken funksjon som skal kjøres
    print('w = "write", r = "read", a = "append"')
    print('rl = "read line"(experimental), o = "open file", q = "quit"')
    x = input('w/r/a, rl/o/q? ')
    if x == 'w':
        skriv_over(filnavnV)
    elif x == 'r':
        les(filnavnV)
    elif x == 'a':
        skriv(filnavnV)
    elif x == 'rl':
        les_linje(filnavnV)
    elif x == 'o':
        velg_fil()
    elif x == 'q':
        avslutt()
    print()

def velg_fil():
    print('Skriv inn filnavn. Finnes ikke filen vil det bli opprettet en ny fil!')
    war = input('Ønsket filnavn: ') # Not 'war' but 'Write, Append, Read'
    war += '.txt'
    print()
    velg(war)
    

def avslutt():
    signOff = 'signing off........'
    print()
    for i in range(1, 10, 1): # Det her er mest for å gjere den fancy!
            if i < 8:
                print(signOff[:-i])
            elif i == 8 :
                print('<<signed off!>>')
                    

def les_linje(filnavnLL):
    # Testing av å lese spesifikke linjer
    lesL = open(filnavnLL, 'r')
    print(lesL.readline())
    print()
    lesL.close()
    velg(filnavnLL)


#print('Første gang programmet kjører siden oppstart, spesifiser fil! (o)')
velg_fil()

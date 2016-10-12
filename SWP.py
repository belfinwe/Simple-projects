# Bruk og kast nr 1
# Endret fra "bruk og kast" (bK1) til SWP - Simple Write Program

def skriv():
    # Skal skrive (legge til) tekst til fil
    skriv_var = open('SWP1.txt', 'a')
    inn = input('Skriv inn det som skal lagres i fil: ')
    skriv_var.write(inn + '\n')
    skriv_var.close()
    print()
    gjenta()

def les():
    # Skal lese fra fil bk1t.txt
    lese = open('bk1t.txt', 'r')
    print(lese.read())
    lese.close()
    print()
    gjenta()

def skriv_over():
    # Skriver over det som er i tekst-filen
    skrivO_var = open('SWP1.txt', 'w')
    innO = input('Skriv inn det som skal OVERSKRIVE til fil: ')
    skrivO_var.write(innO + '\n')
    skrivO_var.close()
    print()
    gjenta()

def velg():
    # Velger hvilken funksjon som skal kjøres
    x = input('\nw/r/a? ')
    if x == 'w':
        skriv_over()
    elif x == 'r':
        les()
    elif x == 'a':
        skriv()
    print()

def gjenta():
    # Spør om "programmet" skal gjentas
    y = input('\ngjenta? (j/n) ')
    if y == 'j':
        velg()
    elif y == 'n':
        print('signing off...')

velg()

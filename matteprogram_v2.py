# Matte-program
# 2017-05-05
# v1.0

from tkinter import *
import random

window = Tk()
window.title('Matte')

# Funksjoner

#generer oppgaver

def generer_oppgave_lett():
    var_tilbakemelding.set('')
    var_svar.set('')
    # genere to tall
    # legge sammen eller trekke fra
    # lage oppgaven og ta vare på svaret
    operator_velger = velger()
    fasit = 0
    while int(fasit) <= 0 or int(fasit) > 10:
        siffer1 = random.randrange(1,6)
        siffer2 = random.randrange(1,6)

        if int(operator_velger) == 1:
            operator = '+'
            fasit = (int(siffer1) + int(siffer2))

        else:
            operator = '-'
            fasit = (int(siffer1) - int(siffer2))

    # skriv ut oppgaven
    text = str(siffer1) + operator + str(siffer2)
    var_oppgave.set(text)
    var_fasit.set(fasit)


def generer_oppgave_middels():
    var_tilbakemelding.set('')
    var_svar.set('')
    # genere to tall
    # legge sammen eller trekke fra
    # lage oppgaven og ta vare på svaret
    operator_velger = velger()
    fasit = 0
    while int(fasit) <= 9:
        siffer1 = random.randrange(1,16)
        siffer2 = random.randrange(1,16)

        if int(operator_velger) == 1:
            operator = '+'
            fasit = (int(siffer1) + int(siffer2))

        else:
            operator = '-'
            fasit = (int(siffer1) - int(siffer2))

    # skriv ut oppgaven
    text = str(siffer1) + operator + str(siffer2)
    var_oppgave.set(text)
    var_fasit.set(fasit)

def generer_oppgave_vanskelig():
    var_tilbakemelding.set('')
    var_svar.set('')
    # genere to tall
    # legge sammen eller trekke fra
    # lage oppgaven og ta vare på svaret

    fasit = 0
    while int(fasit) <= 9 and int(fasit) >= 0:
        siffer1 = random.randrange(1,16)
        siffer2 = random.randrange(1,16)
        operator_velger = random.randrange(1,3)

        if int(operator_velger) == 1:
            operator = '+'
            fasit = (int(siffer1) + int(siffer2))

        else:
            operator = '-'
            fasit = (int(siffer1) - int(siffer2))

    # skriv ut oppgaven
    text = str(siffer1) + operator + str(siffer2)
    var_oppgave.set(text)
    var_fasit.set(fasit)


# funksjon for å sjekke om svaret er rett (knappen)
def lever_svar():
    levert_svar = var_svar.get()
    fasit = var_fasit.get()
    oppgave = var_oppgave.get()
    tilbakemelding = oppgave + ' blir ' + str(fasit) + '. Bra gjort!'

    # printe tilbakemelding etter at knappen er trykket
    if int(fasit) == int(levert_svar):
        var_tilbakemelding.set(tilbakemelding)
    elif int(fasit) > int(levert_svar):
        var_tilbakemelding.set('For lavt.')
    elif int(fasit) < int(levert_svar):
        var_tilbakemelding.set('For høyt.')

# Gir mulighet til å bare plusse sammen
def bare_pluss():
    var_operator.set('p')

# Gir mulighet til å bare trekke fra
def bare_minus():
    var_operator.set('m')

# Gir mulighet til å få tilfeldig mellom pluss og minus
def pluss_minus():
    var_operator.set('r')

# Setter opp for lett og middels funksjonene.
# MERK: Vanskelig kjører ikke denne funksjonen, men er låst til å velge tilfeldig
def velger():
    op_velger = var_operator.get()

    if op_velger == 'p':
        var_op_velger = 1
    elif op_velger == 'm':
        var_op_velger = 2
    elif op_velger == 'r':
        var_op_velger = random.randrange(1,3)

    return var_op_velger


# Hovedfunksjoner:
var_operator = StringVar()
var_operator.set('r')


# GUI

# tittel
lbl_tittel = Label(window, text='Velkommen til matteprogrammet!')
lbl_tittel.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=W)

# beskrivelse
lbl_beskrivelse = Label(window, text='Hva blir:')
lbl_beskrivelse.grid(row=3, column=0, padx=5, pady=5, sticky=W)

# oppgaven?
var_oppgave = StringVar()
ent_oppgave = Entry(window, width=6, state='readonly', textvariable=var_oppgave)
ent_oppgave.grid(row=3, column=1, padx=5, pady=5, sticky=W)

# svar-boks
var_svar = StringVar()
ent_svar = Entry(window, width=2, textvariable=var_svar)
ent_svar.grid(row=3, column=2, padx=5, pady=5, sticky=W)

# knapp for å levere svar
btn_svar = Button(window, text='Svar', command=lever_svar)
btn_svar.grid(row=3, column=3, padx=5, pady=5, sticky=W)

# knapp for ny oppgave: lett
btn_nyOppg_lett = Button(window, text='Lett', command=generer_oppgave_lett)
btn_nyOppg_lett.grid(row=4, column=0, padx=5, pady=5, sticky=W)

# knapp for bare pluss-oppgaver
btn_bare_pluss = Button(window, text='+', command=bare_pluss)
btn_bare_pluss.grid(row=4, column=1, padx=5, pady=5, sticky=W)

# tilbakemelding
var_tilbakemelding = StringVar()
ent_tilbakemelding = Entry(window, width=20, state='readonly', textvariable=var_tilbakemelding)
ent_tilbakemelding.grid(row=4, column=2, columnspan=3, padx=5, pady=5, sticky=W)

# knapp for ny oppgave: middels
btn_nyOppg_middels = Button(window, text='Middels', command=generer_oppgave_middels)
btn_nyOppg_middels.grid(row=5, column=0, padx=5, pady=5, sticky=W)

# knapp for bare minus-oppgaver
btn_bare_pluss = Button(window, text='-', command=bare_minus)
btn_bare_pluss.grid(row=5, column=1, padx=5, pady=5, sticky=W)

# knapp for ny oppgave: vanskelig
btn_nyOppg_vanskelig = Button(window, text='Vanskelig', command=generer_oppgave_vanskelig)
btn_nyOppg_vanskelig.grid(row=6, column=0, padx=5, pady=5, sticky=W)

# knapp for minus og pluss
btn_bare_pluss = Button(window, text='+/-', command=pluss_minus)
btn_bare_pluss.grid(row=6, column=1, padx=5, pady=5, sticky=W)

# avslutt
btn_avslutt = Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=6, column=4, padx=5, pady=5, sticky=E)

var_fasit = StringVar()

window.mainloop()

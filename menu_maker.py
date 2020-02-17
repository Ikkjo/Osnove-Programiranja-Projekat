from menus import *
from os import remove

text_red = '\033[91m'
text_green = '\033[32m'
text_end = '\033[0m'


def menu(user):                                                                     #Funkcija za glavni meni


    if user == 'kupac':
        menu = 'kupac'
        options = kupac_options

    elif user == 'menadzer':
        menu = 'menadzer'
        options = menadzer_options

    elif user == 'prodavac':
        menu = 'prodavac'
        options = prodavac_options

    else:
        menu = 'main'
        options = main_options


    while True:
        menu_print[menu]()
        odabir_korisnika = input('Unesite broj željene opcije >> ')
        if (((odabir_korisnika == 'x') or (odabir_korisnika == 'X')) or ((odabir_korisnika in options)) and odabir_korisnika == ''):
            return
        if odabir_korisnika not in options:
            print(text_red + 'Greška, izabrana opcija ne postoji. Pokušajte ponovo.' + text_end)
            continue
        pokretanje_opcija(odabir_korisnika, options)


from menu_options import *


def pokretanje_opcija(odabir_korisnika, options):
    odabir_korisnika = eval(odabir_korisnika) - 1

    for opcija in range(len(options)):
        if odabir_korisnika == opcija:
            opcija += 1
            opcija = str(opcija)
            options[opcija]()
from os import remove

def print_MainMenu():
    try:
        remove('current_user.txt')
    except FileNotFoundError:
        0 + 0
    print('{0:-^60}'.format('GLAVNI MENI'))
    print('|{0:<58}|' .format('1 - Prijava na sistem'))
    print('|{0:<58}|' .format('2 - Registracija na sistem'))
    print_AllUsersMenu()

def print_KupacMenu():
    print('{0:-^60}'.format('MENI ZA KUPCE'))
    print('|{0:<58}|' .format('1 - Kupovina karte'))
    print('|{0:<58}|' .format('2 - Pregled nerealizovanih karata'))
    print('|{0:<58}|' .format('3 - Prijava na let(check-in)'))
    print('|{0:-^58}|'.format('OPCIJE ZA SVE KORISNIKE'))
    print('|{0:<58}|' .format('4 - Pregled nerealizovanih letova'))
    print('|{0:<58}|' .format('5 - Pretraga letova'))
    print('|{0:<58}|' .format('6 - Višekriterijumska pretraga letova'))
    print('|{0:<58}|' .format('7 - Prikaz 10 najjeftinijih letova (po opadajućoj ceni)'))
    print('|{0:<58}|' .format('8 - Fleksibilni polasci'))
    print('|{0:<58}|' .format('X - Odjava'))
    print('-'*60)



def print_MenadzerMenu():
    print('{0:-^60}'.format('MENI ZA MENADŽERE'))
    print('|{0:<58}|'.format('1 - Pretraga prodatih karata'))
    print('|{0:<58}|'.format('2 - Registracija novih prodavaca'))
    print('|{0:<58}|'.format('3 - Kreiranje letova'))
    print('|{0:<58}|'.format('4 - Izmena letova'))
    print('|{0:<58}|'.format('5 - Brisanje karata'))
    print('|{0:<58}|'.format('6 - Izveštaji'))
    print('|{0:-^58}|'.format('OPCIJE ZA SVE KORISNIKE'))
    print('|{0:<58}|' .format('7 - Pregled nerealizovanih letova'))
    print('|{0:<58}|' .format('8 - Pretraga letova'))
    print('|{0:<58}|' .format('9 - Višekriterijumska pretraga letova'))
    print('|{0:<58}|' .format('10 - Prikaz 10 najjeftinijih letova (po opadajućoj ceni)'))
    print('|{0:<58}|' .format('11 - Fleksibilni polasci'))
    print('|{0:<58}|' .format('X - Odjava'))
    print('-'*60)
    return


def print_ProdavacMenu():
    print('{0:-^60}'.format('MENI ZA PRODAVCE'))
    print('|{0:<58}|'.format('1 - Prodaja karata'))
    print('|{0:<58}|'.format('2 - Prijava na let (check-in)'))
    print('|{0:<58}|'.format('3 - Izmena karte'))
    print('|{0:<58}|'.format('4 - Brisanje karte'))
    print('|{0:<58}|'.format('5 - Pretraga prodatih karata'))
    print('|{0:-^58}|'.format('OPCIJE ZA SVE KORISNIKE'))
    print('|{0:<58}|' .format('6 - Pregled nerealizovanih letova'))
    print('|{0:<58}|' .format('7 - Pretraga letova'))
    print('|{0:<58}|' .format('8 - Višekriterijumska pretraga letova'))
    print('|{0:<58}|' .format('9 - Prikaz 10 najjeftinijih letova (po opadajućoj ceni)'))
    print('|{0:<58}|' .format('10 - Fleksibilni polasci'))
    print('|{0:<58}|' .format('X - Odjava'))
    print('-'*60)


def print_AllUsersMenu():
    print('|{0:-^58}|'.format('OPCIJE ZA SVE KORISNIKE'))
    print('|{0:<58}|' .format('3 - Pregled nerealizovanih letova'))
    print('|{0:<58}|' .format('4 - Pretraga letova'))
    print('|{0:<58}|' .format('5 - Višekriterijumska pretraga letova'))
    print('|{0:<58}|' .format('6 - Prikaz 10 najjeftinijih letova (po opadajućoj ceni)'))
    print('|{0:<58}|' .format('7 - Fleksibilni polasci'))
    print('|{0:<58}|' .format('X - Izlazak iz aplikacije'))
    print('-'*60)


menu_print = {
    'main': print_MainMenu,
    'kupac': print_KupacMenu,
    'menadzer': print_MenadzerMenu,
    'prodavac': print_ProdavacMenu
}



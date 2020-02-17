import korisnici, letovi
from karte import buy_ticket, print_nerealizovane_karte, check_in_flight_menu, izmena_karte, brisanje_karte, ticket_search, delete_ticket_menu, izvestaji
from provera import provera
main_options = {
    '1': korisnici.log,                                                               #Funkcija iz korisnici.py
    '2': korisnici.reg,                                                               #...
    '3': letovi.nerealizovani,                                                        #Funkcije
    '4': letovi.pretraga,                                                             #iz
    '5': letovi.VKpretraga,                                                           #letovi.py
    '6': letovi.jeftino,                                                              #...
    '7': letovi.fleks_polazak                                                         #..
}

kupac_options = {
    '1': buy_ticket,
    '2': print_nerealizovane_karte,
    '3': check_in_flight_menu,
    '4': letovi.nerealizovani,                                                        #Funkcije
    '5': letovi.pretraga,                                                             #iz
    '6': letovi.VKpretraga,                                                           #letovi.py
    '7': letovi.jeftino,                                                              #...
    '8': letovi.fleks_polazak


}

menadzer_options = {
    '1': ticket_search,
    '2': korisnici.seller_reg,
    '3': provera,
    '4': provera,
    '5': delete_ticket_menu,
    '6': izvestaji,
    '7': letovi.nerealizovani,                                                        #Funkcije
    '8': letovi.pretraga,                                                             #iz
    '9': letovi.VKpretraga,                                                           #letovi.py
    '10': letovi.jeftino,                                                              #...
    '11': letovi.fleks_polazak




}

prodavac_options = {
    '1': buy_ticket,
    '2': check_in_flight_menu,
    '3': izmena_karte,
    '4': brisanje_karte,
    '5': ticket_search,
    '6': letovi.nerealizovani,                                                        #Funkcije
    '7': letovi.pretraga,                                                             #iz
    '8': letovi.VKpretraga,                                                           #letovi.py
    '9': letovi.jeftino,                                                              #...
    '10': letovi.fleks_polazak

}
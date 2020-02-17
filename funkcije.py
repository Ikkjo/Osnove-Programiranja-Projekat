def ucitavanje_podataka():
    global korisnici, letovi, konkretni_letovi, aerodromi, modeli
    korisnici = []
    letovi = []
    konkretni_letovi = []
    aerodromi = []
    modeli = []
    users = open('korisnici.txt', 'r', encoding='utf-8-sig')
    for user in users:
        user = user.replace('\n', '').split('|')
        if user[4] == 'kupac':
            korisnik = {'username': user[0], 'password': user[1], 'name': user[2], 'surname': user[3], 'uloga': user[4],
                        'broj pasosa': user[5], 'drzavljanstvo': user[6], 'broj telefona': user[7], 'email': user[8],
                        'pol': user[9]}
        else:
            korisnik = {'username': user[0], 'password': user[1], 'name': user[2], 'surname': user[3], 'uloga': user[4],
                        'broj pasosa': '0', 'drzavljanstvo': '0', 'broj telefona': '0', 'email': '0',
                        'pol': '0'}
        korisnici.append(korisnik)
    flights = open('avionski_letovi.txt', 'r', encoding='utf-8-sig')
    for flight in flights:
        flight = flight.replace('\n', '').split('|')
        let = {'broj leta': flight[0], 'polazisni aerodrom': flight[1], 'odredisni aerodrom': flight[2],
               'vreme poletanja': flight[3], 'vreme sletanja': flight[4], 'sledeci dan': flight[5],
               'prevoznik': flight[6], 'dani': flight[7], 'model': flight[8], 'cena': flight[9]}
        letovi.append(let)
    specific_flights = open('konkretni_letovi.txt', 'r')
    for specific_flight in specific_flights:
        specific_flight = specific_flight.replace('\n', '').split('|')
        konkretan_let = {'sifra konkretnog leta': specific_flight[0], 'broj leta': specific_flight[1],
                         'datum polaska': specific_flight[2], 'datum dolaska': specific_flight[3]}
        konkretni_letovi.append(konkretan_let)
    airports = open('aerodromi.txt', 'r')
    for airport in airports:
        airport = airport.replace('\n', '').split('|')
        aerodrom = {'kod': airport[0], 'naziv': airport[1], 'grad': airport[2], 'drzava': airport[3]}
        aerodromi.append(aerodrom)
    models = open('modeli_aviona.txt', 'r')
    for m in models:
        m = m.replace('\n', '').split('|')
        model = {'naziv': m[0], 'broj redova': m[1], 'pozicija u redu': m[2]}
        modeli.append(model)
    users.close()
    flights.close()
    specific_flights.close()
    airports.close()
    models.close()
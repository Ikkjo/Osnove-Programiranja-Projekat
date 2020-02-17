from letovi import airports_dict, flights_dict, planemodels_dict, regularflights_dict, pretraga, VKpretraga
from data_input import input_passpnum, input_gender, input_nationality
from find_userdata import users_dict, alldata_from_uname
from check_if_num import check_if_num
from domains import domain_list
from table import print_table
import datetime

flights = {}
regular_flights = {}
plane_models = {}
airports = {}

users = {}
logged_user = ''

all_tickets = []

text_red = '\033[91m'
text_green = '\033[32m'
text_end = '\033[0m'

position_in_row = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L',
                   13: 'M',
                   14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
                   25: 'Y', 26: 'Z'}

filter_params = {'1': 'start_airport',
                 '2': 'end_airport',
                 '3': 'start_date',
                 '4': 'end_date',
                 '5': 'name'}

param_names = {'start_airport': 'polazište (grad)',
               'end_airport': 'odredište (grad)',
               'start_date': 'datum polaska (dd.mm.yyyy.)',
               'datum odlaska': 'datum dolaska (dd.mm.yyyy.)',
               'name': 'ime'}


def buy_ticket():
    whos_logged_in()
    users_dict()
    airports_dict()
    flights_dict()
    planemodels_dict()
    regularflights_dict()
    load_avionskekarte()

    user = alldata_from_uname(whos_logged_in())
    prodavac = False
    if user['uloga'] == 'prodavac':
        prodavac = True

    while True:

        unos = input(
            'Unesite 1 za unos broja leta (četvorocifreni broj), P za pretragu ili X za povratak na prethodni meni\n>>')
        if unos == '1':
            flight = input('Unesite broj leta (četvorocifreni broj): ')
            flight, error = ticket_whole_check(flight)

            if error:
                break

            ticket_num = new_ticket_number()

            ticket = get_data_for_ticket(flight, ticket_num, saputnik=False, prodavac=prodavac)
            izbor = {'da': True,
                     'DA': True,
                     'Da': True,
                     'dA': True,
                     'ne': False,
                     'NE': False,
                     'Ne': False,
                     'nE': False}
            potvrda = input('Da li potvrđujete kupovinu karte?(DA/NE)\n>>')
            while potvrda not in izbor:
                potvrda = input('Da li potvrđujete kupovinu karte?(>DA/NE<)\n>>')
            if izbor[potvrda] is True:
                upis_karte(ticket)
                input(
                    text_green + 'Uspešno ste kupili kartu za let ' + flight + '!\nPritisnite ENTER za nastavak...' + text_end)

                potvrda = input('Da li želite da kupite kartu i za saputnika?(DA/NE)\n>>')
                while potvrda not in izbor:
                    potvrda = input('Da li želite da kupite kartu i za saputnika?(>DA/NE<)\n>>')
                if izbor[potvrda] is True:
                    if check_if_full(flight) is True:
                        input(text_red + 'Nažalost, ovaj let je pun. Pritisnite ENTER za nastavak.' + text_end)
                        break
                    ticket_num = new_ticket_number()
                    ticket = get_data_for_ticket(flight, ticket_num, saputnik=True, prodavac=False)
                    potvrda = input('Da li potvrđujete kupovinu karte?(DA/NE)\n>>')
                    while potvrda not in izbor:
                        potvrda = input('Da li potvrđujete kupovinu karte?(>DA/NE<)\n>>')
                    if izbor[potvrda] is True:
                        upis_karte(ticket)
                        input(
                            text_green + 'Uspešno ste kupili saputniku kartu za let ' + flight + '!\nPritisnite '
                                                                                                        'ENTER za '
                                                                                                        'nastavak...' +
                            text_end)


        elif unos == 'p' or unos == 'P':
            while True:
                search = input('Pritisnite 1 za pretragu letova ili 2 za višekriterijumsku pretragu letova\n>>')
                if search == '1':
                    pretraga()

                elif search == '2':
                    VKpretraga()

                else:
                    print(text_red + 'Opcija nije validna' + text_end)
                break

        elif unos == 'x' or unos == 'X':
            break

        else:
            print(text_red + 'Uneli ste nepostojeću opciju.\nPokušajte ponovo.' + text_end)



def print_nerealizovane_karte(izmena=False, brisanje=False):
    load_avionskekarte()
    buyer = whos_logged_in()
    user_tickets = []
    if not izmena and not brisanje:
        for ticket in all_tickets:
            if ((ticket['buyer'] == buyer or ticket['seller'] == buyer)
                    and ticket['active']
                    and ticket['seat'] == ''):
                user_tickets.append(ticket)

    elif izmena:
        for ticket in all_tickets:
            if ((ticket['buyer'] == buyer or ticket['seller'] == buyer)
                    and ticket['active']):
                user_tickets.append(ticket)

    elif brisanje:
        for ticket in all_tickets:
            if ticket['active'] is False:
                user_tickets.append(ticket)


    if len(user_tickets) == 0 and not brisanje:
        input(text_red + 'Nemate kupljenih karata!\n'
                         'Pritisnite ENTER za nastavak...' + text_end)

    elif len(user_tickets) == 0 and brisanje:
        input(text_red + 'Nema karata koje su označene za brisanje!\n'
                         'Pritisnite ENTER za nastavak...' + text_end)
    else:
        ticket_table(user_tickets)


def ticket_table(ticket_list):
    airports = airports_dict()
    flights = flights_dict()
    regularf = regularflights_dict()
    ticket_print = []

    for ticket in ticket_list:
        kflight_num = ticket['flight_num']
        reg_flnum = flights[kflight_num]['flight_num']
        depart_date = flights[kflight_num]['start_date']
        arrival_date = flights[kflight_num]['end_date']
        depart_time = regularf[reg_flnum]['start_time']
        arrival_time = regularf[reg_flnum]['end_time']
        depart_airpnum = regularf[reg_flnum]['start_airport']
        arrival_airpnum = regularf[reg_flnum]['end_airport']
        depart_airport = airports[depart_airpnum]['name']
        depart_city = airports[depart_airpnum]['city']
        depart_country = airports[depart_airpnum]['country']
        arrival_airport = airports[arrival_airpnum]['name']
        arrival_city = airports[arrival_airpnum]['city']
        arrival_country = airports[arrival_airpnum]['country']

        departure_dt = depart_date + ' ' + depart_time
        departure_cc = depart_city + ', ' + depart_country
        arrival_dt = arrival_date + ' ' + arrival_time
        arrival_cc = arrival_city + ', ' + arrival_country

        departure = 'Departure:\n' + depart_airport + '\n' + departure_cc + '\n' + departure_dt
        arrival = 'Arrival:\n' + arrival_airport + '\n' + arrival_cc + '\n' + arrival_dt

        current_ticket = ['Broj karte:\n' + ticket['ticket_num'], 'Broj leta:\n' + kflight_num,
                          'Putnik: \n' + ticket['name'] + '\n' + ticket['surname'], departure, arrival,
                          'Povezan let:\n' + ticket['connected_flight'], 'Sedište: ' + ticket['seat']]

        ticket_print.append(current_ticket)

    print_table(ticket_print)


def check_in_flight_menu():
    izbor = {'1': check_in_flight,
             '2': print_nerealizovane_karte}
    while True:
        odgovor = input(
            'Unesite 1 za prijavu na let (check-in), 2 da pogledate vaše karte ili X za povratakna prthodni meni.\n>>')

        if odgovor in izbor:
            if odgovor == '2':
                izbor[odgovor]()
            else:
                izbor[odgovor]()
                break
        if odgovor == 'X' or odgovor == 'x':
            break


def check_in_flight():
    global all_tickets
    global position_in_row
    load_avionskekarte()
    user = whos_logged_in()
    while True:
        ticket_num = input('Unesite broj karte koju želite da prijavite: ')
        while ticket_num == '':
            input(text_red + 'Greška, polje ne sme biti prazno.' + text_end + '\nPritisnite ENTER za nastavak...')

        if check_if_ticket_valid(user, ticket_num) is False:
            break

        if check_if_flightdate_valid(ticket_num) is False:
            input(
                text_red + 'Možete obaviti prijavu na let samo \033[4m48h (2 dana)' + text_end + text_red + ' pre polaska\n'
                                                                                                            'Pritisnite ENTER za nastavak...' + text_end)
            break

        for ticket in all_tickets:
            if ticket_num == ticket['ticket_num']:
                flight_num = ticket['flight_num']

        taken_seats, rows, columns = print_available_seats(flight_num)

        while True:

            seat = input('Unesite koje mesto želite (1-' + str(rows) + ', A-' + position_in_row[columns] + '): ')
            if len(seat) == 0:
                print(text_red + 'Greška, polje ne sme biti prazno!')
                break

            if len(taken_seats) != 0:
                found = False
                for taken_seat in taken_seats:
                    if taken_seat == seat:
                        found = True

                if found == True:
                    print(text_red + 'Ovo mesto je zauzeto!' + text_end)
                    break
                try:
                    if type(eval(seat[:-1])) is not int:
                        print(text_red + 'Niste uneli ispravno!' + text_end)
                        break
                except NameError:
                    print(text_red + 'Niste uneli ispravno!' + text_end)
                    break

                if int(seat[:-1]) > rows:
                    print(text_red + 'Niste uneli ispravno!' + text_end)
                    break

                try:

                    int(seat[-1])
                    print(text_red + 'Niste uneli ispravno!' + text_end)
                    break

                except ValueError:
                    pass


            for ticket in all_tickets:
                if ticket['ticket_num'] == ticket_num:
                    ticket['seat'] = seat
            upisi_karte()
            input(text_green + 'Uspešno ste se prijavili na let ' + flight_num + ' na mesto ' + seat + '!\n'
                                                                                                       'Pritisnite ENTER da nastavite...' + text_end)
            return


def upisi_karte():
    global all_tickets
    upis = ''
    file = open('avionske_karte.txt', 'w', encoding='utf-8')
    for ticket in range(len(all_tickets)):
        if ticket != (len(all_tickets) - 1):
            tic_str = str(all_tickets[ticket]) + '\n'
        else:
            tic_str = str(all_tickets[-1])
        file.write(tic_str)
    file.close()


def check_if_ticket_valid(user, ticket_num):
    global all_tickets
    found = False
    tickID = 0
    try:
        while found == False:
            ticket = all_tickets[tickID]

            found = ((ticket['buyer'] == user or ticket['seller'] == user) and
                     (ticket['ticket_num'] == ticket_num) and ticket['active'])
            tickID += 1

        if found is False:
            input(text_red + 'Niste kupili ovu kartu ili je ta karta deaktivirana\n'
                             'Pritisnite ENTER za nastavak...' + text_end)
            return False
        else:
            return True
    except IndexError:
        input(text_red + 'Karta ' + ticket_num + 'ne postoji!\n'
                                                 'Pritisnite ENTER za nastavak...' + text_end)
        return False


def check_if_flightdate_valid(ticket_num):
    global all_tickets
    flights = flights_dict()

    for ticket in all_tickets:
        if ticket['ticket_num'] == ticket_num:
            flight_num = ticket['flight_num']
            break

    start_date = flights[flight_num]['start_date']
    start_date = start_date.split('.')
    day = int(start_date[0])
    month = int(start_date[1])
    year = int(start_date[2])
    depart_date = datetime.date(year, month, day)

    today = datetime.date.today()

    datedelta = depart_date - today

    valid_delta = datetime.timedelta(2)

    if today > depart_date:
        print(text_red + 'Žao nam je, ovaj let je prošao.' + text_end)
        return False

    if datedelta <= valid_delta:
        return True
    else:
        return False


def print_available_seats(flight_num):
    global all_tickets

    flights = flights_dict()
    reg_flights = regularflights_dict()
    plane_models = planemodels_dict()

    regflight_num = flights[flight_num]['flight_num']

    p_model = reg_flights[regflight_num]['plane_model']

    rows = eval(plane_models[p_model]['rows'])

    pos = plane_models[p_model]['position_in_row'].split(' ')
    columns = len(pos)
    seats = []
    for ticket in all_tickets:
        if ticket['flight_num'] == flight_num and ticket['seat'] != '':
            seats.append(ticket['seat'])
    taken_seats = []
    if len(seats) == 0:
        taken_seats = []
    else:
        for seat in seats:
            pos_in_row = seat[-1]
            row = seat[:-1]
            seat = [row, pos_in_row]
            taken_seats.append(seat)

    print_plane_matrix(taken_seats, rows, columns)
    return taken_seats, rows, columns


def print_plane_matrix(taken_seats, rows, columns):
    for row in range(1, rows + 1):
        print('{0:>2}{1}'.format(str(row), '. red: '), end='')
        for position in range(1, columns + 1):
            if position == columns:
                print(check_if_seat_taken(row, position, taken_seats), end='\n')
            else:
                print(check_if_seat_taken(row, position, taken_seats), end=' ')


def check_if_seat_taken(row, position, taken_seats):
    global position_in_row

    found = False
    seat = 0

    while not found:
        try:
            if position_in_row[position] == taken_seats[seat][1] and row == int(taken_seats[seat][0]):
                found = True
                print_pos = text_red + 'X' + text_end
                seat += 1
            else:
                found = False
                print_pos = text_green + position_in_row[position] + text_end
                seat += 1
        except IndexError:
            found = True
            print_pos = text_green + position_in_row[position] + text_end

    return print_pos


def load_avionskekarte():
    global all_tickets
    all_tickets = []
    file = open('avionske_karte.txt', 'r', encoding='utf-8')
    ceo_fajl = file.read()
    ticketlist = ceo_fajl.split('\n')
    try:
        for dictionary in ticketlist:
            ticket_dict = eval(dictionary)
            all_tickets.append(ticket_dict)

    except SyntaxError:
        all_tickets = []


def new_ticket_number():
    file = open('avionske_karte.txt', 'r', encoding='utf-8')
    list = file.readlines()
    file.close()
    ticket_num = str(len(list) + 1)

    return ticket_num


def check_if_full(currentflight_num):
    whos_logged_in()
    users_dict()
    airports_dict()
    flights = flights_dict()
    plane_models = planemodels_dict()
    regular_flights = regularflights_dict()
    load_avionskekarte()

    seats_taken = 0
    for ticket in all_tickets:
        if ticket['active']:
            if ticket['flight_num'] == currentflight_num:
                seats_taken += 1

    regular = flights[currentflight_num]['flight_num']

    model = regular_flights[regular]['plane_model']

    rows = eval(plane_models[model]['rows'])

    pos = plane_models[model]['position_in_row'].split(' ')
    position = len(pos)

    max_seats = rows * position

    if seats_taken < max_seats:
        return False
    else:
        return True


def whos_logged_in():
    file = open('current_user.txt', 'r', encoding='utf-8')
    user = file.read()
    file.close()

    global logged_user

    logged_user = user

    return user


def get_data_for_ticket(flight, ticket_num, saputnik, prodavac):
    today = datetime.date.today()
    buyer = whos_logged_in()
    seller = ''
    user = alldata_from_uname(whos_logged_in())
    if user['uloga'] == 'prodavac':
        seller = user['u_name']
        prodavac = True

    izbor = {'da': True,
             'DA': True,
             'Da': True,
             'dA': True,
             'ne': False,
             'NE': False,
             'Ne': False,
             'nE': False, }
    if saputnik is False and prodavac is False:
        za_sebe = input('Da li kupujete kartu za sebe?\n>>')
        while za_sebe not in izbor:
            za_sebe = input('Da li kupujete kartu za sebe?\n(Unesite DA ili NE)\n>>')
        if izbor[za_sebe] is True:
            user = alldata_from_uname(buyer)
        else:
            user = podaci_za_drugo_lice()

    if saputnik is True:
        user = podaci_za_drugo_lice()

    if prodavac is True and saputnik is False:
        registrovan_kor = da_li_je_reg()
        if len(registrovan_kor) != 0:
            buyer = registrovan_kor
            user = alldata_from_uname(buyer)
        else:
            user = podaci_za_drugo_lice()

    try:
        ticket = {'ticket_num': ticket_num,
                  'flight_num': flight,
                  'buyer': buyer,
                  'name': user['name'],
                  'surname': user['surname'],
                  'mail': user['mail'],
                  'phone_num': user['phone_num'],
                  'passp_num': user['passp_num'],
                  'nationality': user['nationality'],
                  'gender': user['gender'],
                  'seat': '',
                  'seller': seller,
                  'connected_flight': '',
                  'active': True,
                  'date_sold': today}

    except KeyError:
        input('Morate uneti dodatne podatke. Pritisnite ENTER za nastavak.')
        nationality = input_nationality()
        gender = input_gender()
        passp_num = input_passpnum()

        ticket = {'ticket_num': ticket_num,
                  'flight_num': flight,
                  'buyer': buyer,
                  'name': user['name'],
                  'surname': user['surname'],
                  'mail': user['mail'],
                  'phone_num': user['phone_num'],
                  'passp_num': passp_num,
                  'nationality': nationality,
                  'gender': gender,
                  'seat': '',
                  'seller': seller,
                  'connected_flight': '',
                  'active': True,
                  'date_sold': today}

    return ticket


def check_flightnum(flightnum):
    allflights = flights_dict()
    if flightnum not in allflights:
        return False
    else:
        return True


def ticket_whole_check(flight):
    check = 0
    error = True
    while check != 3:

        while len(flight) != 4 and check_if_num(flight) is False:
            flight = input('Unesite broj leta (>ČETVOROCIFRENI BROJ<): ')
        check += 1

        if check_flightnum(flight) is False:
            input(text_red + 'Greška, ovaj let ne postoji. Pritisnite ENTER za nastavak.' + text_end)
            error = True
            break
        check += 1
        try:
            if check_if_full(flight) is True:
                input(text_red + 'Nažalost, ovaj let je pun. Pritisnite ENTER za nastavak.' + text_end)
                error = True
                break
            else:
                check += 1
                error = False
        except KeyError:
            check += 1
            error = False

    return flight, error


def podaci_za_drugo_lice():
    ime = input('Unesite ime putnika: ')
    while len(ime) == 0:
        print(text_red + 'Greška, polje ne sme biti prazno' + text_end)
        ime = input('Unesite ime putnika: ')

    prezime = input('Unesite prezime putnika: ')
    while len(prezime) == 0:
        print(text_red + 'Greška, polje ne sme biti prazno' + text_end)
    tel = input('Unesite broj kontakt telefona putnika: ')

    while check_term('phone_num', tel):
        print(text_red + 'Greška, već postoji korisnik sa tim brojem telefona.\nPokušajte ponovo: ' + text_end)
    tel = provera_tel(tel)
    e_mail = input('Unesite e-mail adresu putnika: ')
    while check_term('mail', e_mail) is True:
        print(text_red + 'Greška, već postoji korisnik sa tom e-mail adresom.\nPokušajte ponovo: ' + text_end)
        e_mail = input('Unesite e-mail adresu putnika: ')
    chkmail = provera_email(e_mail)

    br_pasosa = input_passpnum()

    drzavljanstvo = input_nationality()

    pol = input_gender()

    drugo_lice = {'name': ime,
                  'surname': prezime,
                  'mail': chkmail,
                  'phone_num': tel,
                  'passp_num': br_pasosa,
                  'nationality': drzavljanstvo,
                  'gender': pol}

    return drugo_lice


def check_term(term, u_input):
    user_dict = users_dict()
    found = False
    for index in range(len(user_dict)):
        ind = str(index)
        current_user = 'user' + ind
        try:
            if u_input == user_dict[current_user][term]:
                found = True

        except KeyError:
            continue

    return found


def provera_email(e_mail):
    check = False
    while check is False:
        e_mail = e_mail.split('@')

        while len(e_mail) != 2:  # odvaja se ime i domen maila, provera da li dobijena lista ima 2 clana
            e_mail = input(text_red + 'Format mail-a nije dobar, verovatno fali "@"?' + text_end +
                           '\nUnesite e-mail adresu putnika: ')
            e_mail = e_mail.split('@')

        try:  # kad se unese jedno slovo izbaci IndexError
            while e_mail[0] == '' or e_mail[1] == '':
                e_mail = input(
                    text_red + 'Format mail-a nije dobar, fali nešto pre ili posle "@"?' + text_end +
                    '\nUnesite e-mail adresu putnika: ')
                e_mail = e_mail.split('@')

        except IndexError:
            e_mail = input(
                text_red + 'Oblik mail-a mora biti ' + text_end + 'ime@domen\nUnesite e-mail adresu putnika: ')

        domain = e_mail[1]

        domain_check = False  # za proveru domena koristim fajl domains.py u kome se nalazi lista najcesce koriscenih>
        if domain_check is False:  # >email domena
            for item in range(len(domain_list)):
                if domain == domain_list[item]:
                    domain_check = True

        if domain_check is True:
            check = True
        else:
            e_mail = input(
                text_red + 'Format mail-a nije dobar, domen nije odgovarajući?' + text_end +
                '\nUnesite e-mail adresu putnika: ')

    mail = e_mail[0] + '@' + e_mail[1]  # spajam nazad ime i domen
    return mail


def provera_tel(tel):
    while True:
        try:
            int(tel)
            break

        except ValueError:
            tel = input(text_red + 'Greška, niste ispravno uneli broj telefona' + text_end +
                        '\nUnesite broj kontakt telefona putnika: ')

    return tel


def da_li_je_reg():
    izbor = {'da': True,
             'DA': True,
             'Da': True,
             'dA': True,
             'ne': False,
             'NE': False,
             'Ne': False,
             'nE': False, }

    while True:
        unos = input('Da li je korisnik registrovan?(DA/NE)\n>>')
        while len(unos) != 0 and (unos not in izbor):
            unos = input('Da li je korisnik registrovan?(>DA/NE<)\n>>')

        if izbor[unos] is True:
            kor_ime = input('Unesite korisničko ime korisnika: ')
            if len(unos) != 0 and not check_for_user(kor_ime):
                print(text_red + 'Korisnik ne postoji!' + text_end)

            else:
                return kor_ime

        else:
            return ''


def check_for_user(uname):
    users = users_dict()
    found = False
    for user in range(len(users)):
        userID = 'user' + str(user)
        curr_user = users[userID]
        if curr_user['u_name'] == uname:
            return True

    return False


def upis_karte(ticket):
    upis = "\n" + str(ticket)

    file = open('avionske_karte.txt', 'a', encoding='utf-8')
    file.write(upis)
    file.close()


def izmena_karte():
    while True:
        unos = input('Pritisnite 1 da izmenite kartu, 2 da vidite prodate karte ili X za povratak.\n>>')
        while len(unos) == 0:
            unos = input('Pritisnite 1 da izmenite kartu, 2 da vidite prodate karte ili X za povratak.\n>>')

        if unos == '1':
            edit_ticket()
            break

        elif unos == '2':
            print_nerealizovane_karte(izmena=True)

        elif unos == 'X' or unos == 'x':
            return

        else:
            print(text_red + 'Izabrali ste nepostojeću opciju')

def brisanje_karte():
    while True:
        unos = input('Pritisnite 1 da obrišete kartu, 2 da vidite prodate karte ili X za povratak.\n>>')
        while len(unos) == 0:
            unos = input('Pritisnite 1 da obrišete kartu, 2 da vidite prodate karte ili X za povratak.\n>>')

        if unos == '1':
            un_active_ticket()

        elif unos == '2':
            print_nerealizovane_karte(izmena=True)

        elif unos == 'X' or unos == 'x':
            return

        else:
            print(text_red + 'Izabrali ste nepostojeću opciju')


def edit_ticket():

    user = whos_logged_in()
    izbor = {'da': True,
             'DA': True,
             'Da': True,
             'dA': True,
             'ne': False,
             'NE': False,
             'Ne': False,
             'nE': False}

    izmena = {'1': 'flight_num',
              '2': 'flight_num',
              '3': 'seat'}

    load_avionskekarte()
    global all_tickets

    tick_num = input('Unesite broj karte za izmenu: ')

    for ticket in all_tickets:
        if ticket['ticket_num'] == tick_num and (ticket['buyer'] == user or ticket['seller'] == user):
            unos = input('Šta želite izmeniti?\n'
                         '1 - Promena leta\n'
                         '2 - Promena datuma leta\n'
                         '3 - Promena sedišta\n'
                         '>>')
            while unos not in izmena:
                unos = input('>>')
            if unos == '1':
                while True:
                    let = input('Unesite novi broj leta ili p za pretragu: ')
                    if let == 'p' or let == 'P':
                        pretraga()

                    else:
                        flight, error = ticket_whole_check(let)
                        if error:
                            return
                        else:
                            ticket['flight_num'] = let
                            upisi_karte()
                            break

                input(text_green + 'Promenili ste let za karti br. ' + str(ticket['ticket_num']) + '\n'
                                   'Pritisnite ENTER za nastavak...' + text_end)
                return

            elif unos == '2':
                while True:
                    let = input('Unesite novi broj leta ili p za pretragu: ')
                    if let == 'p' or let == 'P':
                        pretraga()

                    else:
                        flight, error = ticket_whole_check(let)
                        if error:
                            return
                        else:
                            ticket['flight_num'] = let
                            upisi_karte()
                            break

                input(text_green + 'Promenili ste let za karti br. ' + str(ticket['ticket_num']) + '\n'
                                   'Pritisnite ENTER za nastavak...' + text_end)
                return
            elif unos == '3':
                while True:
                    taken_seats, rows, columns = print_available_seats(ticket['flight_num'])
                    seat = input(
                        'Unesite koje mesto želite (1-' + str(rows) + ', A-' + position_in_row[columns] + '): ')
                    if len(seat) == 0:
                        print(text_red + 'Greška, polje ne sme biti prazno!')
                        break

                    if len(taken_seats) != 0:
                        found = False
                        for taken_seat in taken_seats:
                            if taken_seat == seat:
                                found = True

                        if found == True:
                            print(text_red + 'Ovo mesto je zauzeto!' + text_end)
                            return
                        try:
                            if type(eval(seat[:-1])) is not int:
                                print(text_red + 'Niste uneli ispravno!' + text_end)
                                return
                        except NameError:
                            print(text_red + 'Niste uneli ispravno!' + text_end)
                            return

                        if int(seat[:-1]) > rows:
                            print(text_red + 'Niste uneli ispravno!' + text_end)
                            return

                        try:

                            int(seat[-1])
                            print(text_red + 'Niste uneli ispravno!' + text_end)
                            return

                        except ValueError:
                            0 + 0

                        ticket['seat'] = seat
                        break
                upisi_karte()
                input(text_green + 'Promenili ste sedište karti br. ' + str(ticket['ticket_num']) + '\n'
                                   'Pritisnite ENTER za nastavak...' + text_end)
                return

            else:
                return print(text_red + 'Greška' + text_end)


    return print(text_red + 'Niste prodali ovu kartu!' + text_end)


def un_active_ticket():
    user = whos_logged_in()
    izbor = {'da': True,
             'DA': True,
             'Da': True,
             'dA': True,
             'ne': False,
             'NE': False,
             'Ne': False,
             'nE': False}


    load_avionskekarte()
    global all_tickets

    tick_num = input('Unesite broj karte za brisanje: ')

    for ticket in all_tickets:
        if ticket['ticket_num'] == tick_num and (ticket['buyer'] == user or ticket['seller'] == user):
            unos = input('Da li ste sigurni?(DA/NE)\n>>')
            while unos not in izbor:
                unos = input('Da li ste sigurni?(>DA/NE<)\n>>')
            if izbor[unos] is True:
                ticket['active'] = False
                upisi_karte()
                input(text_green + 'Označili ste kartu br. ' + str(ticket['ticket_num']) + ' za brisanje!\n'
                                   'Pritisnite ENTER za nastavak...' + text_end)
                return

            else:
                return

    return print(text_red + 'Niste prodali ovu kartu!' + text_end)


def delete_ticket_menu():

    while True:
        unos = input('Pritisnite 1 da obrišete kartu, 2 da vidite karte označene za brisanje ili X za povratak.\n>>')
        while len(unos) == 0:
            unos = input('Pritisnite 1 da obrišete kartu, 2 da vidite karte označene za brisanje ili X za povratak.\n>>')

        if unos == '1':
            found = False
            while True:
                tick_num = input('Unesite broj karte koju želite obrisati: ')
                for ticket in all_tickets:
                    if ticket['ticket_num'] == tick_num and ticket['active'] == False:
                        delete_ticket(tick_num)
                        upisi_karte()
                        return input(text_green + 'Obrisali ste kartu br. ' + tick_num + '!\n'
                                                  'Pritisnite ENTER za nastavak...' + text_end)

                return print(text_red + 'Nema karte označene za brisanje (ili niste uneli dobar broj karte)!' + text_end)



        elif unos == '2':
            print_nerealizovane_karte(brisanje=True)

        elif unos == 'X' or unos == 'x':
            return

        else:
            print(text_red + 'Izabrali ste nepostojeću opciju' + text_end)


def delete_ticket(ticket_number):
    load_avionskekarte()
    global all_tickets

    for ticket in all_tickets:
        if ticket['ticket_num'] == ticket_number and ticket['active'] == False:
            all_tickets.remove(ticket)
            return




def ticket_search():
    izbor = {'da': True,
             'DA': True,
             'Da': True,
             'dA': True,
             'ne': False,
             'NE': False,
             'Ne': False,
             'nE': False}

    global filter_params
    global param_names
    print('1 - Polazište\n'
          '2 - Odredište\n'
          '3 - Datum polaska\n'
          '4 - Datum dolaska\n'
          '5 - Putnik')
    while True:
        param = input('Unesite broj za odgovarajući kriterijum pretrage: ')
        if param not in filter_params:
            print(text_red + 'Odabrali ste nepostojeću opciju!' + text_end)
            return

        filter = input('Izaberite ' + param_names[filter_params[param]] + ': ')
        while filter is False:
            print(text_red + 'Polje ne sme biti prazno!' + text_end)
            filter = input('Izaberite ' + param_names[filter_params[param]] + ': ')



def izvestaji():
    users = users_dict()
    izvestaj = {'1': list_datesold,
                '2': list_departdate,
                '3': list_datesold_seller,
                '4': amount_datesold,
                '5': amount_departdate,
                '6': amount_datesold_seller,
                '7': amount_30days}

    print('1 - Lista prodatih karata za izabrani dan prodaje \n'
          '2 - Lista prodatih karata za izabrani dan polaska\n'
          '3 - Lista prodatih karata za izabrani dan prodaje i izabranog prodavca\n'
          '4 - Ukupan broj i cena prodatih karata za izabrani dan prodaje\n'
          '5 - Ukupan broj i cena prodatih karata za izabrani dan polaska\n'
          '6 - Ukupan broj i cena prodatih karata za izabrani dan prodaje i izabranog prodavca\n'
          '7 - Ukupan broj i cena prodatih karata u poslednjih 30 dana, po prodavcima.\n'
          'X - Povratak')

    izbor = input('Izaberite broj opcije: ')
    if izbor == 'X' or izbor == 'x':
        return
    while izbor not in izvestaj:
        izbor = input('Izaberite broj opcije: ')
        if izbor == 'X' or izbor == 'x':
            return

    if izbor != '7' and izbor != '3' and izbor != '6':
        date = input('Unesite datum (dd.mm.yyyy.): ')
        dt = date.split('.')
        day = dt[0]
        month = dt[1]
        year = dt[2]
        while len(dt) != 4 or len(day) != 2 or len(month) != 2 or len(year) != 4:
            print(text_red + 'Pogrešno ste uneli datum!' + text_end)
            date = input('Unesite datum (dd.mm.yyyy.): ')

        izvestaj[izbor](date)
        return

    elif izbor !='7':
        date = input('Unesite datum (dd.mm.yyyy.): ')
        dt = date.split('.')
        day = dt[0]
        month = dt[1]
        year = dt[2]
        while len(dt) != 4 or len(day) != 2 or len(month) != 2 or len(year) != 4:
            print(text_red + 'Pogrešno ste uneli datum!' + text_end)
            date = input('Unesite datum (dd.mm.yyyy.): ')
        while True:

            seller = input('Unesite korisnicko ime prodavca: ')
            found = False
            for id in range(len(users)):
                userid = 'user' + str(id)
                if seller == users[userid]['u_name'] and users[userid]['uloga'] == 'prodavac':
                    found = True

            if not found:
                return print(text_red + 'Taj kupac ne postoji!'+ text_end)
            break

        izvestaj[izbor](date, seller)
        return



    else:
        izvestaj[izbor]()
        return





def list_datesold(date):

    load_avionskekarte()
    global all_tickets
    ticket_list = []

    dt = date.split('.')
    day = int(dt[0])
    month = int(dt[1])
    year = int(dt[2])

    date = datetime.date(year, month, day)

    for ticket in all_tickets:
        if ticket['date_sold'] == date and ticket['active']:
            ticket_list.append(ticket)


    if len(ticket_list) == 0:
        input(text_red + 'Nema takvih karata!\n'
                         'Pritisnite ENTER za nastavak...' + text_end)

    else:
        ticket_table(ticket_list)
        input('Pritisnite ENTER za nastavak...')


def list_departdate(date):

    load_avionskekarte()
    fl = flights_dict()

    global all_tickets
    ticket_list = []

    for ticket in all_tickets:
        depart_date = fl[ticket['flight_num']]['start_date']
        if depart_date == date and ticket['active']:
            ticket_list.append(ticket)


    if len(ticket_list) == 0:
        input(text_red + 'Nema takvih karata!\n'
                         'Pritisnite ENTER za nastavak...' + text_end)

    else:
        ticket_table(ticket_list)
        input('Pritisnite ENTER za nastavak...')




    return


def list_datesold_seller(date, seller):
    load_avionskekarte()
    global all_tickets
    ticket_list = []

    dt = date.split('.')
    day = int(dt[0])
    month = int(dt[1])
    year = int(dt[2])

    date = datetime.date(year, month, day)

    for ticket in all_tickets:
        if ticket['date_sold'] == date and ticket['active'] == True and ticket['seller'] == seller:
            ticket_list.append(ticket)


    if len(ticket_list) == 0:
        input(text_red + 'Nema takvih karata!\n'
                         'Pritisnite ENTER za nastavak...' + text_end)

    else:
        ticket_table(ticket_list)
        input('Pritisnite ENTER za nastavak...')
    return


def amount_datesold(date):
    reg_fl = regularflights_dict()
    fl = flights_dict()
    load_avionskekarte()
    global all_tickets
    number_sold = 0
    sum = 0

    dt = date.split('.')
    day = int(dt[0])
    month = int(dt[1])
    year = int(dt[2])

    d = datetime.date(year, month, day)

    for ticket in all_tickets:
        if ticket['date_sold'] == d:
            number_sold += 1
            tick_price = int(reg_fl[fl[ticket['flight_num']]['flight_num']]['ticket_price'])
            sum = sum + tick_price

    if number_sold == 0:
        print(text_red + 'Za odabrani datum nije bilo prodaja.' + text_end)

    else:
        print(date +' je prodato ' + text_green+ str(number_sold)+ text_end + ' karata.\n'
          'Ukupna suma je ' + str(sum) + ' €.')
    return


def amount_departdate(date):
    reg_fl = regularflights_dict()
    fl = flights_dict()
    load_avionskekarte()
    global all_tickets
    number_sold = 0
    sum = 0

    for ticket in all_tickets:
        depart_date = fl[ticket['flight_num']]['start_date']
        if depart_date == date:
            number_sold += 1
            tick_price = int(reg_fl[fl[ticket['flight_num']]['flight_num']]['ticket_price'])
            sum = sum + tick_price

    if number_sold == 0:
        print(text_red + 'Za odabrani datum nije bilo prodaja.' + text_end)

    print('Za letove koji poleću ' + date +' je prodato ' + text_green + str(number_sold)+ text_end + ' karata.\n'
          'Ukupna suma je ' + str(sum) + ' €.')
    return


def amount_datesold_seller(date, seller):
    user = alldata_from_uname(seller)
    reg_fl = regularflights_dict()
    fl = flights_dict()
    load_avionskekarte()
    global all_tickets
    number_sold = 0
    sum = 0

    dt = date.split('.')
    day = int(dt[0])
    month = int(dt[1])
    year = int(dt[2])

    d = datetime.date(year, month, day)

    for ticket in all_tickets:
        if ticket['date_sold'] == d and seller == ticket['seller']:
            number_sold += 1
            tick_price = int(reg_fl[fl[ticket['flight_num']]['flight_num']]['ticket_price'])
            sum = sum + tick_price

    if number_sold == 0:
        print(text_red + user['name'] + ' ' + user['surname'] + ' za odabrani datum nije imao prodaja.' + text_end)

    else:
        print(user['name'] + ' ' + user['surname'] +' je ' + date + ' prodao ' + text_green+ str(number_sold)+ text_end + ' karata.\n'
          'Ukupna suma je ' + str(sum) + ' €.')

    return


def amount_30days():
   # user_dict = alldata_from_uname(seller)
    users = users_dict()
    reg_fl = regularflights_dict()
    fl = flights_dict()
    load_avionskekarte()
    global all_tickets

    today = datetime.date.today()
    delta = datetime.timedelta(30)
    past30 = today - delta
    table = [['Prodavac:','Broj i suma prodatih karata:']]

    for user in range(len(users)):
        u_id = 'user' + str(user)
        user = users[u_id]['u_name']
        user_dict = alldata_from_uname(user)
        sum = 0
        number_sold = 0
        if user_dict['uloga'] == 'prodavac':
            for ticket in all_tickets:
                if (past30 <= ticket['date_sold'] and ticket['date_sold'] <= today) and (user_dict['u_name'] == ticket['seller']):
                    number_sold += 1
                    tick_price = int(reg_fl[fl[ticket['flight_num']]['flight_num']]['ticket_price'])
                    sum = sum + tick_price

            row = [user_dict['name'] + ' ' + user_dict['surname'],
                   'Br. prodaja: ' + str(number_sold) + '\nSuma: ' + str(sum) + ' €']
            table.append(row)

    print_table(table)

    return

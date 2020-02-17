from provera import provera
from file_list import file_list
import datetime
from table import print_table

text_red = '\033[91m'
text_green = '\033[32m'
text_end = '\033[0m'

flights = {}
regular_flights = {}
plane_models = {}
airports = {}


def nerealizovani(filter='', param='', vk=False, flight_list=None, fin_print=False):
    if flight_list is None:
        flight_list = []
    table = []

    flights_dict()
    regularflights_dict()
    airports_dict()

    for flight in range(len(flights) + 1):
        if flight != 0:
            konkretanfID = '{0:0>4}'.format(str(flight))
            start_date = flights[konkretanfID]['start_date']

            flightnum = flights[konkretanfID]['flight_num']

            end_date = flights[konkretanfID]['end_date']

            current_flight_data = flight_data(flightnum)

            start_airport = current_flight_data['start_airport']
            start_airport = airport_data(start_airport)
            depart_country_city = start_airport['city'] + ', ' + start_airport['country']

            end_airport = current_flight_data['end_airport']
            end_airport = airport_data(end_airport)
            arrival_country_city = end_airport['city'] + ', ' + end_airport['country']

            start_time = current_flight_data['start_time']
            end_time = current_flight_data['end_time']

            price = current_flight_data['ticket_price'] + ' €'

            carrier = current_flight_data['carrier']

            startdt = start_date + ', ' + start_time
            enddt = end_date + ', ' + end_time
            flduration = duration(startdt, enddt)
            column1text = 'Polazak:\n' + startdt + '\n' + depart_country_city
            column3text = 'Dolazak:\n' + enddt + '\n' + arrival_country_city
            column0 = 'Broj leta:\n' + str(konkretanfID)
            column1 = '{:^20}'.format(column1text)
            column2 = '{:^20}'.format(
                'Vreme letenja: ' + str(flduration) + '\nCena: ' + price + '\nPrevoznik: ' + carrier)
            column3 = '{:^20}'.format(column3text)

            today = datetime.datetime.today()
            depart_date = convert_datetime(startdt)

            if filter is False and param is False:
                row = [column1, column2, column3]
                if today < depart_date:
                    table.append(row)
            elif param == 'start_airport':
                if filter == start_airport['city'] and today < depart_date :
                    row = [column0, column1, column2, column3]
                    table.append(row)
                elif vk and is_flight_in_list(konkretanfID, flight_list):
                    flight_list.append(konkretanfID)
            elif param == 'end_airport':
                if filter == end_airport['city'] and today < depart_date :
                    row = [column0, column1, column2, column3]
                    table.append(row)
                elif vk and is_flight_in_list(konkretanfID, flight_list):
                    flight_list.append(konkretanfID)

            elif param == 'start_date':
                if filter == start_date and today < depart_date:
                    row = [column0, column1, column2, column3]
                    table.append(row)
                elif vk and is_flight_in_list(konkretanfID, flight_list):
                    flight_list.append(konkretanfID)

            elif param == 'end_date':
                if filter == end_date and today < depart_date:
                    row = [column0, column1, column2, column3]
                    table.append(row)
                elif vk and is_flight_in_list(konkretanfID, flight_list):
                    flight_list.append(konkretanfID)

            elif param == 'start_time':
                if filter == start_time and today < depart_date:
                    row = [column0, column1, column2, column3]
                    table.append(row)
                elif vk and is_flight_in_list(konkretanfID, flight_list):
                    flight_list.append(konkretanfID)

            elif param == 'end_time':
                if filter == end_time and today < depart_date:
                    row = [column0, column1, column2, column3]
                    table.append(row)
                elif vk and is_flight_in_list(konkretanfID, flight_list):
                    flight_list.append(konkretanfID)

            elif param == 'carrier':
                if filter == carrier and today < depart_date :
                    row = [column0, column1, column2, column3]
                    table.append(row)
                elif vk and is_flight_in_list(konkretanfID, flight_list):
                    flight_list.append(konkretanfID)

    if len(table) == 0:
        print(text_red + 'Ne postoji ni jedan let koji zadovoljava dati kriterijum (ili ste nešto pogrešno uneli)!'
              + text_end)
        return
    else:
        print_table(table)
        input('Pritisnite ENTER da se vratite na prethoni meni...')





filter_params = {'1': 'start_airport',
                 '2': 'end_airport',
                 '3': 'start_date',
                 '4': 'end_date',
                 '5': 'start_time',
                 '6': 'end_time',
                 '7': 'carrier'}

param_names = {'start_airport': 'polazište (grad)',
               'end_airport': 'odredište (grad)',
               'start_date': 'datum polaska (dd.mm.yyyy.)',
               'datum odlaska': 'datum dolaska (dd.mm.yyyy.)',
               'start_time': 'vreme poletanja (HH:MM)',
               'end_time': 'vreme sletanja (HH:MM)',
               'carrier': 'prevoznika'}


def is_flight_in_list(flightID, flight_list):
    found = False
    for id in flight_list:
        if flightID == id:
            found = True

    return found


def pretraga():
    global filter_params
    global param_names

    print('1 - Polazište\n'
          '2 - Odredište\n'
          '3 - Datum polaska\n'
          '4 - Datum dolaska\n'
          '5 - Vreme poletanja\n'
          '6 - Vreme sletanja\n'
          '7 - Prevoznik')
    while True:
        param = input('Unesite broj za odgovarajući kriterijum pretrage: ')
        if param not in filter_params:
            print(text_red + 'Odabrali ste nepostojeću opciju!' + text_end)
            return

        filter = input('Izaberite ' + param_names[filter_params[param]] + ': ')
        while len(filter) == 0:
            print(text_red + 'Polje ne sme biti prazno!' + text_end)
            filter = input('Izaberite ' + param_names[filter_params[param]] + ': ')

        nerealizovani(filter, filter_params[param])
        return



def VKpretraga():
    filters = {}
    izbor = {'da': True,
             'DA': True,
             'Da': True,
             'dA': True,
             'ne': False,
             'NE': False,
             'Ne': False,
             'nE': False}
    global filter_params
    try:

        param, filter = choice()

    except TypeError:
        return

    filters[filter_params[param]] = filter
    while True:
        unos = input('Da li želite pretraživati po još jednom kriterijumu? (DA/NE)\n>>')
        while unos not in izbor:
            unos = input('Da li želite pretraživati po još jednom kriterijumu? (>DA/NE<)\n>>')

        if izbor[unos] is False:
            VKprint(filters)
            return

        else:
            param, filter = choice()
            filters[filter_params[param]] = filter


def choice():
    global filter_params
    global param_names

    print('1 - Polazište\n'
          '2 - Odredište\n'
          '3 - Datum polaska\n'
          '4 - Datum dolaska\n'
          '5 - Vreme poletanja\n'
          '6 - Vreme sletanja\n'
          '7 - Prevoznik')
    while True:
        param = input('Unesite broj za odgovarajući kriterijum pretrage: ')
        if param not in filter_params:
            print(text_red + 'Odabrali ste nepostojeću opciju!' + text_end)
            return

        filter = input('Izaberite ' + param_names[filter_params[param]] + ': ')
        while len(filter) == 0:
            print(text_red + 'Polje ne sme biti prazno!' + text_end)
            filter = input('Izaberite ' + param_names[filter_params[param]] + ': ')

        return param, filter

def VKprint(filters):
    flight_table = []

    filter_num = len(filters)

    flights_dict()
    regularflights_dict()
    airports_dict()

    for flight in range(len(flights) + 1):
        if flight != 0:
            konkretanfID = '{0:0>4}'.format(str(flight))
            start_date = flights[konkretanfID]['start_date']

            flightnum = flights[konkretanfID]['flight_num']

            end_date = flights[konkretanfID]['end_date']

            current_flight_data = flight_data(flightnum)

            start_airport = current_flight_data['start_airport']
            start_airport = airport_data(start_airport)
            depart_country_city = start_airport['city'] + ', ' + start_airport['country']

            end_airport = current_flight_data['end_airport']
            end_airport = airport_data(end_airport)
            arrival_country_city = end_airport['city'] + ', ' + end_airport['country']

            start_time = current_flight_data['start_time']
            end_time = current_flight_data['end_time']

            price = current_flight_data['ticket_price'] + ' €'

            carrier = current_flight_data['carrier']

            startdt = start_date + ', ' + start_time
            enddt = end_date + ', ' + end_time
            flduration = duration(startdt, enddt)
            column1text = 'Polazak:\n' + startdt + '\n' + depart_country_city
            column3text = 'Dolazak:\n' + enddt + '\n' + arrival_country_city
            column0 = 'Broj leta:\n' + str(konkretanfID)
            column1 = '{:^20}'.format(column1text)
            column2 = '{:^20}'.format(
                'Vreme letenja: ' + str(flduration) + '\nCena: ' + price + '\nPrevoznik: ' + carrier)
            column3 = '{:^20}'.format(column3text)

            today = datetime.datetime.today()
            depart_date = convert_datetime(startdt)
            append = False
            count = 0

            if today < depart_date:

                try:
                    if filters['start_airport'] == start_airport['city']:
                        append = True
                        count += 1
                except KeyError:
                    pass

                try:
                    if filters['end_airport'] == end_airport['city']:
                        append = True
                        count += 1
                except KeyError:
                    pass

                try:
                    if filters['start_time'] == start_time:
                        append = True
                        count += 1
                except KeyError:
                    pass

                try:
                    if filters['end_time'] == end_time:
                        append = True
                        count += 1
                except KeyError:
                    pass

                try:
                    if filters['start_date'] == start_date:
                        append = True
                        count += 1
                except KeyError:
                    pass

                try:
                    if filters['end_date'] == end_date:
                        append = True
                        count += 1
                except KeyError:
                    pass

                try:
                    if filters['carrier'] == carrier:
                        append = True
                        count += 1
                except KeyError:
                    pass

                if append is True and count == filter_num:
                    row = [column0, column1, column2, column3]
                    flight_table.append(row)

    if len(flight_table) == 0:
        print(text_red + 'Ne postoji ni jedan let koji zadovoljava dati kriterijum (ili ste nešto pogrešno uneli)!'
              + text_end)
        return
    print_table(flight_table)
    input('Pritisnite ENTER da se vratite na prethoni meni...')
    return






def jeftino():
    provera()


def fleks_polazak():
    provera()


def regularflights_dict():
    regularflights_list = file_list('avionski_letovi.txt')
    global regular_flights

    flightslen = len(regularflights_list)

    for flightnum in range(flightslen):

        current_flight = regularflights_list[flightnum]
        # pretvaramo sletanje sl dana (da/ne) u boolean vrednost
        if current_flight[5] == 'da':
            l_n_day = True
        else:
            l_n_day = False
        # broj leta je prvi element niza (zbog konstrukcije podataka)
        flightnum = current_flight[0]
        # dane letenja stavljamo u listu
        days = current_flight[7]
        days = days.split(' ')
        # pravimo recnik od podataka iz liste
        current_flightdict = {
            'start_airport': current_flight[1],
            'end_airport': current_flight[2],
            'start_time': current_flight[3],
            'end_time': current_flight[4],
            'land_next_day': l_n_day,
            'carrier': current_flight[6],
            'flight_days': days,
            'plane_model': current_flight[8],
            'ticket_price': current_flight[9]
        }
        regular_flights[flightnum] = current_flightdict

    return regular_flights


def flights_dict():
    flight_list = file_list('konkretni_letovi.txt')
    global flights

    flightlen = len(flight_list)
    # slican algoritam kao za regularflights_dict samo recnik drugacije izgleda zbog strukture podataka
    for flightnum in range(flightlen):
        current_flight = flight_list[flightnum]
        flightid = current_flight[0]
        current_flightdict = {
            'flight_num': current_flight[1],
            'start_date': current_flight[2],
            'end_date': current_flight[3],
        }
        flights[flightid] = current_flightdict

    return flights


def planemodels_dict():
    global plane_models
    models = file_list('modeli_aviona.txt')
    modellen = len(models)
    for model in range(modellen):
        current_model = models[model]
        model_name = current_model[0]
        model_dict = {
            'rows': current_model[1],
            'position_in_row': current_model[2]
        }
        plane_models[model_name] = model_dict

    return plane_models


def airports_dict():
    airport_list = file_list('aerodromi.txt')
    global airports

    listlen = len(airport_list)
    for airport in range(len(airport_list)):
        current_airport = airport_list[airport]
        airportID = current_airport[0]
        airport_dict = {
            'name': current_airport[1],
            'city': current_airport[2],
            'country': current_airport[3]
        }
        airports[airportID] = airport_dict

    return airports


def flight_data(flightnum):
    flight_data = regular_flights[flightnum]

    return flight_data


def airport_data(airportID):
    airport_data = airports[airportID]

    return airport_data


def convert_datetime(datet):
    date_time = datet.split(', ')
    date = date_time[0].split('.')
    time = date_time[1].split(':')
    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    hours = int(time[0])
    minutes = int(time[1])

    return datetime.datetime(year, month, day, hours, minutes)


def convert_date(date):
    datelist = date.split('.')
    year = int(date[2])
    month = int(date[1])
    day = int(date[0])
    return datetime.date(year, month, day)


def duration(start, end):
    departure = convert_datetime(start)
    arrival = convert_datetime(end)
    delta = arrival - departure
    return delta

# if __name__ == '__main__':
# nerealizovani()

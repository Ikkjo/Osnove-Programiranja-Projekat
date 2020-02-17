import datetime
import funkcije

danasnji_dan = datetime.datetime.today().weekday()
danas = datetime.datetime.today()
sifra_leta = ''


def generisanje():
    funkcije.ucitavanje_podataka()
    letovi = funkcije.letovi
    global sifra_leta
    k = 0
    konkretni = open('konkretni_letovi.txt', 'w')
    for i in range(len(letovi)):
        dani = letovi[i]['dani']
        dani = dani.split()
        for dan in dani:
            if dan == 'ponedeljak':
                dan = 0
            elif dan == 'utorak':
                dan = 1
            elif dan == 'sreda':
                dan = 2
            elif dan == 'četvrtak':
                dan = 3
            elif dan == 'petak':
                dan = 4
            elif dan == 'subota':
                dan = 5
            elif dan == 'nedelja':
                dan = 6
            if dan < danasnji_dan:
                dan_poletanja = danas + datetime.timedelta(7 - (danasnji_dan - dan))
                k += 1
                if k < 10:
                    sifra_leta = 3 * '0' + str(k)
                elif 10 <= k < 100:
                    sifra_leta = 2 * '0' + str(k)
                elif 100 <= k < 1000:
                    sifra_leta = '0' + str(k)
                elif 1000 <= k < 10000:
                    sifra_leta = str(k)
                if letovi[i]['sledeci dan'] == 'da':
                    dan_sletanja = dan_poletanja + datetime.timedelta(1)
                else:
                    dan_sletanja = dan_poletanja
                day = str(dan_poletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_poletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_poletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_poletanja.year)
                day = str(dan_sletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_sletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_sletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_sletanja.year)
                konkretni.write(sifra_leta + '|' + letovi[i]['broj leta'] + '|' + dan_poletanja + '|' + dan_sletanja +
                                '\n')
                dan_poletanja = danas + datetime.timedelta(14 - (danasnji_dan - dan))
                k += 1
                if k < 10:
                    sifra_leta = 3 * '0' + str(k)
                elif 10 <= k < 100:
                    sifra_leta = 2 * '0' + str(k)
                elif 100 <= k < 1000:
                    sifra_leta = '0' + str(k)
                elif 1000 <= k < 10000:
                    sifra_leta = str(k)
                if letovi[i]['sledeci dan'] == 'da':
                    dan_sletanja = dan_poletanja + datetime.timedelta(1)
                else:
                    dan_sletanja = dan_poletanja
                day = str(dan_poletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_poletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_poletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_poletanja.year)
                day = str(dan_sletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_sletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_sletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_sletanja.year)
                konkretni.write(sifra_leta + '|' + letovi[i]['broj leta'] + '|' + dan_poletanja + '|' + dan_sletanja +
                                '\n')
            elif dan == danasnji_dan:
                dan_poletanja = danas + datetime.timedelta(7)
                k += 1
                if k < 10:
                    sifra_leta = 3 * '0' + str(k)
                elif 10 <= k < 100:
                    sifra_leta = 2 * '0' + str(k)
                elif 100 <= k < 1000:
                    sifra_leta = '0' + str(k)
                elif 1000 <= k < 10000:
                    sifra_leta = str(k)
                if letovi[i]['sledeci dan'] == 'da':
                    dan_sletanja = dan_poletanja + datetime.timedelta(1)
                else:
                    dan_sletanja = dan_poletanja
                day = str(dan_poletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_poletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_poletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_poletanja.year)
                day = str(dan_sletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_sletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_sletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_sletanja.year)
                konkretni.write(sifra_leta + '|' + letovi[i]['broj leta'] + '|' + dan_poletanja + '|' + dan_sletanja +
                                '\n')
                dan_poletanja = danas
                k += 1
                if k < 10:
                    sifra_leta = 3 * '0' + str(k)
                elif 10 <= k < 100:
                    sifra_leta = 2 * '0' + str(k)
                elif 100 <= k < 1000:
                    sifra_leta = '0' + str(k)
                elif 1000 <= k < 10000:
                    sifra_leta = str(k)
                if letovi[i]['sledeci dan'] == 'da':
                    dan_sletanja = dan_poletanja + datetime.timedelta(1)
                else:
                    dan_sletanja = dan_poletanja
                day = str(dan_poletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_poletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_poletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_poletanja.year)
                day = str(dan_sletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_sletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_sletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_sletanja.year)
                konkretni.write(sifra_leta + '|' + letovi[i]['broj leta'] + '|' + dan_poletanja + '|' + dan_sletanja +
                                '\n')
            elif dan > danasnji_dan:
                dan_poletanja = danas + datetime.timedelta(dan - danasnji_dan)
                k += 1
                if k < 10:
                    sifra_leta = 3 * '0' + str(k)
                elif 10 <= k < 100:
                    sifra_leta = 2 * '0' + str(k)
                elif 100 <= k < 1000:
                    sifra_leta = '0' + str(k)
                elif 1000 <= k < 10000:
                    sifra_leta = str(k)
                if letovi[i]['sledeci dan'] == 'da':
                    dan_sletanja = dan_poletanja + datetime.timedelta(1)
                else:
                    dan_sletanja = dan_poletanja
                day = str(dan_poletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_poletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_poletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_poletanja.year)
                day = str(dan_sletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_sletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_sletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_sletanja.year)
                konkretni.write(sifra_leta + '|' + letovi[i]['broj leta'] + '|' + dan_poletanja + '|' + dan_sletanja +
                                '\n')
                dan_poletanja = danas + datetime.timedelta(7 + (dan - danasnji_dan))
                k += 1
                if k < 10:
                    sifra_leta = 3 * '0' + str(k)
                elif 10 <= k < 100:
                    sifra_leta = 2 * '0' + str(k)
                elif 100 <= k < 1000:
                    sifra_leta = '0' + str(k)
                elif 1000 <= k < 10000:
                    sifra_leta = str(k)
                if letovi[i]['sledeci dan'] == 'da':
                    dan_sletanja = dan_poletanja + datetime.timedelta(1)
                else:
                    dan_sletanja = dan_poletanja
                day = str(dan_poletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_poletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_poletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_poletanja.year)
                day = str(dan_sletanja.day)
                if len(day) != 2:
                    day = '0' + day
                mesec = str(dan_sletanja.month)
                if len(mesec) != 2:
                    mesec = '0' + mesec
                dan_sletanja = '{:}.{:}.{:}.'.format(day, mesec, dan_sletanja.year)
                konkretni.write(sifra_leta + '|' + letovi[i]['broj leta'] + '|' + dan_poletanja + '|' + dan_sletanja +
                                '\n')
    konkretni.close()


if __name__ == '__main__':
    generisanje()

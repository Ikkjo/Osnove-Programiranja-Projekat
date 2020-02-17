from file_list import file_list

text_red = '\033[91m'
text_green = '\033[32m'
text_end = '\033[0m'

users = {}

def input_passpnum():
    while True:
        passp_num = input('Unesite broj pasoša: ')
        if len(passp_num) == 9:
            try:
                int(passp_num)
                break

            except ValueError:
                return print(text_red + 'Greška, BROJ pasoša mora sadržati samo BROJEVE.' + text_end)
        else:
            print(text_red + 'Greška, broj pasoša mora imati 9 cifara.' + text_end)
    return passp_num


def input_nationality():
    nationality = input('Unesite državljanstvo: ')
    while len(nationality) <3:
        print(text_red + 'Greška, pokušajte ponovo' + text_end)
        nationality = input('Unesite državljanstvo: ')

    return nationality


def input_gender():
    gender = input("Unesite pol: ")
    while len(gender) == 0:
        print(text_red + 'Greška, pokušajte ponovo' + text_end)
        gender = input("Unesite pol: ")
    return gender

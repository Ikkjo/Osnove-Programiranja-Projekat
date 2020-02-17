from menu_maker import menu
from data_input import input_passpnum, input_gender, input_nationality
from find_userdata import users_dict, data_from_uname
from provera import provera
from domains import domain_list

text_red = '\033[91m'
text_green = '\033[32m'
text_end = '\033[0m'

logged_user = ''


def reg():
    kor_ime, lozinka, tel, e_mail, ime, prezime = reg_input()
    try:
        broj_pasosa, drzavljanstvo, pol = dodatni_podaci()

    except TypeError:
        broj_pasosa, drzavljanstvo, pol = '', '', ''
    novi_korisnik = {
        'u_name': kor_ime,
        'passw': lozinka,
        'name': ime,
        'surname': prezime,
        'uloga': 'kupac',
        'passp_num': broj_pasosa,
        'nationality': drzavljanstvo,
        'phone_num': tel,
        'mail': e_mail,
        'gender': pol,

    }
    korisnik_upis = formatiraj_za_upis(novi_korisnik)
    upis_korisnika(korisnik_upis)
    print(text_green + 'Uspešno ste se registrovali!\nSada se možete prijaviti na sistem sa nalogom'
                       ' koji ste napravili.' + text_end)


def formatiraj_za_upis(novi_korisnik, prodavac=False):

    if prodavac is True:
        upis = ('\n' + novi_korisnik['u_name'] + '|' + novi_korisnik['passw'] + '|' + novi_korisnik['name'] + '|' +
                novi_korisnik['surname'] + '|' + novi_korisnik['uloga'])

    else:
        upis = ('\n' + novi_korisnik['u_name'] + '|' + novi_korisnik['passw'] + '|' + novi_korisnik['name'] + '|' +
                novi_korisnik['surname'] + '|' + novi_korisnik['uloga'] + '|' + novi_korisnik['passp_num'] + '|' +
                novi_korisnik['nationality'] + '|' + novi_korisnik['phone_num'] + '|' + novi_korisnik['mail'] + '|' +
                novi_korisnik['gender'])

    return upis


def upis_korisnika(korisnik):
    file = open('korisnici.txt', 'a', encoding='utf-8')
    file.write(korisnik)
    file.close()


def reg_input():
    kor_ime = input('Unesite vaše korisničko ime: ')  # implementiraj i provere
    while len(kor_ime) <= 4:
        print(text_red + 'Greška, minimalan broj karaktera je 4' + text_end)
        kor_ime = input('Unesite vaše korisničko ime: ')

    while check_term('u_name', kor_ime) is True:
        print(text_red + 'Greška, već postoji korisnik sa tim korisničnim imenom.\nPokušajte ponovo.' + text_end)
        kor_ime = input('Unesite vaše korisničko ime: ')

    lozinka = input('Unesite vašu lozinku: ')
    while len(kor_ime) <= 4:
        print(text_red + 'Greška, minimalan broj karaktera je 4' + text_end)


    tel = input('Unesite vaš broj kontakt telefona: ')
    while check_term('phone_num', tel):
        print(text_red + 'Greška, već postoji korisnik sa tim brojem telefona.\nPokušajte ponovo: ' + text_end)
    tel = provera_tel(tel)
    e_mail = input('Unesite vašu e-mail adresu: ')
    while check_term('mail', e_mail) is True:
        print(text_red + 'Greška, već postoji korisnik sa tom e-mail adresom.\nPokušajte ponovo: ' + text_end)
        e_mail = input('Unesite vašu e-mail adresu: ')
    chkmail = provera_email(e_mail)
    ime = input('Unesite vaše ime: ')
    while len(ime) == 0:
        print(text_red + 'Greška, polje ne sme biti prazno' + text_end)
        ime = input('Unesite vaše ime: ')

    prezime = input('Unesite vaše prezime: ')
    while len(prezime) == 0:
        print(text_red + 'Greška, polje ne sme biti prazno' + text_end)

    return kor_ime, lozinka, tel, chkmail, ime, prezime


def seller_reg():
    kor_ime = input('Unesite korisničko ime prodavca: ')  # implementiraj i provere
    while len(kor_ime) <= 4:
        print(text_red + 'Greška, minimalan broj karaktera je 4' + text_end)
        kor_ime = input('Unesite vaše korisničko ime: ')

    while check_term('u_name', kor_ime) is True:
        print(text_red + 'Greška, već postoji korisnik sa tim korisničnim imenom.\nPokušajte ponovo.' + text_end)
        kor_ime = input('Unesite vaše korisničko ime: ')

    lozinka = input('Unesite lozinku prodavca: ')
    while len(kor_ime) <= 4:
        print(text_red + 'Greška, minimalan broj karaktera je 4' + text_end)

    ime = input('Unesite ime prodavca: ')
    while len(ime) == 0:
        print(text_red + 'Greška, polje ne sme biti prazno' + text_end)
        ime = input('Unesite vaše ime: ')

    prezime = input('Unesite prezime prodavca: ')
    while len(prezime) == 0:
        print(text_red + 'Greška, polje ne sme biti prazno' + text_end)

    novi_korisnik = {
        'u_name': kor_ime,
        'passw': lozinka,
        'name': ime,
        'surname': prezime,
        'uloga': 'prodavac'}

    korisnik_upis = formatiraj_za_upis(novi_korisnik, prodavac=True)
    upis_korisnika(korisnik_upis)
    print(text_green + 'Uspešno ste registrovali novog prodavca!\n' + text_end)
    return







def dodatni_podaci():
    odabir = input('Da li želite uneti dodatne podatke? \n(Broj pasoša, državljanstvo, pol)\n>>')
    if odabir == 'NE' or odabir == 'Ne' or odabir == 'ne':
        return
    passp_num = input_passpnum()
    nationality = input_nationality()
    gender = input_gender()

    return passp_num, nationality, gender


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
                           '\nUnesite vašu e-mail adresu: ')
            e_mail = e_mail.split('@')

        try:  # kad se unese jedno slovo izbaci IndexError
            while e_mail[0] == '' or e_mail[1] == '':
                e_mail = input(
                    text_red + 'Format mail-a nije dobar, fali nešto pre ili posle "@"?' + text_end +
                    '\nUnesite vašu e-mail adresu: ')
                e_mail = e_mail.split('@')

        except IndexError:
            e_mail = input(text_red + 'Oblik mail-a mora biti ' + text_end + 'ime@domen\nUnesite vašu e-mail adresu: ')

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
                '\nUnesite vašu e-mail adresu: ')

    mail = e_mail[0] + '@' + e_mail[1]  # spajam nazad ime i domen
    return mail


def provera_tel(tel):
    while True:
        try:
            int(tel)
            break

        except ValueError:
            tel = input(text_red + 'Greška, niste ispravno uneli broj telefona' + text_end +
                        '\nUnesite vaš broj kontakt telefona: ')

    return tel


def check_passw(uname, passw):
    user_dict = users_dict()
    match = False
    for index in range(len(user_dict)):
        ind = str(index)
        current_user = 'user' + ind
        if uname == user_dict[current_user]['u_name'] and passw == user_dict[current_user]['passw']:
            match = True

    return match


def log():
    uname = input('Korisničko ime: ')
    passw = input('Šifra: ')
    while check_term('u_name', uname) is False or check_passw(uname, passw) is False:
        print(text_red + 'Greška, korisnik ne postoji.\nPokušajte ponovo.' + text_end)
        uname = input('Korisničko ime: ')
        passw = input('Šifra: ')

    registration_succ(uname)
    uloga = data_from_uname(uname, 'uloga')
    write_logged_user = open('current_user.txt', 'w', encoding='utf=8')
    write_logged_user.write(uname)
    write_logged_user.close()

    menu(uloga)


def registration_succ(uname):
    print('{0}{1}{4}{2}{3}{4}{0}{1}{4}'.format(text_red, '💯💯🔥🔥', text_green,
                                               'Uspešno ste se registrovali, ' + uname + '!', text_end))


# if __name__=='__main__':
# log_out()

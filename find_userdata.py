from file_list import file_list

text_red = '\033[91m'
text_green = '\033[32m'
text_end = '\033[0m'

users = {}

def data_from_uname(uname,param):
    user_dict = users_dict()

    for index in range(len(user_dict)):
        ind = str(index)
        current_user = 'user' + ind
        try:
            if uname == user_dict[current_user]['u_name']:
                ret_param = user_dict[current_user][param]
                return ret_param

        except IndexError:
                continue

    return print(text_red + 'SYSTEM ERROR, NO USER WITH SUCH PARAM' + text_end)



def alldata_from_uname(uname):
    user_dict = users_dict()
    found = False
    index = 0
    try:
        while not found:
            ind = str(index)
            current_user = 'user' + ind
            if uname == user_dict[current_user]['u_name']:
                user = user_dict[current_user]
                found = True
            index += 1
    except KeyError:
        user = {}

    return user


def users_dict():
    global users
    users = {}
    user_list = file_list('korisnici.txt')
    userlen = len(user_list)
    for usernum in range(userlen):
        userid = 'user' + str(usernum)
        current_user = user_list[usernum]
        if current_user[4] == 'kupac':
            current_userdict = {
                'u_name': current_user[0],
                'passw': current_user[1],
                'name': current_user[2],
                'surname': current_user[3],
                'uloga': current_user[4],
                'passp_num': current_user[5],
                'nationality': current_user[6],
                'phone_num': current_user[7],
                'mail': current_user[8],
                'gender': current_user[9],
            }
        else:
            current_userdict = {
                'u_name': current_user[0],
                'passw': current_user[1],
                'name': current_user[2],
                'surname': current_user[3],
                'uloga': current_user[4],
            }
        users[userid] = current_userdict

    return users

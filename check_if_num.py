def check_if_num(number):
    try:
        int(number)
        return True

    except TypeError:
        return False

    except ValueError:
        return False
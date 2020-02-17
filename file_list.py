def file_list(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    newfile = file.read()
    file.close()
    newfile = newfile.split('\n')
    for line in range(len(newfile)):
        newfile[line] = newfile[line].split('|')
        line += 1

    return newfile

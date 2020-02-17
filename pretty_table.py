def pretty_table(rows,columns,elements):
    for list in range(rows):
        if list == 0:
            if columns != 2:
                columnprint = ('╦' + '═'*28 + '╦')*(rows-2)
            else:
                columnprint = ''
            print('╔'+'═'*30 + columnprint + '═'*30 + '╗')
        else:
            columnprint = '═'*30
            print(columnprint)
        current_el = elements[list]
        for item in current_el:
            if item == current_el[0]:
                print('║{0:^30}║'.format(item),end='')
            else:
                print('{0:^30}║'.format(item),end='')

        if list == rows:
            rowprint = ('╩' + '═' * 28 + '╩') * (rows - 2)
            print('╚' + '═' * 30 + rowprint + '═' * 30 + '╝')







matrix = [['ponedeljak', 'utorak', 'sreda'],[1,2,3]]
pretty_table(2,3,matrix)

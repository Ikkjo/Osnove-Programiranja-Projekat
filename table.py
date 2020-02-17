from tabulate import tabulate

def print_table(data):
    print(tabulate(data, tablefmt = 'fancy_grid'))
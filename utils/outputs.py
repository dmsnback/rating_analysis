from prettytable import PrettyTable


def pretty_output(result):
    """Создание и печаь таблицы"""
    table = PrettyTable()
    table.field_names = [''] + list(result[0].keys())
    count = 0
    for row in result:
        count += 1
        table.add_row([count] + list(row.values()))
    print(table)

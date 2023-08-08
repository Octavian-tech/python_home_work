def printTable(table):
    print(table[1] + " | " + table[2] + " | " + table[3])
    print("---------")
    print(table[4] + " | " + table[5] + " | " + table[6])
    print("---------")
    print(table[7] + " | " + table[8] + " | " + table[9])


def set_next_move(lista, symbol, table):
    for item in lista:
        if table[item[0]] == table[item[1]] == symbol and table[item[2]] == '-':
            return item[2]
        elif table[item[0]] == table[item[2]] == symbol and table[item[1]] == '-':
            return item[1]
        elif table[item[1]] == table[item[2]] == symbol and table[item[0]] == '-':
            return item[0]
    return None


def is_victory(table, icon):
    if (table[1] == table[2] == table[3] == icon) or \
            (table[4] == table[5] == table[6] == icon) or \
            (table[7] == table[8] == table[9] == icon) or \
            (table[1] == table[4] == table[7] == icon) or \
            (table[2] == table[5] == table[8] == icon) or \
            (table[3] == table[6] == table[9] == icon) or \
            (table[1] == table[5] == table[9] == icon) or \
            (table[3] == table[5] == table[7] == icon):
        return True
    else:
        return False


def machine_player(table, lista, symbol, symbol2):
    # Verifica daca poate castiga
    next_move = set_next_move(lista, symbol, table)
    if next_move is not None:
        return next_move

    # Verifica daca juctorul uman poate castiga si blocheaza mutarea
    next_move = set_next_move(lista, symbol2, table)
    if next_move is not None:
        return next_move

    if table[5] == '-':
        return 5

    if table[1] == '-':
        return 1
    if table[3] == '-':
        return 3
    if table[7] == '-':
        return 7
    if table[9] == '-':
        return 9

    # Alege orice alta mutare disponibila
    for pos in range(1, 10):
        if table[pos] == '-':
            return pos


def check_position(table, position) -> int:
    while table[int(position)] != '-':
        print("Pozitia este ocupata alege din nou \n")
        position = input("Alege pozitia:")
    return int(position)


list_pos_castig = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [1, 4, 7],
                   [2, 5, 8],
                   [3, 6, 9],
                   [1, 5, 9],
                   [3, 5, 7]]

your_symbol = input(("Alege simbolul tau (X sau 0):"))
pc_symbol = 'X'
your_position = None

if your_symbol == 'X':
    pc_symbol = '0'

table = {pos: '-' for pos in range(1, 10)}
print(table)

while "-" in table.values():
    your_position = input("Alege pozitia: ")

    table[check_position(table, position=your_position)] = your_symbol

    printTable(table)
    print('#####################')

    if is_victory(table, your_symbol):
        print("Ai castigat")
        break

    if "-" not in table.values():
        print("Jocul sa finalizat")
        break

    pc_position = machine_player(table, lista=list_pos_castig, symbol=pc_symbol, symbol2=your_symbol)
    print(pc_position)
    table[pc_position] = pc_symbol
    printTable(table)

    if is_victory(table, pc_symbol):
        print("0 wins! Congratulation")
        break

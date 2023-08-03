table = {
    1: '-',
    2: '-',
    3: '-',
    4: '-',
    5: '-',
    6: '-',
    7: '-',
    8: '-',
    9: '-',
}

jucatorulCurent = "X"
castigator = None
joculRuleaza = True


def printTable(table):
    print(table[1] + " | " + table[2] + " | " + table[3])
    print("---------")
    print(table[4] + " | " + table[5] + " | " + table[6])
    print("---------")
    print(table[7] + " | " + table[8] + " | " + table[9])


def playerInput(table):
    select = int(input("Selecteaza optiunea 1-9:"))
    if table[select] == '-':
        table[select] = jucatorulCurent
    else:
        print("Oops jucatorul a ales deja acea pozitie.")


def checkHorizontal(table):
    global castigator
    if table[1] == table[2] == table[3] != "-":
        castigator = table[1]
        return True
    elif table[4] == table[5] == table[6] != "-":
        castigator = table[4]
        return True
    elif table[7] == table[8] == table[9] != "-":
        castigator = table[7]
        return True


def checkRow(table):
    global castigator
    if table[1] == table[4] == table[7] != "-":
        castigator = table[1]
        return True
    elif table[2] == table[5] == table[8] != "-":
        castigator = table[2]
        return True
    elif table[3] == table[6] == table[9] != "-":
        castigator = table[3]
        return True


def checkDiag(table):
    global castigator
    if table[1] == table[5] == table[9] != "-":
        castigator = table[1]
        return True
    elif table[3] == table[5] == table[7] != "-":
        castigator = table[2]
        return True


choose_symbol = input("ALEGE SIMBOLUL:")
choose_pc = 'X'
choose_position = None

if choose_symbol == 'X':
    choose_pc = '0'


def test_move(lista, symbol, table):
    next_move = None

    for i in lista:
        if table[int(i[0])] == table[int(i[1])] == symbol and i[2] == '-':
            next_move = i[2]
        elif table[int(i[0])] == table[int(i[2])] == symbol and i[1] == '-':
            next_move = i[1]
        elif table[int(i[1])] == table[int(i[2])] == symbol and i[0] == '-':
            next_move = i[0]

        if next_move is not None:
            print(next_move)
            return next_move

    return None


def pc_choose(table, list, symbol, symbol2):
    if test_move(list, symbol, table) is not None:
        table[test_move(list, symbol, table)] = symbol
        printTable(table)
    elif test_move(list, symbol2, table) is not None:
        table[test_move(list, symbol2, table)] = symbol2
        printTable(table)
    elif table[5] == '-':
        table[5] = symbol
    elif table[1] == '-':
        table[1] = symbol
    elif table[3] == '-':
        table[3] = symbol
    elif table[7] == '-':
        table[7] = symbol
    elif table[9] == '-':
        table[9] = symbol

    return table


def control_position(table, position) -> int:
    while table[int(position)] != '-':
        position = input("Alege pozitia:")
    return int(position)


lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [1, 4, 7],
         [2, 5, 8],
         [3, 6, 9],
         [1, 5, 9],
         [3, 5, 7]]

if choose_symbol == 'X':
    printTable(table)
    while "-" in table.values():
        choose_position = input("Alege pozitia:")
        table[control_position(table, position=choose_position)] = 'X'
        print(table)
        printTable(table)
        table = pc_choose(table, lista, 'O', 'X')

        printTable(table)

print(choose_symbol)
# test_move(list, choose_symbol)

# while joculRuleaza:
#     printTable(table)

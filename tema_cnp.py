judete_romania = {
    "01": "Alba",
    "02": "Arad",
    "03": "Argeș",
    "04": "Bacău",
    "05": "Bihor",
    "06": "Bistrița-Năsăud",
    "07": "Brăila",
    "08": "Botoșani",
    "09": "Brașov",
    "10": "Buzău",
    "11": "Caraș-Severin",
    "12": "Călărași",
    "13": "Cluj",
    "14": "Constanța",
    "15": "Covasna",
    "16": "Dâmbovița",
    "17": "Dolj",
    "18": "Galați",
    "19": "Giurgiu",
    "20": "Gorj",
    "21": "Harghita",
    "22": "Hunedoara",
    "23": "Ialomița",
    "24": "Iași",
    "25": "Ilfov",
    "26": "Maramureș",
    "27": "Mehedinți",
    "28": "Mureș",
    "29": "Neamț",
    "30": "Olt",
    "31": "Prahova",
    "32": "Satu Mare",
    "33": "Sălaj",
    "34": "Sibiu",
    "35": "Suceava",
    "36": "Teleorman",
    "37": "Timiș",
    "38": "Tulcea",
    "39": "Vaslui",
    "40": "Vâlcea",
    "41": "Vrancea",
    "42": "București, Sector 1",
    "43": "București, Sector 2",
    "44": "București, Sector 3",
    "45": "București, Sector 4",
    "46": "București, Sector 5",
    "47": "București, Sector 6",
    "48": "București"
}


def validare_sex_sec(number):
    if number == 1:
        return True
    elif number == 2:
        return True
    elif number == 3:
        return True
    elif number == 4:
        return True
    elif number == 5:
        return True
    elif number == 6:
        return True
    elif number == 7:
        return True

    elif number == 8:
        return True
    return False


def validare_localitate(codArr):
    cod = "".join(str(n) for n in codArr)

    if cod in judete_romania:
        return True
    else:
        return False


def validare_numar_NNN(numar):
    if (numar < "001" or numar > "999"):
        print("nu se afla in interval")
        return False

    return True


def calculator_cifra_control(cnp):
    numere = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

    suma_totala = 0

    for cnpNum, numere in zip(cnp, numere):
        suma_totala = suma_totala + int(cnpNum) * numere
    rest = suma_totala % 11

    if rest == 10:
        return 1
    else:
        print(rest)
        return rest


def validare_data_nastere(an, luna, zi):
    zile = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if an < 0 or luna > 12 or zi < 1:
        print("Primul IF")
        return False

    if (an % 4 == 0 and an % 100 != 0) or an % 400 == 0:
        print("al doilea")
        zile[2] = 29

    if zi > zile[luna]:
        print("AL trilea")
        return False

    return True


CNP = "1800630340012"
# "1200229410089" exemplu an bisect
# "1800630340012" exemplu normal corect


zi = int("".join(str(n) for n in CNP[5:7]))
luna = int("".join(str(n) for n in CNP[3:5]))
an = int("".join(str(n) for n in CNP[1:3]))
NNN = "".join(str(n) for n in CNP[9:12])


# print(validare_sex_sec(int(CNP[0:1])))
# print(validare_data_nastere(an, luna, zi))
# print(validare_localitate(CNP[7:9]))
# print(validare_numar_NNN("995"))
# print(calculator_cifra_control(CNP) == int(CNP[12:13]))


def validareCNP(CNP):
    if validare_sex_sec(int(CNP[0:1])) and validare_data_nastere(an, luna, zi) and validare_localitate(
            CNP[7:9]) and validare_numar_NNN(NNN) and calculator_cifra_control(CNP) == int(CNP[12:13]):
        return True
    else:
        return False


if validareCNP(CNP):
    print("CNP ul este valid")
else:
    print("CNP ul nu este valid")

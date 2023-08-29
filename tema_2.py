# 1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
#
# caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
#
# In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
#
# caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
#
# preluat automat de la tastatura.
#

value = input("Introduceti ceva de la tastatura:")

# try:
#     float(value)
#     print("Digit")
# except ValueError:
#     print("Not a Digit")

if value.isdigit():
    print("isDIgit")
elif type(value) == str:
    print(f"Sirul de caractere a fost gasit de {value}")
else:
    print(type(value))

#
# 2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
#
# numar este par sau impar si afisati un raspuns in acest sens.


numar = input("Introduceti un numar:")

if int(numar) % 2 == 0:
    print(f"Numar {numar} este par")
else:
    print(f"Numar {numar} este impar")

# 3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
#
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
#
# la 4 (fara rest)
#

year = int(input("Introduceti anul:"))

if year % 400 == 0 and year % 100 == 0:
    print(f" Anul {year} este bisect")
elif year % 4 == 0 and year % 100 != 0:
    print(f"Anul {year} este bisect")
else:
    print(f"Anul {year} nu  este bisect")
#
# 4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
#
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
#
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
#
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
#
# afisati numarul pozitiv.
#
#
#
# 5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
#
# de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
#
# acest sir de caractere:
#
# “”” 1 – Afisare lista de cumparaturi
#
# 2 – Adaugare element
#
# 3 – Stergere element
#
# 4 – Sterere lista de cumparaturi
#
# 5 - Cautare in lista de cumparaturi “””
#
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
#
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
#
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
#
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
#
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
#
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”

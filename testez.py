# import json
#
# file_angajatii = open("angajatii.json","r")
# angajatii = json.load(file_angajatii)
# file_angajatii.close()
#
# key_to_be_deleted = str(input("cheia:"))
# for j in angajatii:
#     print(j)
#     print(type(j))
#     if key_to_be_deleted == j:
#         angajatii.pop(key_to_be_deleted)
#     else:
#         print(f'Key {key_to_be_deleted} is not in the dictionary')

#
# lista = []
# id = int(input("ID : "))
# for j in angajatii:
#     lista.append(angajatii[j][2])
# print(lista)
# if id not in lista:
#     print("nu se gaseste")
# else:
#
#     for i in angajatii:
#         if id in angajatii[i]:
#             print(angajatii[i])
from datetime import date
fdate = date.today().strftime('%d/%m/%Y')
print(fdate)

opt = "DA"
print(opt.lower())

if self.an_nastere < 2001:
    self.an_nastere = self.an_nastere - 1901
else:
    self.an_nastere = f"0{self.an_nastere - 2000}"

if self.zi_nastere < 10:
    self.zi_nastere = f"0{self.zi_nastere}"
else:
    self.zi_nastere = f"{self.zi_nastere}"

if self.luna_nastere < 10:
    self.luna_nastere = f"0{self.luna_nastere}"
else:
    self.luna_nastere = f"{self.luna_nastere}"

if self.functie == "Operator":
    id_log = 11
elif self.functie == "Manager":

    id_log = 99
else:
    # gestionar
    id_log = 22

# creez un cod unic angajat in firma
# self.email = f"{self.nume}.{self.prenume}@gmail.com"
print()
self.id = f"Codul unic de utilizator este : {id_log}{self.gen}{self.an_nastere}{self.luna_nastere}{self.zi_nastere}"
import json

class Meniu:

    #meniu = "Login : "
    invalid = "Invalid login"

    def login(self):
        #deschide angajatii si cauta daca e userul in lista dupa id_unic. Daca e returneaza o lista cu un singur user
        file_angajatii = open("angajatii.json","r")
        angajatii = json.load(file_angajatii)
        file_angajatii.close()

        lista = []
        id = input("Login ID : ")
        for j in angajatii:
            lista.append(angajatii[j][2])

        if id not in lista:
            print(self.invalid)
        else:
            for i in angajatii:
                if id in angajatii[i]:
                    return angajatii[i]
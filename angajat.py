import json
import copy
from datetime import date

# class Fabrica:
#     nume = "ALBASTROS"
#     def __init__(self,domeniu_activitate,adresa):
#         self.domeniu_activitate = domeniu_activitate
#         self.adresa = adresa

#Fabrica_mea = Fabrica["Iasi, Str Bucium , nr 10", "Productie electrocasnice"]
class Angajat:

    def __init__(self,prenume,nume,an_nastere,luna_nastere,zi_nastere,gen,functia):
        self.prenume = prenume
        self.nume = nume
        self.an_nastere = an_nastere
        self.luna_nastere = luna_nastere
        self.zi_nastere = zi_nastere
        self.gen = gen
        self.functia = functia
        self.mesaj = f"Bine ai venit {nume} {prenume}"


class Manager(Angajat):
    def __init__(self,data):
        super().__init__(data[0],data[1],data[2],date[3],data[4],data[5],data[6])
        self.id = data[7]

    def adaugare_angajat(self):
        print("Urmeaza sa adaugi un angajat!")
        print("*"*20)
        nume = str(input("Nume : "))
        prenume = str(input("Prenume : "))
        an_nastere = int(input("Anul : "))
        luna = int(input("Luna : "))
        zi = int(input("Zi : "))
        gen = int(input("Genul (2 feminin -1 masculin : "))


        if an_nastere<2001 and an_nastere>1989:
            an_nastere = an_nastere - 1900
        elif an_nastere>2000:
            an_nastere = f"0{an_nastere-2000}"

        if zi_nastere<10 :
            zi_nastere = f"0{zi_nastere}"
        else:
            zi_nastere = f"{zi_nastere}"

        if luna_nastere<10:
            luna_nastere = f"0{luna_nastere}"
        else:
            luna_nastere = f"{luna_nastere}"

        functia = str(input("Functia : "))

        if functie == "manager":
            id_log = 11
        elif functie == "operator":

            id_log = 33
        else:
            #gestionar
            id_log = 22

        #creez un cod unic angajat in firma
        print()
        id = f"{id_log}{gen}{an_nastere}{luna_nastere}{zi_nastere}"



        user_nou = [nume,prenume,an_nastere,luna,zi,gen,functia,id]
        file = open("angajatii.json","r")
        angajati = json.load(file)
        file.close()
        angajati[len(angajati)+1] = user_nou
        file_rescrie =open("angajatii.json","w")
        file_rescrie.write(json.dumps(angajati,indent=4))
        file_rescrie.close()
        print(f"Ai adaugat userul {nume} {prenume} ")


    def stergere_angajat(self):
        print("Urmeaza sa stergi un angajat !")
        print("*"*30)
        file = open("angajatii.json","r")
        angajati = json.load(file)

        #convertesc json in dictionar
        file.close()
        #afiseaza lista
        for i in angajati:
            print(f"{i} . {angajati[i][0]} {angajati[i][1]}")
        print()

        stergere_user = input("Ce angajat stergi?\n<")


        for key in list(angajati):
            if key == stergere_user:
                angajati.pop(key)

        file_angajati = open("angajatii.json","w")
        file_angajati.write(json.dumps(angajati,indent=4))
        file_angajati.close()
        print("Angajatul s-a sters!")

    def modificare_calificare(self):
        print("Modifica calificare unui angajat !")
        print("*"*30)
        file = open("angajatii.json","r")
        angajati = json.load(file)
        file.close()

        for i in angajati:
            print(f"{i}.{angajati[i][0]} {angajati[i][1]} cu id-ul {angajati[i][2]} are profesia {angajati[i][3]} ")

        print()
        user_calificare = input("Carui angajat ii modifici calificarea? \n>")
        for key in angajati:
            if key == user_calificare:
                new = str(input("Noua functie este : \n>"))
                angajati[key][3] = new
                if new == "operator":
                    angajati[key][2] = 33
                elif new =="gestionar":
                    angajati[key][2] =22
        file_a = open("angajatii.json","w")
        file_a.write(json.dumps(angajati,indent=4))
        file_a.close()
        print("S-a schimbat calificarea !")

    def menu(self):
        #print(self.mesaj)
        meniu = ["1. Adauga angajat","2.Sterge angajat","3.Modificare calificare","4.Exit"]
        for i in meniu:
            print(i)
        opt = int(input("Alege o optiune din meniu ! "))
        while True:
            if opt == 0:
                print("Existing program")
            elif opt == 1:
                self.adaugare_angajat()
                continue
            elif opt == 2:
                self.stergere_angajat()
                continue
            elif opt == 3:
                self.modificare_calificare()
                continue
            else:
                break




class Gestionar(Angajat):

    msg_stoc_initial = "Stocul la momentul actual din magazie !"
    print("*"*30)
    invalid = "Invalida optiune"

    def __init__(self,data):
        super().__init__(data[0],data[1],data[2])

    def menu(self):
        print()
        meniu = ["1. Stocul initial ! ","2.Adauga in stoc ! ","3.Generare pdf produse create !", "4.Exit! "]
        for i in meniu:
            print(i)
        opt = int(input("Alege o optiune! \n> " ))
        if opt ==1:
            self.stoc_initial()
        elif opt ==2:
            self.adaugare_stoc()
        elif opt ==3:
            self.generare_pdf()
        elif opt not in len(meniu):
            self.invalid()


    def stoc_initial(self):
        print(self.msg_stoc_initial)
        # deschid depozitul cu materiale
        file = open("depozit.json","r")
        produse = json.load(file)
        file.close()
        # aici e dictionar
        for key in produse:
            print(f"Produsul {key} are o cantitate de {produse[key]} bucati in stoc ! ")

    def adaugare_stoc(self):

        file = open("materiale.json","r")
        material = json.load(file)
        file.close()

        print("Urmeaza sa adaugi materiale in magazie !")
        print("*"*30)
        fdate = date.today().strftime('%d/%m/%Y')

        new_material = str(input("Ce material adaugati ?\n> "))
        new_nr = int(input("Cate bucati? \n<"))
        new = [fdate,new_material,new_nr]
        material[len(material) + 1] = new
        file_rescrie = open("materiale.json", "w")
        file_rescrie.write(json.dumps(material, indent=4))
        file_rescrie.close()
        print(f"Ai adaugat in magazie  {new_material} cu  {new_nr} Buc !")


    def generare_pdf(self):
        pass


class Operator(Angajat):

    msg2 = "Optiune invalida !"
    msg1 = "Urmeaza sa adaugi un produs !"

    def __init__(self,data):
        super().__init__(data[0],data[1],data[2],date[3],data[4],data[5],data[6])
        self.calificare = data[7]


    def menu(self):

        meniu = ["1. Creaza produs material", "2.Exit"]
        for i in meniu:
            print(i)
        while True:
            optiune = int(input("Alege o optiune! \n> "))
            if optiune == 1 :
                self.creaza_produs()
            elif  optiune not in range(len(meniu)):
                self.mesaj()
            else:
                break


    def creaza_produs(self):

        file = open("depozit.json","r")
        produse = json.load(file)
        file.close()
        print("Stocul initial de produse este : ")
        print("*"*30)
        for key in produse:
            print(f"{key}. {produse[key][0]}-{produse[key][1]} BUC !")

        optiune = str(input("Se introduc produse noi ? Raspuns asteptat : DA/NU \n <"))
        if optiune.lower() == "da":
            new_produs = str(input("Ce produs introduci? \n <"))
            nr_produs = int(input("Cate bucati?\n>"))
            new = [new_produs,nr_produs]

            produse[len(produse) + 1] = new
            file_rescrie = open("depozit.json", "w")
            file_rescrie.write(json.dumps(produse, indent=4))
            file_rescrie.close()
            print(f"Ai adaugat un nou produse numit  {new_produs} avand un numar de {nr_produs} BUC ")

        elif optiune.lower() == "nu":
            for key in produse:
                print(f"In depozit se  gasesc : {produse[key][0]}")
            opt1 = str(input("Ce  produs adaugi?\n>"))
            opt2 = int(input("In ce cantitate? \n<"))
            for key in produse:
                if produse[key][0]==opt1.lower():
                    produse[key][1] +=opt2
                    print(f"Produsul {produse[key][0]} are {produse[key][1]} BUC")
        else:
            self.msg1()












import meniu
import angajat

# mergem in clasa MENIU
main = meniu.Meniu()

user = main.login()
print(user)
    #returneza lista data de user din meniu.py de la functia login
if user[6] == "manager":
    user_logged = angajat.Manager(user)
    user_logged.menu()

elif user[6] == "operator"  :
    print("Creezi produse cu ceea ce ai in magazie ! ")
    print("*"*30)
    user_logged = angajat.Operator(user)
    user_logged.menu()

elif user[6] == "gestionar" :
    print("Adauti materie prima in materiale.json ! ")
    print("*" * 30)
    user_logged = angajat.Gestionar(user)
    user_logged.menu()
else:
    print("Am iesit !")
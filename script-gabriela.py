import csv
import random
import string

def llegir_dades_csv(nom_arxiu):
    estudiants = []
    with open(nom_arxiu, mode='r', encoding='utf-8') as fitxer:
        lector = csv.DictReader(fitxer)
        for fila in lector:
            estudiants.append(fila)
    return estudiants

def generar_mail(nom, cognoms):
    email =  f"(nom).(cognoms)@insgabrielamistral.cat".lower().replace(" ","")


def generar_contrasenya():   
    caracters = string.ascii_letters + string.punctuation
    contrasenya = "".join(random.choice(caracters) for _ in range(1,11))

#Funcio per fer de deures
def escriure_csv(estudiants, nom_arxiu):
    print("Escriure csv")
    print("dsdasd")


#Exemple d'us del programa
nom_arxiu_entrada = "estudiants_noms.csv"
estudiants = llegir_dades_csv(nom_arxiu_entrada)
for estudiant in estudiants:
    estudiant["email"] = generar_mail(estudiant["nom"], estudiant["cognoms"])
    estudiant["contrasenya"] = generar_contrasenya()

print(estudiants)
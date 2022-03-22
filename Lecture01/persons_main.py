from persons import *

def main():

    #Demo
    doctor1 = Doctor(2,"Johan","Larsson", "Cardiology")
    patient1 = Patient(2,"Nils","Karlsson", condition = 2.0)
    patient2 = Patient(2,"Lina","Zhang", condition = 9.0)


    doctor1.add_patients([patient1,patient2])

    print(doctor1.patients)
    print(patient1.doctor.first_name)

    print(doctor1.last_name)

    print(Person.total_population)
    for patient in doctor1.patients:
        print(patient.condition)

    doctors_data = [[26, "Carl", "Jendle", "Patologi"], (32, "Henrik","Stenbom", "Kardiologi"),(25, "Lina", "Zhang", "Radiology")]

    # TODO - Skapa en lista av doktorer baserat på doctors_data. Det går att göra i en list comprehension med en rad kod!
    # https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480 kan användas

    # Sortera därefter listan av läkare på deras efternamn

    # Gör några patienter och lägg till dem till valfri läkare. Lägg till en funktion hos läkarklassen som tar bort den yngsta patienten
    # från en läkare.
    # 

if __name__ == "__main__":
    main()

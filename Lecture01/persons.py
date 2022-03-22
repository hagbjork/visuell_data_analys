import abc
from typing import List

class Person(metaclass = abc.ABCMeta):
    """
    Abstrakt klass person som vi ärver ifrån.

    Alla personer kommer att ha ålder samt för- och efternamn - vare sig man är läkare eller patient!
    """

    total_population = 0
    @abc.abstractmethod
    def __init__(self, age: int, first_name: str, last_name: str):
        """
        Grundinitialisering för en Person som är en abstrakt klass.
        
        Args in: age - ålder
                 first_name - förnamn
                 last_name - efternamn 
        """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        Person.total_population += 1



class Doctor(Person):
    """Doctor subklass som ärver från Person."""

    def __init__(self, age: int, first_name: str, last_name: str, expertise: str):
        """
        Initfunktion för Doctor som är en subklass av Person.
                Args in: age - ålder
                 first_name - förnamn
                 last_name - efternamn 
        """
        super().__init__(age, first_name, last_name)
        self.expertise = expertise
        self.patients = []

    
    
    def add_patients(self, patients: List[Person])-> None:
        """
        Metod för att lägga till patienter till en läkares rond. Kan ta in antingen en enstaka patient eller en lista med patienter.
        """
        try:
            for patient in patients:
                self.patients.append(patient)
                patient.doctor = self
        except:
            self.patients.append(patients)
            #Sorterar med patienterna med avseende på condition. Varje x svarar mot en patient och vi kan nå
            #alla variabler hos x via detta.
        self.patients = sorted(self.patients, key = lambda x: x.condition)

    def remove_patients(self, patients: List[Person]) -> None:
        """
        Tar bort patienter från en läkare.

        Args in: Patients - en enda patient eller flera patienter som ska tas bort från en läkare

        Returns: None
        """
        try:
            for patient in patients:
                patient.doctor = None
                self.patients.remove(patient)
        except:
            self.patients.remove(patients)




class Patient(Person): 
    """Patientklass som ärver från person. Tillagt är float value condition som avgör hur kritiskt deras tillstånd är."""

    def __init__(self, age: int, first_name: str, last_name: str, condition: float):
        super().__init__(age, first_name, last_name)
        self.condition = condition
        self.doctor = None





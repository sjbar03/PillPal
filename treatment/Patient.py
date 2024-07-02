from Medication import *

class Patient():

    def __init__(self, kwargs):

        self.first_name = kwargs['fname']
        self.last_name = kwargs['lname']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.diseases = kwargs['diseases']
        self.meds: list[tuple[Medication, str]] = []

    def __str__(self):

        builder = ""

        builder += "First Name: " + self.first_name + '\n'
        builder += "Last Name: " + self.last_name + '\n'
        builder += "Age: " + str(self.age) + '\n'
        builder += "Gender: " + ('female' if self.gender else 'male') + '\n'
        builder += "Diseases: " + str(self.diseases) + '\n'
        builder += "Meds: "
        for med in self.meds:
            builder += '\t' + str(med[0]) + " for: " + med[1] + '\n'

        return builder

    def add_med(self, med: Medication):

        self.meds.append(med)

    def meds_to_table(self):

        acc = []

        for med in self.meds:

            m = med[0]
            acc.append([m.brand_name, m.generic_name,med[1], (m.rxcui[0] if (len(m.rxcui) > 0) else "<>")])

        return acc

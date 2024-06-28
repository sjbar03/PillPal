import Medication
import Networking
import random

class Patient():
    
    def __init__(self, name, dob, ins):

        self.name = name
        self.dob = dob
        self.ins = ins
        self.meds = []

    def generate_meds(self, med_base):

        quantity = random.randint(1,15)

        for i in range(quantity):

            term_info = Networking.network.get_term_info(random.choice(med_base)['rxcui']) 
            m = Medication.Medication(term_info)
            self.meds.append(m)

    def meds_to_table(self):

        table = []

        for med in self.meds:

            table.append(med.to_row())
        
        return table


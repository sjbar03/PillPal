from Patient import *
import random

def wnl(string: str):
    loc = string.find('\n')
    if loc != -1:
        return string[:loc].strip()
    else:
        return string.strip()

class PatientPool():

    def __init__(self):

        self.patients = []
        self.populate_disease_base('data/conditions.txt')
        self.populate_fname_bases('data/male_names.txt','data/female_names.txt')
        self.populate_lname_base('data/last_names.txt')

    '''
    Populate this patient pool with diseases.
    '''
    def populate_disease_base(self, filename):

        file = open(filename)

        self.disease_base = []

        for line in file:

            self.disease_base.append(wnl(line))

        file.close()

    '''
    Populate this patient pool with last names.
    '''
    def populate_lname_base(self, filename):

        file = open(filename)

        self.lname_base = []

        for line in file:
            self.lname_base.append(wnl(line))
        
        file.close()

    '''
    Populate this patient pool with first names for both men and women.
    '''
    def populate_fname_bases(self, mfilename, ffilename):

        mfile = open(mfilename)
        ffile = open(ffilename)

        self.mname_base = []
        self.fname_base = []
        
        for line in mfile:

            self.mname_base.append(wnl(line))

        for line in ffile:

            self.fname_base.append(wnl(line))

        mfile.close()
        ffile.close()

    '''
    Randomly generate [ num_patients ] patients with [ num_diseases ] diseases each.
    Default is one patient with between 1 and 6 diseases.
    '''
    def generate_patient(self, num_patients=1, num_diseases=None): 
        
        for i in range(num_patients):

            kwargs = {}

            kwargs['gender'] = random.choice([0,1]) # 1 for female, 0 for male
            kwargs['fname'] = random.choice(self.fname_base if kwargs['gender'] else self.mname_base)
            kwargs['lname'] = random.choice(self.lname_base)
            kwargs['age'] = random.choice(range(14, 100))

            num_diseases = random.choice(range(1, 6))
            diseases = []

            for j in range(num_diseases):
               diseases.append(wnl(random.choice(self.disease_base)))
            
            kwargs['diseases'] = list(set(diseases)) # remove potential duplicates

            self.patients.append(Patient(kwargs))

pool = PatientPool()

pool.generate_patient()

print(str(pool.patients[0]))

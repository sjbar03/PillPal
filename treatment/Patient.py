
class Patient():

    def __init__(self, kwargs):

        self.first_name = kwargs['fname']
        self.last_name = kwargs['lname']
        self.age = kwargs['age']
        self.gender = kwargs['gender']
        self.diseases = kwargs['diseases']
        self.meds = []

    def __str__(self):

        builder = ""

        builder += "First Name: " + self.first_name + '\n'
        builder += "Last Name: " + self.last_name + '\n'
        builder += "Age: " + str(self.age) + '\n'
        builder += "Gender: " + ('female' if self.gender else 'male') + '\n'
        builder += "Diseases: " + str(self.diseases) + '\n'

        return builder

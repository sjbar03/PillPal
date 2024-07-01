import json

class MedBase():

    def __init__(self):

        file = open('/Users/stephenbarlett/Code/PillPal/src/data/med_base.json')
        self.med_base = json.load(file)['data']
        file.close()

base = MedBase()
med_base = base.med_base

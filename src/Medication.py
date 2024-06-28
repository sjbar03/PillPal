class Medication():

    def __init__(self, term_dict):
        
        self.name = term_dict['displayName']
        self.rxcui = term_dict['rxcui']
        self.full_generic = term_dict['fullGenericName']
        self.strength = term_dict['strength']
        self.dose = term_dict['rxnormDoseForm']
        self.brand_name = term_dict['brandName']
        
    def to_row(self):
        if self.brand_name == '':
            brand = '<NO BRAND>'
        else:
            brand = self.brand_name.lower()
        return [self.full_generic.lower(), brand,self.strength.lower(), self.rxcui.lower()]

    def __str__(self):
        
        return self.name

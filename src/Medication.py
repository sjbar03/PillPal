class Medication():

    def __init__(self, term_dict: dict):
        self.ndc = term_dict['product_ndc']
        self.generic = term_dict['generic_name'].lower()
        self.brand = term_dict['brand_name'].upper()
        self.active_ingredients = term_dict["active_ingredients"] if 'active_ingredients' in term_dict else []
        self.pharm_class = term_dict["pharm_class"] if 'pharm_class' in term_dict else []
        self.dosage_form = term_dict['dosage_form'] if 'dosage_form' in term_dict else ""
        
    def to_row(self):
        return [self.brand,
                self.generic,
                self.dosage_form,
                self.ndc]

    def __str__(self):
        
        return self.brand

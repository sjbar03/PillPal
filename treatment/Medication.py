import json

class Medication():

    def __init__(self, med_json):

        self.data = med_json
        self.openfda_data = med_json['openfda']

        self.brand_name = self.openfda_data['brand_name'][0]
        self.generic_name = self.openfda_data['generic_name'][0]
        self.rxcui = self.openfda_data['rxcui'] if 'rxcui' in self.openfda_data else []
        self.route = self.openfda_data['route'][0] if 'route' in self.openfda_data else []

        if 'pharm_class_epc' in self.openfda_data:
            self.pharm_class = self.openfda_data['pharm_class_epc']
        else:
            self.pharm_class = []
            
    def __str__(self):

        return str(self.generic_name)


import requests
import json

class Networking():

    NIH = "https://rxnav.nlm.nih.gov"
    ALL_EXT = "/REST/RxTerms/allconcepts.json"

    OPEN_FDA = 'https://api.fda.gov/drug/ndc.json?/search=brand_name:'

    def term_info(self, rxcui):
        return "/REST/RxTerms/rxcui/" + rxcui + "/allinfo.json"

    def get_drug_info(self, brand):

        resp = requests.get(Networking.OPEN_FDA + brand)

        if resp.ok:
            return resp.content
        else:
            resp.raise_for_status()
        
network = Networking()

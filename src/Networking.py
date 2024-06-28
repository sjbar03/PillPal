import requests
import json

class Networking():

    NIH = "https://rxnav.nlm.nih.gov"
    ALL_EXT = "/REST/RxTerms/allconcepts.json"

    def term_info(self, rxcui):
        return "/REST/RxTerms/rxcui/" + rxcui + "/allinfo.json"

    def update_meds(self):

        resp = requests.get(Networking.NIH + Networking.ALL_EXT)

        if resp.ok:
            return json.loads(resp.content)['minConceptGroup']['minConcept']
        else:
            print(resp.raise_for_status())

    def get_term_info(self, rxcui):

        resp = requests.get(Networking.NIH + self.term_info(rxcui))

        if resp.ok:

            return json.loads(resp.content)['rxtermsProperties']

        else:
            print(resp.raise_for_status())

network = Networking()

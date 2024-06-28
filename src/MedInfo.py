import Networking
import Medication

class MedInfo():

    def __init__(self):

        self.med_base = Networking.network.update_meds()

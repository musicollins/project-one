class IBankFactory:
    
    def get_bank(self, bank_name):
        pass

class DefaultBankFactory:

    def __init__(self):
        self.banks = {}
        banks["swedbank"] = Bank()
    def get_bank(self, bank_name):

class IContainer:

    def get_bank_factory(self):
        pass

    def get_gateway_factory(self):
        pass


class Container(IContainer):
    
    def __init__(self):
        self.bank_factory = None
        self.gateway_factory = None 
        
    def get_bank_factory(self):
        return self.bank_factory

    def set_bank_factory(self, bank_factory):
        self.bank_factory = bank_factory

    def get_gateway_factory(self):
        return self.gateway_factory
    
    def set_gateway_factory(self, gateway_factory):
        self.gateway_factory = gateway_factory


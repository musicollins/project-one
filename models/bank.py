from UI.data_access.customer_da import CustomerDataAccess
from models.customer import Customer



class Bank:
    def __init__(self, data_access : CustomerDataAccess):
        self._name = "Swedbank"
        self._location = "Malmö"
        self._data_access = data_access
        self._customers = self._data_access.getall()
    
    def add_account(self, ssn):
        for cust in self._customers:
            if cust._ssn == ssn:
                cust.add_account()
                print(len(cust._accounts))

        return None


    def get_customers(self):
        customers = self._customers
        return customers
    
    def get_customer_by_ssn(self, ssn):

        for cust in self._customers:
            if cust._ssn == ssn:
                print(cust._name)
                return cust
        return None


    def update_data_source(self):
        customers = []
        for cust in self._customers:
            customers.append(f"{cust._name}:{cust._ssn}:{len(cust._accounts)}")
        self._data_access.update_data(customers)
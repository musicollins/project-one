from data_source.data_source import DataSourceInterface, DataSourceText
from models.customer import Customer

class CustomerDataAccess:
    def __init__(self, data_source : DataSourceInterface):
        self._data_source = data_source

    def update_data(self, data):
        self._data_source.update_data(data)


    def getall(self):
        """
        Deserialize to Python list containing Customer objects
        """
        data = self._data_source.get_data()
        customers = []
        for cust in data.split("\n"):
            customer = cust.split(":")
            name = customer[0]
            ssn = customer[1]
            num_of_accs = customer[2]
            customers.append(Customer(name, ssn))
        ##deserialize to python object
        return customers

    def getbyssn(self, ssn):
        """
        Deserialize to Python list containing customer objects
        filter out the right customer by using its ssn property
        """
        self._datasource.get_data()
        return None
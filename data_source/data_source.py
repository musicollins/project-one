from abc import abstractmethod
import json

class DataSourceInterface:
    @abstractmethod
    def get_data(self):
        pass

class DataSourceText(DataSourceInterface):

    def get_data(self):
            with open('data_source/customers.txt') as f:
                data = f.read()
                return data
    
    def update_data(self, data):
        with open('data_source/customers.txt', 'w') as f:
            f.write('\n'.join(data))
            

class DataSourceJSON(DataSourceInterface):
        def get_data(self):
            print("This data is coming from a JSON file")

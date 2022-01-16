from UI.menu import UI
import json
from container.IContainer import IContainer
from data_source.data_source import DataSourceInterface, DataSourceText, Test
from models.transaction import Transaction


# def app_start(_ui: UI):
#     # ui = _ui
#     # ui.menu()
#     pass


def app_start():
    container = Container()
    container.set_bank_factory( Bank() )
    

    
if __name__ == "__main__":
    app_start()
        # transaction = Transaction(111111, 1001, 200)
        # # print(transaction.__dict__)
        # res_json = json.dumps(transaction.__dict__)
        # print(res_json)



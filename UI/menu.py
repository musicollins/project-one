import os
from UI.data_access.customer_da import CustomerDataAccess
from data_source.data_source import DataSourceText
from models.bank import Bank

class UI:
    def __init__(self):
        self._bank = Bank(data_access=CustomerDataAccess(data_source=DataSourceText()))

    def clear(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def interact_customer_menu(self, cust):
        # self.clear()
        print(f"ID[{cust._id}]\nCustomer name: {cust._name} ## customer ssn: {cust._ssn} ## Accounts: [{len(cust._accounts)}]")
        
        while True:
            print('1 -- CustomerOptions 1')
            print('2 -- CustomerOptions 2')
            print('3 -- CustomerOptions 3')
            print('1 -- Go Back')

            option = int(input())
            
            if option == 1:
                self.clear()
                break
            elif option == 2:
                self.clear()
                print(f"ID[{cust._id}]\nCustomer name: {cust._name} ## customer ssn: {cust._ssn} ## Accounts: [{len(cust._accounts)}]")
            else:
                print('Invalid option. Please enter a number between 1 and 4.')



    def menu(self):
        while True:
            print('1 -- Option 1')
            print('2 -- Option 2')
            print('3 -- Option 3')
            print('9 -- Option 9')
            print('4 -- Exit')

            option = int(input('Enter your choice: '))
            if option == 1:
                self.clear()
                print('Show All \'Customers\'')
                customers = self._bank.get_customers()
                for cust in customers:
                    print(f"ID[{cust._id}]\nCustomer name: {cust._name} ## customer ssn: {cust._ssn} ## Accounts: [{len(cust._accounts)}]")
            elif option == 2:
                self.clear()
                print("Enter Customer's SSN")
                option = input()
                cust = self._bank.get_customer_by_ssn(option)
                if cust != None:
                    self.interact_customer_menu(cust)
                else: print("Customer not found!")
                
            elif option == 3:
                self.clear()
                print('Add \'Account\'')
                user_input = input("Add Customer's SSN\n")
                print(user_input)
                self._bank.add_account(user_input)
            elif option == 4:
                self.clear()
                print('Thanks message before exiting')
                exit()
            elif option == 9:
                self.clear()
                print('Save changes')
                self._bank.update_data_source()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')


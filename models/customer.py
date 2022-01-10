from uuid import uuid4
from models.account import Account

class Customer:

    def __init__(self, name, ssn, accounts):
        self._id = uuid4()
        self._name = name
        self._ssn = ssn
        if accounts == '0':
            self._accounts = []

    def add_account(self):
        self._accounts.append(Account())

        

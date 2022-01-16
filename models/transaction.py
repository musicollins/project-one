from uuid import uuid4
from datetime import date
class Transaction:
    def __init__(self, cust_id, acc_id, amount):
        self.id = 1
        self.cust_id = cust_id
        self.acc_id = acc_id
        self.date = str(date.today())
        self.amount = amount

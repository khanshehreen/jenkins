'''Simple banking application which checks the user balance, its deposits and withdraws'''
class BankAccount():
    '''Main class which has all the methods'''
    def __init__(self, balance=3000):
        '''First method to be implemented which will display user's current balance'''
        self.balance = balance
        #print('\nYour Current bank balance is:', self.balance)
    def deposit(self, amount):
        '''This method will update the main balanceafter user deposists any amount'''
        self.balance += amount
        print('After depositing Rs', amount, 'your balance is', self.balance)
        #return self.balance
    def withdraw(self, amount):
        '''This method will update the main balance after user withdraws any amount'''
        if self.balance >= amount:
            self.balance -= amount
            print('After withdrawing Rs', amount, 'your current balance is', self.balance)
            return self.balance
        return 'Invalid Transaction'
def main():
    '''Main function where we instantiate the class'''
    bank = BankAccount()
    bank.deposit(1000)
    bank.withdraw(500)
main()
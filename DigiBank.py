import random
import csv

class Bank:
    def __init__(self):
        self.choices = {
            'A': 'Open Account',
            'B': 'Deposit',
            'C': 'Withdraw',
            'D': 'Balance'
        }
        self.user_input = ''
        self.validAccountNumber = 0
        self.allData = []

    def open_account(self):
        print("Thank you for choosing our bank, input your name and password")

        self.name = input("Enter name:")

        self.password = input("Hey {} Enter your password:".format(self.name))
        print("Hey {} thank you for choosing our bank your password is {}".format(self.name, self.password))

    def readCsv(self):
        pass


    def deposit(self,amount, account_number):
        # take the amount and account number
        # verify account number
        # update user account with new amount

        amount = amount
        account_number = account_number

        if self.searchUser(account_number):
            #get csv data
            allData = self.getData()
            # print(allData)
            #loop through list
            for account_info in allData:
                if account_number == account_info['accountnumber']:
                    print("OLD ACCOUNT BAL:", account_info['amount'])
                    new_account_balance = amount + int(account_info['amount'])
                    print("NEW ACCOUNT BAL:", new_account_balance)
        else:
            print("incorrect account number")
    def balance(self, account_number):
        #read all data
        all_data = self.getData()
        for data in all_data:
            if account_number == data['accountnumber']:
                print("your balance is {}".format(data['amount']))
                break
        else:
            pass
            # print("account number is not correct")
    def withdraw(self):
        user_account_number = str(input('Enter your account number:'))
        user_password = str(input('Enter your password:'))
        all_data = self.getData()

        for data in all_data:
            if user_account_number == data['accountnumber'] and user_password == data['password']:
                user_amount = int(input('Enter the amount you want to withdraw:'))
                if user_amount < int(data['amount']):
                    acc_bal = int(data['amount']) - user_amount
                    print("Your new balance is {}".format(acc_bal))
                    break
                elif user_amount > int(data['amount']):
                    print("sorry your account balance is insufficient ")
                    break
                else:
                    print('nothing')
        else:
            print("error")








    def genesis(self):
        print('''
        A.{A}
        B.{B}
        C.{C}
        D.{D}'''.format(**self.choices))

        self.user_input = input("what can I help you with Today?choose A,B,C or D:")

        if self.user_input == 'A':
        # OPen Account function here
                self.open_account()
        # print("YEH A")
        elif self.user_input == 'B':
                self.deposit(32011, '11122345')
        # Deposit function here
        #         print("YEH B")
        elif self.user_input == 'C':
        # Withdraw function here
                self.withdraw()
        elif self.user_input == 'D':
            user_balance = str(input("Enter your account number:"))
            self.balance(user_balance)
        # Account Balance function here

        else:
                print("Get outta here Dude")

    # Get user data from csv
    def getData(self, accountnumber=""):

        with open('data.csv') as file_handler:
            bankData = csv.DictReader(file_handler)

            self.allData = [theData for theData in bankData]
            return self.allData

        # if account number is specified
        # if accountnumber:
        #     for user_accountnumber in self.allData:
        #         if accountnumber == user_accountnumber['accountnumber']:
        #             self.allData = user_accountnumber
        #             return self.allData
        # else:
        #     return self.allData
        # print(allData)

    # Search available user account
    def searchUser(self, account_number):
        data_value = self.getData()
        for i in data_value:
            # new_account_number = int(i['accountnumber'])
            if account_number == i['accountnumber']:
                self.validAccountNumber = 1
                break
            else:
                self.validAccountNumber = 0

        return self.validAccountNumber
    def write(self):
        f = open('data.csv', 'w')
        f.write('hi there\n')  # Give your csv text here.
        ## Python will convert \n to os.linesep
        f.close()
        print(f)



# call func
bank = Bank()
bank.genesis()
# bank.write()
# bank.open_account()
# bank.deposit()
# print(bank.searchUser('11122333'))
# bank.deposit('700', '10000')



# check available user
# def checkUser():
#     pass





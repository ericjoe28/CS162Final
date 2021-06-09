# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:38:13 2021

@author: ericj
"""
"""
#**************************************
#Final Project: Bank Simulation
#@Eric Joe Evangelista
#@version CS 161, 03/17/2021
#**************************************
"""
import csv
#BankOperations will print data and calculations are made
class Bank:
    def __init__(self, payment_amt=0, account_info=[]):
        self.payment_amt = payment_amt
        self.account_info = account_info
        self.start_bal = 0
#This function will turn all the data into a list to use in functions below
    def list_info(self, userinfo, acc_type):
        if acc_type == 'S':
            self.account_info.append(userinfo)
            
        elif acc_type == 'C':
            self.account_info.append(userinfo) 
            
        #This function will print all the updated data of the account owners
    def print_account_info(self, acc_num):
        for info in self.account_info:
            print("\nAccount Name: {}". format(info.name))
            print("Date of birth: {}". format(info.dob))
            print("Social Security: XXXX-XX-{}". format(info.ssn))
            print("Phone Number: ({})-{}-{}". format(info.phone_number[0:3], info.phone_number[3:6], info.phone_number[6:10]))
            print("\nBalance: ${:.2f}". format(info.deposit))
#This function will only print the searched account owner's personal details
    def individual_account(self, search_name):
        access = 0
        for info in self.account_info:
            if search_name == info.name:
                access = 1
                print("\nPersonal Details:")
                print("\nAccount Name: {}". format(info.name))
                print("Date of birth: {}". format(info.dob))
                print("Social Security: XXXX-XX-{}". format(info.ssn))
                print("Phone Number: ({})-{}-{}". format(info.phone_number[0:3], info.phone_number[3:6], info.phone_number[6:10]))
                print("\nBalance: ${:.2f}". format(info.deposit))
        if access == 0:
            print("Account Name Does Not Exist!")
#This function will allow the manager to make the client deposit/payment and shows the updated data
    def payment(self, payment_amt, search_name):
        access = 0
        title = "Payment Details:\n"
        title_center = title.center(85)
        print(title_center)
        for info in self.account_info:
            if search_name == info.name:
                info.deposit = info.deposit + payment_amt
                access = 1
                print("Account Name: {}". format(search_name))
                print("Amount Balance: ${:.2f}". format(info.deposit))
        if access == 0:
            print("\nError: Account Does Not Exist!")
            print_menu(new_account)
#This function will allow the manager to charge/deduct the account owners balance
    def charges(self, charge_amt, search_name, manager_pin1):
        access = 0
        title = "Charge Details:\n"
        title_center = title.center(85)
        print(title_center)
        if manager_pin1 == manager_pin:
            print("")
        for acc in self.account_info:
            if search_name == acc.name:
                acc.deposit -= charge_amt
                access = 1
                print("Account Name: {}". format(acc.name))
                print("Charge amount: ${:.2f}". format(charge_amt))
                print("Balance Amount: ${:.2f}". format(acc.deposit))
                if acc.deposit < 0:
                    print("Insufficient Amount")
        if access == 0:
            print("Error: Account Does Not Exist!")
            print_menu(acc)
#This function will close the account of the searched name
    def closing_acc(self, search_name):
        status = 0
        for info in self.account_info:
            if search_name == info.name and info.status == True:
                info.status = False
                self.account_info.remove(info)
                print('\nAccount Has Been CLosed.')
                status = 1
                print()
                break
        if(status == 0):
            print('Account Does Not Exist')
            print_menu(info)
            print()
   
class Accounts(Bank):
    def __init__(self, name, dob, phone_number, ssn, deposit, charge_amt, status):
        Bank.__init__(self, account_info = [], payment_amt = 0)
        self.name = name
        self.dob = dob
        self.phone_number = phone_number
        self.ssn = ssn
        self.deposit = deposit
        self.charge_amt = charge_amt
        self.status = True


 

class Savings(Accounts):
    def __init__(self):
        Accounts.__init__(self, name='xx', dob='xx', phone_number='xx', ssn='xx', deposit=0, charge_amt=0, status=True)
        with open('savings.txt', 'a+') as file:
            file.write(str(self.name) + ' ' + str(self.dob) + ' ' + str(self.phone_number) + ' ' + str(self.deposit) + ' ' + '\n')
        with open('savings.txt', 'r') as read:
            info = read.readlines()
            info.sort()
 

    def print_account_info(self):
        for info in self.account_info:
            print("\nAccount Name: {}". format(info.name))
            print("Date of birth: {}". format(info.dob))
            print("Social Security: XXXX-XX-{}". format(info.ssn))
            print("Phone Number: ({})-{}-{}". format(info.phone_number[0:3], info.phone_number[3:6], info.phone_number[6:10]))
            print("\nBalance: ${:.2f}". format(info.deposit))
        
        
class Checkings(Accounts):
    def __init__(self):
        pass
import random
for i in range(5):
    num = 16
    rand_nums = random.randint(1,9) 
    rand_nums = str(rand_nums)
    nrs = [str(random.randrange(10)) for i in range(num-1)]
    for i in range(len(nrs)):
        rand_nums += str(nrs[i])

#This function will print the menu to allow the manager to choose from
def print_menu(acc):
    customer_account = new_account
    menu = ('\nMENU\n'
        '1 - Create an account\n'
        '2 - Closing an account\n'
        '3 - Make Charges\n'
        '4 - Make Deposit\n'
        '5 - Individual Account Details\n'
        '6 - All Account Details\n'
        'q - Quit\n')
    menuOp = ''
    while(menuOp != 'q'):
        print(menu)
        acc_num = rand_nums
        acc_dict = {}
        menuOp = input('Choose an option:\n')
        while(menuOp != '1' and menuOp != '2' and menuOp != '3' and menuOp != '4' and menuOp != '5' and menuOp != '5' and menuOp != '6' and menuOp != 'q'):
            menuOp = input('Choose an option:\n')
        if(menuOp == '1'):
            try:
                print("Opening an account")
                acc_type = input("Choose Account Type:\n"
                                 "S - Savings\n"
                                 "C - Checkings\n"
                                 "R - Return Main Menu\n").capitalize()
                name = input("Enter first and last name:\n")
                dob = input("Date of birth (mm/dd/yyyy):\n")
                phone_number = input("Mobile number:\n")
                ssn = input("Last 4 digits of SSN:\n")
                deposit = float(input("Enter the amount to deposit:\n"))
            except: len(phone_number) != 10:
                    raise ("\nInvalid Phone Number")
                else:
                    if acc_type == 'S':
                        print("Savings Account Has Been Created! Thank You!")
                        status = True
                        acc_dict.update({name:acc_num})
                        userinfo = Accounts(name, dob, phone_number, ssn, deposit, status, acc_num)
                        customer_account.list_info(userinfo, acc_type)
                
                        
        elif (menuOp == '2'):
            print("Closing Account:\n")
            search_name = input("Enter First and Last Name:\n")
            customer_account.closing_acc(search_name)
        elif (menuOp == '3'):
            manager_pin1 = input("Enter Security Pin:\n")
            search_name = input("Enter first and last name to the account you want to charge:\n")
            charge_amt = float(input("Enter Charge Amount:\n$"))
            customer_account.charges(charge_amt, search_name, manager_pin1)
        elif (menuOp == '4'):
            print("Making Deposits:")
            search_name = input("Enter First and Last Name:\n")
            payment_amt = float(input("Enter the deposit amount:\n$"))
            customer_account.payment(payment_amt, search_name)
        elif (menuOp == '5'):
            print("Search Individual Account Details:")
            search_name = input("Enter First and Last Name:\n")
            customer_account.individual_account(search_name)
        elif (menuOp == '6'):
            title = "All Account Details:"
            title_center = title.center(85)
            print(title_center)
            customer_account.print_account_info(acc_dict)
        elif (menuOp == 'q'):
            break
            
if __name__ == "__main__":
#A password is needed to enter the program
    manager_pin = input("Enter Manager PIN:\n")
    while True:
        if manager_pin == 'Password':
            new_account = Bank(manager_pin)
            print_menu(new_account)
        else:
            print("Invalid Pin")
        manager_pin = input("Enter Manager PIN:\n")
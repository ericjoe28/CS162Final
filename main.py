# -*- coding: utf-8 -*-
"""
#**************************************
#Final Project: Bank Simulation
#@Eric Joe Evangelista
#@version CS 162, 06/09/2021
#**************************************
"""
from accounts import Accounts
from checkings import Checkings
from savings import Savings
from bank import Bank

def print_menu():
    menu = ('\nMENU\n'
        '1 - Create an account\n'
        '2 - Closing an account\n'
        '3 - Make Charges\n'
        '4 - Make Deposit\n'
        '5 - Individual Account Details\n'
        '6 - All Account Details\n'
        '7 - Plot\n'
        'q - Quit\n')
    menuOp = ''
    while(menuOp != 'q'):
        print(menu)
        menuOp = input('Choose an option:\n')
        while(menuOp != '1' and menuOp != '2' and menuOp != '3' and menuOp != '4' and menuOp != '5' and menuOp != '5' and menuOp != '6' and menuOp != '7' and menuOp != 'q'):
            menuOp = input('Choose a  n option:\n')
        if(menuOp == '1'):
            print("Opening an account")
            try:
                acc_type = str(input("Savings or Checkings Account[S/C]: \n")).capitalize()
                if acc_type != 'S' and acc_type != 'C':
                    raise ValueError("Invalid Data Type")
                name = str(input("Enter Full Name: \n") )
                if name is int:
                    raise ValueError("Invalid Data Type")
                dob = input("Date of Birth(xx/xx/xxx): \n")
                phone = input("Phone Number: \n")
                if len(phone) != 10:
                    raise ValueError("Invalid Phone Number")
                ssn = input("Enter Last 4 Digits of SSN: \n")
                deposit = float(input("Enter Deposit Amount: \n"))
                if deposit is str:
                    raise ValueError("Invalid Data Type")
                status = True
                if acc_type == 'S':
                    saving = Savings(name, dob, phone, ssn, deposit, status, acc_type)
                    saving.csv_file_op(acc_type)
                elif acc_type == 'C':    
                    check = Checkings(name, dob, phone, ssn, deposit, status, acc_type)
                    check.csv_file_op(acc_type)
            except ValueError as ve:
                print(ve)
            finally:
                print("\nAccount Has Been Created")
        elif (menuOp == '2'):
            print("Closing Account:\n")
            search_name = input("Enter First and Last Name:\n")
        elif (menuOp == '3'):
            manager_pin = input("Enter Security Pin:\n")
            key = input("Enter first and last name to the account you want to charge:\n")
            charge_amt = float(input("Enter Charge Amount:\n$"))
            charge1 = Accounts(name, dob, phone, ssn, deposit, status, acc_type)
            charge1.charge(manager_pin, charge_amt, acc_type, key)
        elif (menuOp == '4'):
            print("Making Deposits:")
            search_name = input("Enter First and Last Name:\n")
            payment_amt = float(input("Enter the deposit amount:\n$"))
        elif (menuOp == '5'):
            print("Search Individual Account Details:")
            key = input("Enter First and Last Name:\n")
            bankOp = Accounts(name, dob, phone, ssn, deposit, status, acc_type)
            bankOp.linear_search(key, acc_type)
            bankOp.print_info(key, acc_type)
        elif (menuOp == '6'):
            title = "All Account Details:"
            acc_type = input("Enter Account Type[S/C]: ").capitalize()
            title_center = title.center(70)
            print(title_center)
            if acc_type == 'S':
                saving = Savings(name, dob, phone, ssn, deposit, status, acc_type)
                saving.print_checking_info()
            elif acc_type == 'C':
                checkin = Checkings(name, dob, phone, ssn, deposit, status, acc_type)
                checkin.print_checking_info()
        elif(menuOp) == '7':
            print_plot = Accounts(name, dob, phone, ssn, deposit, status, acc_type)
            print_plot.plot()
        elif (menuOp == 'q'):
            break

  
if __name__ == "__main__":
    manager_pin = input("Enter Manager PIN:\n")
    while True:
        if manager_pin == 'Password':
            print_menu()
        else:
            print("Invalid Pin")
        manager_pin = input("Enter Manager PIN:\n")
   
            
        
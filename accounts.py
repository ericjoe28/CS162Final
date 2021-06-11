# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:24:42 2021

@author: ericj
"""
from bank import Bank
import pie
import csv
class Accounts(Bank):
    def __init__(self, name, dob, phone, ssn, deposit, status, acc_type):
        Bank.__init__(self, name, dob, phone, ssn, deposit, status, acc_type)

    def close_acc(self):
        pass
    def plot(self):
        pie.PieChart()
    def sort(self):
        pass   
    def linear_search(self, key, acc_type): 
        if acc_type == 'S':
            with open('savings.csv', 'r') as csvfile_saving:
                saving_reader = csv.reader(csvfile_saving, delimiter=',')
                for i in saving_reader:
                    if key in i:
                        return i
        elif acc_type == 'C':
            with open('checkings.csv', 'r') as csvfile_saving:
                saving_reader = csv.reader(csvfile_saving, delimiter=',')
                for i in saving_reader:
                    if key in i:
                        return i
        else:
            print("Not Found")
            
    def print_info(self, key, acc_type):
        if acc_type == 'S':
            found = self.linear_search(key, acc_type)
            names = found[0]
            dobs = found[1]
            phones = found[2]
            ssn_num = found[3]
            deposits = found[4]
            print(format("Name", "<13s"), format("Date of Birth", "<13s"),\
                 format("Phone Number", "<13s"), format("SSN", "<13s"),\
                 format("Balance $$", "<13s"), format("Account Type:", "<13s"))
            print(format(names, "<13s"), format(dobs, "<13s"),\
                 format(phones, "<13s"), format(ssn_num, "<13s"),\
                 format(deposits, "<13s"), format(self.acc_type + "avings", "<13s"))
    def charge(self, key, acc_type, manager_pin, charge_amt):
        access = 0
        title = "Charge Details:\n"
        title_center = title.center(85)
        print(title_center)
        if manager_pin == 'Password':
            print("")
            acc_charge = self.linear_search(key, acc_type)
            names = acc_charge[0]
            deposits = float(acc_charge[4])
            deposits -= charge_amt
            access = 1
            print("Account Name: {}". format(names))
            print("Charge amount: ${:.2f}". format(charge_amt))
            print("Balance Amount: ${:.2f}". format(deposits))
        elif access == 0:
            print("Error: Account Does Not Exist!")
            
    


        
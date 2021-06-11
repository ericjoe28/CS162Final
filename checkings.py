# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:26:21 2021

@author: ericj
"""
import csv
from accounts import Accounts
class Checkings(Accounts):
    def __init__(self, name, dob, phone_number, ssn, deposit, status, acc_type):
        Accounts.__init__(self, name, dob, phone_number, ssn, deposit, status, acc_type)
    def print_checking_info(self):
        print('Account Type: Checkings:')
        with open('checkings.csv', 'r') as csvfile:
            checkings_reader = csv.reader(csvfile, delimiter=',')
            print(format("Full Names:", "<13s"), format("Date of Birth", "<13s"),\
                 format("Phone Numbers:", "<13s"), format("SSN", "<13s"),\
                      format("Balance $$", "<13s"), format("Account Type:"))
            for i in checkings_reader:
                names = i[0]
                dobs = i[1]
                phone = i[2]
                ssn_num = i[3]
                deposit = i[4]
                print(format(names, "<13s"), format(dobs, "<13s"),\
                      format(phone, "<13s"), format(ssn_num, "<13s"),\
                      format(deposit, "<13s"), format(self.acc_type + 'heckings', "<13s"))
              
        
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:24:42 2021

@author: ericj
"""
import csv
from accounts import Accounts
class Savings(Accounts):
    def __init__(self, full_name, dob, phone, ssn, deposit, acc_type, status):
        Accounts.__init__(self, full_name, dob, phone, ssn, deposit, acc_type, status)
    def userinfo_list(self):
        pass
    def print_checking_info(self):
        print('Account Type: Savings')
        with open('savings.csv', 'r') as csvfile:
            checkings_reader = csv.reader(csvfile, delimiter=',')
            print(format("Name", "<13s"), format("Date of Birth", "<13s"),\
                 format("Phone Number", "<13s"), format("SSN", "<13s"),\
                      format("Balance $$", "<13s"), format("Account Type:", "<13s"))
            print()
            for i in checkings_reader:
                names = i[0]
                dobs = i[1]
                phone = i[2]
                ssn_num = i[3]
                deposit = i[4]
                print(format(names, "<13s"), format(dobs, "<13s"),\
                      format(phone, "<13s"), format(ssn_num, "<13s"),\
                      format(deposit, "<13s"), format(self.acc_type + "avings", "<13s"))
        
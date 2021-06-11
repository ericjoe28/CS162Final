# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:24:42 2021

@author: ericj
"""

class Bank:
    def __init__(self, full_name, dob, phone, ssn, deposit, status, acc_type):
        self.full_name = full_name
        self.dob = dob
        self.phone = phone
        self.ssn = ssn
        self.deposit = deposit
        self.status = status
        self.data_info_list = []
        self.acc_type = acc_type
        
    def userinfo_list(self):
        self.data_info_list = [self.full_name, self.dob, self.phone,self.ssn,self.deposit]
        return self.data_info_list
    def csv_file_op(self, acc_type):   
        if acc_type == 'S':
            with open('savings.csv', 'a+') as file:
                file.write(str(self.full_name) + ',' + str(self.dob) + ',' + str(self.phone) + ',' + str(self.ssn) + ',' + str(self.deposit) + '\n')

        elif acc_type == 'C':
            with open('checkings.csv', 'a+') as file:
                file.write(str(self.full_name) + ',' + str(self.dob) + ',' + str(self.phone) + ',' + str(self.ssn) + ',' + str(self.deposit) + '\n')

    
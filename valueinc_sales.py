# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:19:44 2022

@author: meyna
"""

import pandas as pd

#file_name = pd.read_csv("file.csv")

#data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv",sep=";")

#summary of the data
data.info()

#working with calculations
#defining variables

CostPerItem = 11.73
SelPrice = 21.1
NumPurch = 6

Profit = SelPrice - CostPerItem
ProfirPerTrans = Profit*NumPurch
CostPerTrans = NumPurch*CostPerItem
SelPricePerTrans = NumPurch*SelPrice

#CostPerTransaction
#variable = data_name('column_name')

CostPerItem = data['CostPerItem']
NumPurch = data['NumberOfItemsPurchased']
CostPerTrans = NumPurch*CostPerItem

#add new column
data['CostPerTransaction'] = CostPerTrans

#sales per transaction
SelPrice = data['SellingPricePerItem']
SelPricePerTrans = NumPurch*SelPrice

data['SalesPerTransaction']=SelPricePerTrans

#profit
data['ProfitPerTransaction']=data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

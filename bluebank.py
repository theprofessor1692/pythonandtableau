# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 11:01:52 2022

@author: meyna
"""

import json
import pandas as pd
import numpy as np
# matplotlib.pyplot as plt

#method 1 to read json files
json_file = open('loan_data_json.json')
data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data)

#findign unique values
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income










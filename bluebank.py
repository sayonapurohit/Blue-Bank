# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:33:31 2022

@author: sayon
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#method 2 to read json data
with open('loan_data_json.json') as json_file:
          data = json.load(json_file)
          
#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describing the data
loandata.describe()

#describe the data for sepcific column
loandata['int.rate'].describe
loandata['fico'].describe
loandata['dti'].describe

#using EXP() to get the annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

#FICO Score

fico = 250
# fico >= 300 and < 400 - 'Very Poor'
# fico >= 400 and ficoscore < 600 - 'Poor'
# fico >= 601 and ficoscore < 660 - 'Fair'
# fico >= 660 and ficoscore < 780 - 'Good'
# fico >=780 - 'Excellent'

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 600 and fico < 700:
    ficocat = 'Good'
elif fico >= 700:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown' 
print(ficocat)

#applying for loops to loan data
#using furst 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good' 
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

#df.loc as conditional statements
# df.loc[df[columnname]condition, newcolumnname] = 'value if the condition is met'

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category
#plots

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'green',  width = 0.2)
plt.show()

#scatter plots

xpoint = loandata['annualincome']
ypoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

#writing to csv
loandata.to_csv('loan_cleaned.csv',index = True)

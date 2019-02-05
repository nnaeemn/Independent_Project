#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:46:03 2019

@author: naeemnowrouzi
"""

import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
sns.set(color_codes=True)


import os
os.getcwd()
os.chdir('/Users/naeemnowrouzi/Desktop/TDIChallenge')
#os.listdir()

# Prepare for Merge
data_0 = pd.DataFrame(pd.read_csv('./all_inventors.csv', dtype={'application_number': np.int64}))
data_1 = pd.DataFrame(pd.read_csv('./application_data.csv', dtype={'application_number' : np.str}))
data_2 = pd.DataFrame(pd.read_csv('./correspondence_address.csv'))


data_11 = data_1[~data_1.application_number.str.startswith('PCT')]
data_11.application_number = pd.to_numeric(data_11.application_number)
data_11.dtypes
data_0.dtypes

# Merge
merged_data = pd.merge(data_0, data_11, on='application_number')
merged_data = pd.DataFrame(merged_data)
# Convert date-time from object to datettime type.
merged_data.filing_date = merged_data.filing_date.astype(str)
merged_data.filing_date = pd.to_datetime(merged_data.filing_date)

merged_data.filing_date.max()


# plot cummulative number of inventors in 5 states

 #filing_dates = pd.DatetimeIndex(merged_data.filing_date)
 #merged_data.groupby('inventor_region_code').size()

from matplotlib import pyplot as pl
state_totals_cummul = {'New York' : data_0.inventor_region_code[data_0.inventor_region_code == 'NY'].shape[0],
          'New Jersey' : data_0.inventor_region_code[data_0.inventor_region_code == 'NJ'].shape[0],
          'California' : data_0.inventor_region_code[data_0.inventor_region_code == 'CA'].shape[0], 
          'Massachusetts' : data_0.inventor_region_code[data_0.inventor_region_code == 'MA'].shape[0],
          'Texas' : data_0.inventor_region_code[data_0.inventor_region_code == 'TX'].shape[0],
          'Florida' : data_0.inventor_region_code[data_0.inventor_region_code == 'FL'].shape[0]
          }
X = np.arange(len(state_totals_cummul))
pl.bar(X, state_totals_cummul.values(), align='center', width=0.5)
pl.xticks(X, state_totals_cummul.keys())

ymax = max(state_totals_cummul.values()) + 500000
pl.ylim(0, ymax)
pl.title('Total Number of Patent Applicants (Inventors) from 1931 - 2018')
pl.show()
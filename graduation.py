# Graduation rates and dropout rates

import sys
import pandas as pd
import urllib.request as request

# Download the file
request.urlretrieve('http://cps.edu/Performance/Documents/DataFiles/Metrics_CohortGraduationDropout_SchoolLevel_2017.xls', 'DATA/raw_graduation.xls')

'''
Format of the xls file:
* Data are in the sheet [School 5 Year Cohort Rates]
* The first row is just the title, so ignore it.
* The second row is the column names
* Cells with no values have a space character " ".
* There are multiple columns but we only need column 0 (School ID) and 16 (Graduation Rate)
'''

# Import raw csv data with all schools
data = pd.read_excel('DATA/raw_graduation.xls', sheet_name='School 5 Year Cohort Rates',
    header=0, skiprows=1, usecols=[0,16], na_values=" ")

data.dropna().to_csv('DATA/refined_graduation.csv', index=False)

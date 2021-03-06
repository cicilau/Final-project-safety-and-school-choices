import sys
import pandas as pd
import urllib.request as request

# Download the file
request.urlretrieve('http://cps.edu/Performance/Documents/Datafiles/CollegeEnrollPersist_2016_SchoolLevel.xls', 'DATA/raw_college.xls')

'''
Format of the xls file:
* Data are in the sheet [collenrollpersist_rpt_20160914]
* The first row is just the title, so ignore it.
* The second row is the column names
* Cells with no values have a space character "*".
* Multiple columns contain data for different school years, but we need the closest one only
* There are multiple columns but we only need column 0 (School ID) and 4 (Enrollment Pct of SY2015)
'''


# Import raw csv data with all schools
data = pd.read_excel('DATA/raw_college.xls', sheet_name='School 5 Year Cohort Rates',
    header=0, skiprows=1, usecols=[0,4], na_values="*")

data.dropna().to_csv('DATA/refined_college.csv', index=False)

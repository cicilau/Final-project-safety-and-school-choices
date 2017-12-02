import sys
import pandas as pd
import urllib.request as request

# Download the file
request.urlretrieve('http://cps.edu/Performance/Documents/Datafiles/CollegeEnrollPersist_2016_SchoolLevel.xls', 'DATA/raw_college.xls')

# Import raw csv data with all schools
data = pd.read_excel('DATA/raw_college.xls', sheet_name='School 5 Year Cohort Rates',
    header=0, skiprows=1, usecols=[0,4], na_values="*")

data.dropna().to_csv('DATA/refined_college.csv', index=False)

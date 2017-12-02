# Neighborhood Safety and High School Performances
Final Project for Introduction to Programming 

Xiaofan Liu, Yuewen Ding
12/1/2017

### PART I. The Question
Students’ decisions making process on future education is influenced by a combination of factors, including but not limited to their past academic achievements, quality of schools, interests and external environment. There are numerous studies on school choices. The 5Essentials Reports for CPS draw from the 2016 My Voice, My School Student and Teacher Surveys, which are administered in collaboration with The University of Chicago Consortium on Chicago School Research (CCSR), clearly stated that schools that score strongly on such measures as supportive environment (including safety) are much more likely to improve academic achievement for their students. 

The target of this project is to explore the correlations between academic performances and the safety of schools’ locations for Chicago public high schools.  We plotted different academic factors and safety levels on maps to investigate clustering patterns, tested the correlations between total number of crimes near the school and different academic factors, and further broke data down by types of crimes to test relationships with different academic factors.  


#### Past Work
In terms of school choice, based on a survey conducted in Ohio region, safety is the top one concern when choosing schools for their children. Another survey of survey the D.C. Opportunity Scholarship Program showed the similar results: parents and children names safety top consideration, regardless of their ethnicities or ages ( **[`Stewart and Wolf, 2016`](http://educationnext.org/power-to-the-people-the-school-choice-journey-review-stewart-wolf/)** ). In terms of school performance, a study conduct in Florida showed that  a 1 percentage point increase in a school’s mean school safety score increases a school’s FCAT score by 18 points, on average (Christopher Duszka, 2015). Not to mention the research on 5Essentials reports  is a clear statement on importance of safety. 


### PART II. Data sources
Check-out scripts for the data in this analysis can be found in my **The folder [`DATA`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/DATA)**  repository.
Check-out list of contents in  **file [`Contents List.md`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/Contents_List.md)** 
The performance data are from several different portals but they are all from Chicago Public Schools (CPS) originally. CPS assign each school a unique School ID in all different data sets and studies, so it helps us combine variables from multiple files by matching the School ID.

#### 1.High Schools locations and their safety level
We are using data of performance of public schools in chicago from file Chicago Public Schools-School Progress Reports SY1617, downloaded from city of Chicago data portal(https://data.cityofchicago.org/Education/Chicago-Public-Schools-School-Progress-Reports-SY1/cp7s-7gxg). 

We selected 5 variables: "School_ID','Short_Name', 'Safety_Level', 'School_Latitude', and'School_Longitude', gave values of 1 to 5 to safety levels of 'very weak', 'weak', 'neutral', 'strong' and 'very strong', dropped schools with 'not enough data', and saved these as refined_progress.csv. 

Check-out codes in  **file [`progress_report.py`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/progress_report.py)** 

#### 2.High Schools Performance
We downloaded average ACT scores on school level from year 2001 to year 2016 and selected only 'school ID', 'Year' and 'Composite'(ACT scores). Similarly from cps.edu, we downloaded 'CPS Graduates College Enrollment/Persistence by School for 2010-2015' for college enrollment rate, 'School 5 Year Cohort Rates' for cohort dropout rates and graduation rates, and converted SQRP(School Overall Rating Policy) levels from 'level 3', 'level 2', 'level 2+', 'level 2', 'level 1' and 'level 1+' to 1 to 5. 

Check-out codes in  **file [`act.py`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/act.py)** , **file [`graduation.py`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/graduation.py)**, **file [`college.py`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/college.py)**, and  **file [`rating.py`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/rating.py)**

#### 3. Crime records
Crime data are from City of Chicago Data Portal. We downloaded the data sets for 2016 and 2017 to cover the 2016 school year and selected “Case ID”, “Crime Type”, “Latitude” and “Longitude”. The key to this project is matching the crime data to schools to reflect the safety conditions of the neighborhood around. Here we used the number of crime cases within 1km distance to the school as the variable. Therefore, We mapped the criminal cases to schools with their latitudes and longitude. 

Check-out codes in  **file [`map_crime.py`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/map_crime.py)** 

#### 4.Merging data
The numbers of criminal cases happend in each school's neighborhood were counted based on distance to school's location( “Latitude” and “Longitude” ) and added as a new column to the final data table. We paired up datasets above on 'School ID' to put all data needed in to a final data table called data_table.csv.

Check-out codes in  **file [`finalize_data.py`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/finalize_data.py)** 

### PART III. Investigation

#### 1.Summary of data
We analyzed 181 high schools from CPS in total. The following graphs show the distributions of SQRP level, safety level, average ACT scores, graduation rate, and college enrollment rate. 

<img src="data_analyze/output_5_0.png" width="49%"> <img src="data_analyze/output_6_0.png" width="49%">
<img src="data_analyze/output_5_1.png" width="49%"> <img src="data_analyze/output_6_1.png" width="49%">

<img src="data_analyze/output_8_0.png" width="32%"> <img src="data_analyze/output_9_0.png" width="32%"> <img src="data_analyze/output_10_0.png" width="32%">




### Step 2: Download School Performace Data

On each page, the variables are within DIV elements with different CSS class names. We checked the source code of the web page, and extract the information based on such characteristics. The PYTHON code is written looping over all links and extract the information to make a CSV table.
```
step1_school_list.py
```
And this code is to finish three tasks:
* Download a web page from links in **data/school_links.txt**
* Parse the web page and find all variables that we need
* Write out variables in the CSV table format at **data/school_performance.csv**.

### Step 3: Process of State Crime Data and Correlation Analysis

Download the raw data file and save it at **data/crime_states.csv**

### Step 4: Process of City Crime Data and Correlation Analysis

Download the raw data files and save them at **data/crime_XX.csv** (XX are for CA, MA, NY, IL)

### Step 5: Process of District Crime Data and Correlation Analysis

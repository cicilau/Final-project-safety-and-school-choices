## Final Project for Introduction to Programming 
# Neighborhood Safety and High School Performances

### The Question


### Past Work

### Data sources
Check-out scripts for the data in this analysis can be found in my **The folder [`data`](https://github.com/yuewending/PPHA30550_Final_Project/tree/master/data)**  repository.
Check-out list of contents for DATA folder in  **file [`0intro.md`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/DATA/0intro.md)** 

#### 1.High Schools locations and their safety level
We are using data of performance of public schools in chicago from file Chicago Public Schools-School Progress Reports SY1617, downloaded from city of Chicago data portal(https://data.cityofchicago.org/Education/Chicago-Public-Schools-School-Progress-Reports-SY1/cp7s-7gxg). 
We selected 5 variables: "School_ID','Short_Name', 'Safety_Level', 'School_Latitude', and'School_Longitude', gave values of 1 to 5 to safety levels of 'very weak', 'weak', 'neutral', 'strong' and 'very strong', dropped schools with 'not enough data', and saved these as refined_progress.csv. 



Check-out list of contents for DATA folder in  **file [`0intro.md`](https://github.com/cicilau/Final-project-safety-and-school-choices/tree/master/DATA/0intro.md)** 


#### Crime Rates

Crime rates are obtained at three levels (resolutions): state, city and district.

* **State** crime rates are from **Uniform Crime Reporting (UCR) Statistics** https://www.ucrdatatool.gov/ with the "state and national estimates" data portal for the year 2014. The CSV formatted raw data file is downloaded manually.

* **City** crime rates are also from **URC Statistics** https://www.ucrdatatool.gov/ with the "Local law enforcement agencies" data portal for the year 2014. Cities of four states (NY, MA, CA, IL) are used for this study. The CSV formatted raw data file is downloaded manually.

* **District** crime rates are obtained for four cities (New York City, Chicago, Boston, Los angeles) with different city data portals.
  * New York City
  * Chicago
  * Boston
  * Los angeles
  
### Investigation

### Step 1: Obtaining List of US High Schools

There's no direct export of table or database file from the greatshools.org, instead, the variables of each school are provided in a seperated page. The links are in the format of "/texas/lubbock/19361-Canyon-Lakes/" combined with the state name, city name, an internal ID and the school name. Therefore, we need to obtain the list of URL links of the schools we care for.

The list can be obtained via its search engine via the GET method. (https://www.greatschools.org/search/search.page) For this project, we select all public high school for the filtering (private school data are not provided). The results from the search are paged, so we need to first obtain the number of pages, and then query the page one by one, and finally extract the school links from each result page. The PYTHON code is written in,
```
step1_school_list.py
```
And this code is to finish four tasks:
* Get the number of pages from the search
* Download all HTML pages
* Obtain school links based on the CSS class name
* Dump all links in the file **data/school_links.txt**

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

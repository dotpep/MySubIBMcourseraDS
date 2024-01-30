import pandas as pd
import requests
from bs4 import BeautifulSoup

"""What is read_html in pandas library?¶
pd.read_html(url) is a function provided by the pandas library in Python 
that is used to extract tables from HTML web pages. 
It takes in a URL as input and returns a list of all the tables found on the webpage.
"""

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

# read_html_pandas_data = pd.read_html(url)
# read_html_pandas_data

# convert the BeautifulSoup object to a string
read_html_pandas_data = pd.read_html(str(soup))

# Because there is only one table on the page, we just take the first table in the list returned
netflix_dataframe = read_html_pandas_data[0]
print(netflix_dataframe.head(5))

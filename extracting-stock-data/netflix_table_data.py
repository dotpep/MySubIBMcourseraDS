import pandas as pd
import requests
from bs4 import BeautifulSoup

"""html5lib and lxml
html5lib is a Python library used for parsing HTML documents and producing a parse tree that closely resembles the HTML input. lxml is a Python library used for processing XML and HTML documents, and provides a very simple and powerful API for parsing and manipulating these documents.
"""
"""difference between: webscraping vs scraping vs parsing
Web scraping is the process of extracting data from websites using code. Scraping refers to the process of extracting data from any source, not just websites. Parsing refers to the process of analyzing a string of symbols according to the rules of a formal grammar.
"""

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

netflix_data = pd.DataFrame()

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all('td')
    date  = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # AttributeError: 'DataFrame' object has no attribute 'append'. Did you mean: '_append'?
    # use concat pandas function to add new row to the dataframe without using .append

    # netflix_data = pd.concat([netflix_data, pd.DataFrame({'Date': date, 'Open': Open, 'High': high, 'Low': low, 'Close': close, 'Volume': volume})], ignore_index=True)
    # ValueError: If using all scalar values, you must pass an index to pd.DataFrame or pd.Series
    netflix_data = pd.concat([netflix_data, pd.DataFrame({'Date': date,
                                                          'Open': Open,
                                                          'High': high,
                                                          'Low': low,
                                                          'Close': close,
                                                          'Volume': volume}, index=[0])], ignore_index=True)

    # netflix_data = netflix_data.append({'Date': date, 'Open': Open, 'High': high, 'Low': low, 'Close': close, 'Volume': volume}, ignore_index=True)



print(netflix_data.head())

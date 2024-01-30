import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

data = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')

# print(soup.prettify())
# print(soup.title.text)
# print(soup.title)

# print(soup.title.parent.name)
# print(soup.title.string)

amazon_data = pd.DataFrame()

for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date  = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    amazon_data = pd.concat([amazon_data, pd.DataFrame({'Date': date,
                                                          'Open': Open,
                                                          'High': high,
                                                          'Low': low,
                                                          'Close': close,
                                                          'Volume': volume}, index=[0])], ignore_index=True)


# print(amazon_data[0:6])
# print(amazon_data.shape)
print(amazon_data.head(5))

# What is the name of the columns of the dataframe?
# print(amazon_data.columns)

# print(amazon_data.columns[-1])

# What is the Open of the last row of the amazon_data dataframe?
# print(amazon_data.iloc[[-1], [1]])
# What is the Open of the first row of the amazon_data dataframe?
# print(amazon_data.iloc[0, 1])

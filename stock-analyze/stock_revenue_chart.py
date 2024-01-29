import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# Tesla

tesla = yf.Ticker("TSLA")

tesla_hist = tesla.history(period="max")
tesla_data = pd.DataFrame(tesla_hist)

tesla_data.reset_index(inplace=True)
tesla_data.head(5)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
data = requests.get(url)
html_data = data.text
beautiful_soup = BeautifulSoup(html_data, "html.parser")

# Using BeautifulSoup or the read_html function extract the table with Tesla Quarterly Revenue and store it into a dataframe named tesla_revenue. The dataframe should have columns Date and Revenue.
"""
tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in beautiful_soup.find("tbody").find_all("tr"):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    tesla_revenue = tesla_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)
"""

tesla_revenue = pd.DataFrame()
for row in beautiful_soup.find("tbody").find_all("tr"):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text

    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date": date, "Revenue": revenue}, index=[0])], ignore_index=True)


# print(tesla_revenue.head())
# print(tesla_revenue.tail())

# Execute the following line to remove the comma and dollar sign from the Revenue column.
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",", "").str.replace("$", "")

# Execute the following lines to remove an null or empty strings in the Revenue column.
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# print(tesla_revenue.head())
# print(tesla_revenue.tail())



# GameStop
game_stop = yf.Ticker("GME")

gme_hist = game_stop.history(period="max")
gme_data = pd.DataFrame(gme_hist)

gme_data.reset_index(inplace=True)
gme_data.head()

# print(gme_data.tail())

data = requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html")
html_data = data.text

soup = BeautifulSoup(html_data, "html.parser")

# gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
gme_revenue = pd.DataFrame()

for row in beautiful_soup.find("tbody").find_all("tr"):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text.replace("$", "").replace(",", "")

    # gme_revenue = gme_revenue.append({"Date": date, "Revenue": revenue}, ignore_index=True)
    gme_revenue = pd.concat([gme_revenue, pd.DataFrame({"Date": date, "Revenue": revenue}, index=[0])], ignore_index=True)

# print(gme_revenue.head())
# print(gme_revenue.tail())

make_graph(tesla_data, tesla_revenue, 'Tesla')
make_graph(gme_data, gme_revenue, 'GameStop')

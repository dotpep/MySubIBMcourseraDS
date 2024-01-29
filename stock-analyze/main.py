import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

from make_graph import make_graph


def get_stock_data(stock_ticker: str) -> pd.DataFrame:
    stock = yf.Ticker(stock_ticker)

    stock_history = stock.history(period="max")
    stock_data = pd.DataFrame(stock_history)

    stock_data.reset_index(inplace=True)
    stock_data.head(5)
    return stock_data


def get_stock_revenue(beauti_html: BeautifulSoup) -> pd.DataFrame:
    stock_revenue = pd.DataFrame()

    for row in beauti_html.find("tbody").find_all("tr"):
        col = row.find_all('td')
        date = col[0].text
        revenue = col[1].text.replace("$", "").replace(",", "")

        stock_revenue = pd.concat([stock_revenue, pd.DataFrame({"Date": date, "Revenue": revenue}, index=[0])], ignore_index=True)

    return stock_revenue


def validate_stock_revenue_data(stock_revenue: pd.DataFrame) -> pd.DataFrame:
    stock_revenue["Revenue"] = stock_revenue["Revenue"].str.replace(",", "").str.replace("$", "")
    stock_revenue.dropna(inplace=True)
    stock_revenue = stock_revenue[stock_revenue["Revenue"] != ""]
    return stock_revenue


def get_data(url: str) -> BeautifulSoup:
    data = requests.get(url)
    html_data = data.text
    beauti_html = BeautifulSoup(html_data, "html.parser")
    return beauti_html


def main():
    gamestop_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
    gamestop_beauti_html = get_data(url=gamestop_url)
    gamestop_data = get_stock_data(stock_ticker="GME")
    gamestop_revenue = get_stock_revenue(beauti_html=gamestop_beauti_html)
    validated_gamestop_revenue = validate_stock_revenue_data(stock_revenue=gamestop_revenue)
    make_graph(gamestop_data, validated_gamestop_revenue, 'GameStop')
    
    
    tesla_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
    tesla_beauti_html = get_data(url=tesla_url)
    tesla_data = get_stock_data(stock_ticker="TSLA")
    tesla_revenue = get_stock_revenue(beauti_html=tesla_beauti_html)
    validated_tesla_revenue = validate_stock_revenue_data(stock_revenue=tesla_revenue)
    make_graph(tesla_data, validated_tesla_revenue, 'Tesla')
    
    
    
if __name__ == '__main__':
    main()
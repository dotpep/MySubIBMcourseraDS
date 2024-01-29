import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

apple = yf.Ticker("AAPL")

"""jupyter notebook
Yes, you can download a JSON file from a URL using the command line. The wget command can be used in the command prompt or terminal to download files from the internet. However, the !wget command is specific to Jupyter notebooks and may not work in the command line. To download a JSON file using wget in the command line, use the following command: wget <url> where <url> is the URL of the JSON file you want to download. Make sure you have an active internet connection and that you have the necessary permissions to write to the current working directory.
"""
"""cmd 
To download the JSON file from the provided URL in PyCharm terminal using curl, use the following command: curl -o apple.json https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json. This will download the file and save it with the name apple.json in the current working directory. Make sure you have an active internet connection and that you have the necessary permissions to write to the current working directory.
"""

with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable
    # print("Type: ", type(apple_info))

apple_info['country']


apple_share_price_data = apple.history(period="max")
print(apple_share_price_data.head())

"""
The reset_index method is a Pandas method used to reset the index of a DataFrame. The index is a way to label and identify the rows in a DataFrame, and it can be useful to reset the index if you want to make the index into a column or if you want to create a new index for the DataFrame. The inplace=True argument tells Pandas to modify the original DataFrame instead of returning a new DataFrame with the reset index. You can use reset_index whenever you need to reset the index of a DataFrame, such as when you want to create a new index or when the current index is not useful for your analysis. It's important to note that reset_index does not modify the data in the DataFrame, only the index labels.
"""
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")


print(apple.dividends)
# apple.dividends.plot()
"""
The output Axes(0.125,0.2;0.775x0.68) indicates that the plot was created successfully. To display the plot, you can add the following line of code after calling the plot method: plt.show(). This will open a separate window displaying the plot. If you want to display the plot inline in your PyCharm console, you can add the following line of code before calling the plot method: %matplotlib inline. Then, after calling the plot method, you can simply run the script and the plot will be displayed inline in your console.
"""
plt.show()


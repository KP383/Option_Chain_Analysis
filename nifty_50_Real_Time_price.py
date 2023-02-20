import requests
from bs4 import BeautifulSoup
import pandas as pd
from string_formatter import string_formatter_value, string_formatter_value_strike,string_formatter_percen, string_formatter_mix, string_formatter_value_nl, string_formatter_mix_nl

def get_current_N50():
    url = "https://www.icicidirect.com/share-market-today/indices/nse/nifty-50/20559"
    data = requests.get(url).text
    Parse = BeautifulSoup(data, features="html.parser")

    current_price = Parse.find("h2", class_="share_amt").text
    current_price_N50 = string_formatter_value_nl(current_price)

#     print(current_price_N50)

    current_price = (Parse.find("p", class_="chg_value").text)[5:]
#     print(current_price)

    N50_change = string_formatter_mix_nl(current_price)
    N50_change_value = N50_change[0]
    N50_change_percen = N50_change[1]

#     print(N50_change_value)
#     print(N50_change_percen)
    return (current_price_N50, N50_change_value, N50_change_percen)

# print(get_current_N50())

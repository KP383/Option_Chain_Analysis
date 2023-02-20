''' 
list of functions :
1) get_OPC_data_ICICID
2) get_OPC_data_groww
3) show_OPC_ICICD
4) show_OPC_GROWW
5) get_pcr
'''

# add for example
import requests
from bs4 import BeautifulSoup
import pandas as pd
from string_formatter import string_formatter_value, string_formatter_value_strike,string_formatter_percen, string_formatter_mix, string_formatter_value_nl, string_formatter_mix_nl

def get_OPC_data_ICICID():
    
    url = "https://www.icicidirect.com/futures-and-options/nifty-option-chain/"
    data = requests.get(url).text
    Parse = BeautifulSoup(data, features="html.parser")
    
    ltp = Parse.find_all("div", class_="ltp")
    ltp= ltp[2:]
    C_LTP = []
    P_LTP = []
    for i in range(0, len(ltp), 2):
        C_LTP.append(float(ltp[i].text))
        P_LTP.append(float(ltp[i+1].text))
    
    ltp_change = Parse.find_all("td", class_="ltp")
    C_ltp_change = []
    for i in range(0, len(ltp_change), 2):
        C_ltp_change.append(ltp_change[i].text)
    
    ltp_change = Parse.find_all("td", class_="change")
    P_ltp_change = []
    for i in range(0, len(ltp_change)):
        P_ltp_change.append(ltp_change[i].text)
    
    string_formatter_value(C_ltp_change)
    string_formatter_value(P_ltp_change)
    
    OI_change = Parse.find_all("td", class_="oi_chg")
    C_OI_change = []
    P_OI_change = []
    for i in range(0, len(OI_change), 2):
        C_OI_change.append((OI_change[i].text).strip())
        P_OI_change.append((OI_change[i+1].text).strip()[0:7].replace("\r","").replace("\n", ""))
    
    string_formatter_value(C_OI_change)
    string_formatter_value(P_OI_change)
    
    OI = Parse.find_all("td", class_="oi")
    C_OI = []
    P_OI = []
    for i in range(0, len(ltp), 2):
        C_OI.append((OI[i].text).split(".")[0])
        P_OI.append((OI[i+1].text).split(".")[0])
    string_formatter_value(C_OI)
    string_formatter_value(P_OI)
    
    strike = Parse.find_all("td", class_="strike_price")
    strike_price = []
    for i in range(len(strike)):
        temp = strike[i].text.strip()
        if len(temp) > 6 :
            strike_price.append(temp[-6:])
        else:
            strike_price.append(temp)
        
    string_formatter_value(strike_price)
    for i in range(len(strike_price)) :
        strike_price[i] = int(strike_price[i])
        
    return (C_LTP, C_ltp_change, C_OI, C_OI_change, strike_price, P_OI_change, P_OI, P_ltp_change, P_LTP)


def get_OPC_data_groww():
    url = "https://groww.in/options/nifty?expiry"
    data = requests.get(url).text
    Parse = BeautifulSoup(data, features="html.parser")

    OI = Parse.find_all("div", class_="opr84CellVal")
    OI_C = []
    C_Price = []
    P_Price = []
    OI_P = []

    for val in range(0, len(OI), 4):
        OI_C.append((OI[val].text))
        C_Price.append((OI[val+1].text)[1:])
        P_Price.append((OI[val+2].text)[1:])
        OI_P.append(OI[val+3].text)
    
    string_formatter_value(OI_C)
    string_formatter_value(OI_P)
    string_formatter_value(C_Price)
    string_formatter_value(P_Price)

    OI = Parse.find_all("div", class_="opr84CellLowerVal")

    OI_C_change = []
    OI_P_change = []
    CP_change = []
    PP_change = []

    for val in range(0, len(OI), 4):
        OI_C_change.append((OI[val].text))
        CP_change.append((OI[val+1].text)[1:])
        PP_change.append((OI[val+2].text)[1:])
        OI_P_change.append(OI[val+3].text)

    string_formatter_percen(OI_C_change)
    string_formatter_percen(OI_P_change)

    CP_change = string_formatter_mix(CP_change)
    PP_change = string_formatter_mix(PP_change)

    CP_change_per = CP_change[1]
    CP_change = CP_change[0]

    PP_change_per = PP_change[1]
    PP_change = PP_change[0]

    OI = Parse.find_all("div", class_="opr84StrikeCell")
    strike_price = []
    for val in range(len(OI)):
        strike_price.append((OI[val].text))
    string_formatter_value_strike(strike_price)

    return (OI_C, OI_C_change, C_Price, CP_change, CP_change_per, strike_price, P_Price, PP_change, PP_change_per, OI_P_change, OI_P)

def show_OPC_ICICD():
    data = list(get_OPC_data_ICICID())
    OPC_dataframe = pd.DataFrame(data = {"Call_LTP":data[0], "Call_Price_Change":data[1], "Call_OI":data[2], "Call_OI_Change":data[3], "Strike_Price":data[4], "Put_OI_change":data[5], "Put_OI":data[6], "Put_Price_Change":data[7], "Put_LTP":data[8]})
    print(OPC_dataframe[19:60])

def show_OPC_GROWW():
    data = list(get_OPC_data_groww())
    OPC_dataframe = pd.DataFrame(data = {"Call OI":data[0], 
                                     "Call OI Change(in %)":data[1], 
                                     "Call LTP":data[2], 
                                     "Call Price Change":data[3], 
                                     "Call Price Change(in %)":data[4], 
                                     "Strike Price":data[5], 
                                     "Put Price Change(in %)":data[7], 
                                     "Put Price Change":data[8], 
                                     "Put LTP":data[6], 
                                     "Put OI Change(in %)":data[9], 
                                     "Put OI":data[10]})
    print(OPC_dataframe[49:90])

def get_pcr():
    url = "https://groww.in/options/nifty?expiry"
    data = requests.get(url).text
    Parse = BeautifulSoup(data, features="html.parser")

    OI = Parse.find_all("div", class_="opr84CellVal")
    OI_C = []
    C_Price = []
    P_Price = []
    OI_P = []

    for val in range(0, len(OI), 4):
        OI_C.append((OI[val].text))
        C_Price.append((OI[val+1].text)[1:])
        P_Price.append((OI[val+2].text)[1:])
        OI_P.append(OI[val+3].text)
    
    string_formatter_value(OI_C)
    string_formatter_value(OI_P)

    return round(sum(OI_P)/sum(OI_C), 3)

print(show_OPC_GROWW())

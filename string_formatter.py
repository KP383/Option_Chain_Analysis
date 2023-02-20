def string_formatter_value(ls):
    for i in range(len(ls)):
        if(ls[i] == ' -- '):
            ls[i] = 0
        else :
            ls[i] = float("".join(ls[i].split(",")))

def string_formatter_value_strike(ls):
    for i in range(len(ls)):
        if(ls[i] == ' -- '):
            ls[i] = 0
        else :
            ls[i] = ("".join(ls[i].split(",")))[:-3]

def string_formatter_percen(ls):
    for i in range(len(ls)):
        if(ls[i] == ''):
            ls[i] = 0
        else :
            ls[i] = float("".join(ls[i][0:-2].split(",")))

def string_formatter_mix(ls):
    ltp_change = []
    ltp_change_per = []
    for i in range(len(ls)):
        temp = (ls[i].split(" "))
        if(temp[0] == 'A'):
            ltp_change.append(0)
        else:
            ltp_change.append(float("".join(temp[0].split(","))))
#             ltp_change.append(float(temp[0]))
        ltp_change_per.append(float(temp[1][1:-2]))
    
    return [ltp_change_per, ltp_change]

def string_formatter_value_nl(data):
    return float("".join(data.split(",")))

def string_formatter_mix_nl(data):
    temp = data.split(" ")
    if(temp[0] == 'A'):
        temp[0] = 0
    else:
        temp[0] = float(temp[0])
    temp[1] = float(temp[1][1:-2])
    
    return temp


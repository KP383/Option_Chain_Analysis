import matplotlib.pyplot as plt
import numpy as np
import OPC_analysis as OPC 


def OPC_OI_data_visulize():
    data = OPC.get_OPC_data_ICICID()

    strike = np.array(data[4][19:60])
    Call_OI = np.round(np.array(data[2][19:60])/100000, 2)
    Put_OI = np.round(np.array(data[6][19:60])/100000, 2)

    width = 50  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(strike, Call_OI, width, label='Call OI', color="red", alpha=0.4)
    rects2 = ax.bar(strike, Put_OI, width, label='Put OI', color="green", alpha=0.4)
    fig.set_figheight(15)
    fig.set_figwidth(40)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('OI',fontsize=20)
    ax.set_xlabel('Strike Price',fontsize=20)
    ax.set_title('Option Chain - Open Interest Analysis', fontsize=35, weight='bold')
    ax.legend()
    # plt.rcParams.update({'font.size': 22})
    ax.bar_label(rects1, padding=3, color="red")
    ax.bar_label(rects2, padding=3, color="green")
    fig.tight_layout()
    plt.show()

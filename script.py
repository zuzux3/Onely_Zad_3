import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

fname = cbook.get_sample_data('indexing.csv', asfileobj=False)
with cbook.get_sample_data('G:\Onely_Zad_3\indexing.csv') as file:
    data = pd.read_csv("indexing.csv")

status = pd.DataFrame(data["status"].value_counts())
print(status)
status.plot(kind='bar')

plt.show()

status_details = pd.DataFrame(data['status_details'].value_counts())
print(status_details)
status_details.plot(kind='bar')

plt.show()
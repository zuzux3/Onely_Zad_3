##import numpy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import seaborn as sns

fname = cbook.get_sample_data('indexing.csv', asfileobj=False)
with cbook.get_sample_data('G:\Onely_Zad_3\indexing.csv') as file:
    data = pd.read_csv("indexing.csv")

date = pd.DataFrame(data['date'].value_counts())
print(date)
date.plot(kind = 'bar')

plt.show()

domain = pd.DataFrame(data['domain'].value_counts())
print(domain)
domain.plot(kind = 'bar', figsize = (15, 7))

plt.show()

status = pd.DataFrame(data["status"].value_counts())
print(status)
status.plot(kind='bar', figsize = (6, 7))
 
plt.show()

status_details = pd.DataFrame(data['status_details'].value_counts())
print(status_details)
status_details.plot(kind='bar', figsize = (7, 10))

plt.show()

data['date'] = data['date'].astype('category').cat.codes
data['domain'] = data['domain'].astype('category').cat.codes
data["status"] = data["status"].astype("category").cat.codes
data['status_details'] = data['status_details'].astype('category').cat.codes
data['pages'] = data['pages'].astype('category').cat.codes
dataCorr = data.corr()

print(dataCorr)

ax = sns.heatmap(
    dataCorr,
    vmin = -1, vmax = 1, center = 0,
    cmap = sns.diverging_palette(20, 220, n = 200),
    square = True
)

ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation = 45,
    horizontalalignment='right'
)

plt.show()
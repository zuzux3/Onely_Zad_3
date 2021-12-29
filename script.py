import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("indexing.csv")

domainDescription = data['domain'].describe()
print(domainDescription)
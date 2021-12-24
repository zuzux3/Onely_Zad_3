import pandas as pd
import numpy as np

data = pd.read_csv("indexing.csv")

domain = data["domain"].value_counts()

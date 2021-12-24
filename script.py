import pandas as pd
import numpy as np
import matlplotlib.pyplot as plt

data = pd.read_csv("indexing.csv")

domain = data["domain"].value_counts()

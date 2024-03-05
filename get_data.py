from sklearn.datasets import make_regression
import pandas as pd
import numpy as np
import os

# if there is no a dataset in the project directory, create a reasonably large one.
# if it exist append new observations.

if os.path.isfile('data.csv'):
    n = 1
else:
    n = 50

for i in range(n):
    X, y = make_regression(10000, n_features= 10)
    df = pd.DataFrame(X)
    df.to_csv('data.csv', mode= 'a')

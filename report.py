import pandas as pd
from pandas_profiling import ProfileReport

data = pd.read_csv('internship companies.csv')
data = data.drop('Unnamed: 0',axis=1)
profile = ProfileReport(data, title='report company')
profile.to_file('internship report.html')
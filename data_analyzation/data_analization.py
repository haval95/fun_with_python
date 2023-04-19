import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


#OVERVIEW
data = pd.read_csv("reviews.csv", parse_dates=["Timestamp"])
print(data.head())
print(data.shape)
print(data.columns)
data.hist("Rating")
plt.show()

#SELECTING DATA FROM DF:

#one col = series
print(type(data["Rating"]))
# more than one = Data frame
print(type(data[["Course Name","Rating"]]))

#selecting one row
print(data.iloc[3])
#selecting multiple row
print(data.iloc[0:3])


#selecting a section (rows * cols)
print(data[["Course Name","Rating"]].iloc[0:3])


#selecting a cell
print(data["Timestamp"].iloc[3])
print(data.at[3,'Timestamp'])


#Conditions 

#ONE CONDTION:
print(data[data["Timestamp"]< data.at[2,"Timestamp"]])
#TWO CONDTION:
print(data[(data["Timestamp"]< data.at[2,"Timestamp"]) & (data["Rating"] >= 5)]["Rating"].mean())

print(data[(data["Timestamp"] >= pd.Timestamp(datetime(2020,7,1),tz='UTC'))] )

print(data[data['Comment'].str.contains("accent", na=False)])
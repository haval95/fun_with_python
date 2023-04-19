from bokeh.plotting import figure
import pandas as pd
from bokeh.io import output_file, show
df = pd.read_csv("adbe.csv")
df['Date'] = pd.to_datetime(df['Date'])
output_file("lineGraph.html")
p = figure(width=500,height=500,x_axis_type="datetime", resizable=True)

p.line(df["Date"], df["Close"], color="orange")

show(p)
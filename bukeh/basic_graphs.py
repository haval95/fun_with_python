from bokeh.plotting import figure
from bokeh.io import output_file, show

# data
x = [1,2,3,4,5,6]
y = [6,7,8,9,10,11]

output_file("line.html")

#creating a figure obj
f = figure()

# creating a line
f.line(x,y)


show(f)
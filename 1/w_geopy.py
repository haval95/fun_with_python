from geopy.geocoders import ArcGIS
import pandas as pd




arg = ArcGIS()

#u can ask for geo cordinates this way
arg.geocode("3995 23rd st, San Francisco, Ca 94114")


df = pd.read_csv("sample.csv")
df["Address"]=df["Address"]+ ", "+ df["City"] + ", " + df["State"] +", "+df["Country"]
#or u can ask for geo cordinates this way which applies tht geocode method to all the rows in address
df["Cordinates"]= df["Address"].apply(arg.geocode)
df["Latitude"]=df["Cordinates"].apply(lambda cordinate: cordinate.latitude)
df["Longitude"]=df["Cordinates"].apply(lambda cordinate: cordinate.longitude)
print(df)
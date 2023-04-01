import pandas as pd

#READING DATA
# to Filter data we have df.loc or df.iloc -->
# loc needs values of the index and the column names u want ["1", ("Availability","Bedrooms","Area/m2")]
# iloc needs index numbers in the inedx column and index number of the clolumns [1:2, 1:4]


print("-----------READING DATA, SETTING INDEX------------------")
data_frame = pd.read_csv("rental_properties.csv", header=None)
data_frame.columns=["Price/PLN","Utility Price","Availability","Bedrooms","Area/m2","Location/Warsaw"]
data_frame= data_frame.set_index('Bedrooms')

print(data_frame.shape)

print(data_frame.iloc[1:4, 2:6])
print(data_frame)
print("-----------ROWS DELETION------------------")
# DELETING DATA
#ROW  axis = 0
data_frame.drop(4,axis=0,inplace=True)
data_frame.drop(data_frame.index[1:2],axis=0,inplace=True)
print(data_frame)

print("------------COLS DELETION------------------")
#col axis = 1
data_frame.drop("Price/PLN", axis=1, inplace=True)
data_frame.drop(data_frame.columns[1:2],axis=1,inplace=True)
print(data_frame)

print("------------UPDATING------------------")
#adding a col
print(data_frame.shape)
data_frame['Flor'] =data_frame.shape[0]* [3]
print(data_frame)

# to add a row u need to rotate the table and add the row as a col ---> .T rotates the table
df_t= data_frame.T
df_t["10"] = ["with bills", 1000, "somewhere", 5]
data_frame = df_t.T
print(data_frame)



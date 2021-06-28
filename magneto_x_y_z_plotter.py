# Importing the liberaries
import pandas as pd
import matplotlib.pyplot as plt

# shortening the data.csv to data
data = pd.read_csv("data.csv")

# reading the time from the data file
time =  data['Time']

# gathering and shortening the magnetometer data to magneto_x ,magneto_y ,magneto_z
Magneto_x = data['Magnetometer_x']
Magneto_y = data['Magnetometer_y']
Magneto_z = data['Magnetometer_z']

# ploting the magneto_x , magneto_y , magneto_z rays
plt.plot( Magneto_x, label="Magneto_x")
plt.plot( Magneto_y, label="Magneto_y")
plt.plot( Magneto_z, label="Magneto_z")

# adding a title to the graph
plt.title("CLOUD-LAB: Magnetometer Graph")
plt.xlabel("Number of readings")
plt.ylabel("Magnetic field intensity (µT)")
plt.legend()
plt.show()
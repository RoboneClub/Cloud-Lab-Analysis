# Importing the liberaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# shortening the data.csv to data
data = pd.read_csv('data.csv')

# reading the time from the data file
time =  data['Time']

# getting the data from magnetometers x,y,z
Magneto_x = data['Magnetometer_x']
Magneto_y = data['Magnetometer_y']
Magneto_z = data['Magnetometer_z']

# giving the data a power of 2
mag_x_2 = np.power(Magneto_x, 2)
mag_y_2 = np.power(Magneto_y, 2)
mag_z_2 = np.power(Magneto_z, 2)

# using a rule to get the absolute magnetic field of x,y,z
abs_mag = np.sqrt( mag_x_2 + mag_y_2 + mag_z_2)

# printing the absolute mag value in the terminal
# print(abs_mag)

# counting the number of readings
number_of_readings = len(abs_mag)

# getting the sum of the readings
sum_of_all_Magneto = np.sum( abs_mag )

# getting the mean using the sum divided by the number
mean_value_of_Magneto = sum_of_all_Magneto / number_of_readings
mean_value_of_Magneto = np.full(shape=number_of_readings, fill_value=mean_value_of_Magneto)

# ploting the x axis label
plt.xlabel("Number of Readings")
# ploting the y axis label
plt.ylabel("Magnetic fields intensity (µT)")
# ploting the abs_mag ray
plt.plot(abs_mag, label="Magneto")
# ploting the abs_mag's mean 
plt.plot(mean_value_of_Magneto, label="mean")
# adding a title to the graph
plt.title("CLOUD-LAB: Magnetometer Graph")
plt.legend()
plt.show()

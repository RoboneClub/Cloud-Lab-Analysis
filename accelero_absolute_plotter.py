
# Importing the liberaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# shortening the data.csv to data
data = pd.read_csv('data.csv')

# reading the time from the data file
time =  data['Time']

# getting the data from Accelometers x,y,z
Accelo_x = data['Accelerometer_x']
Accelo_y = data['Accelerometer_y']
Accelo_z = data['Accelerometer_z']

# giving the data a power of 2
accelo_x_2 = np.power(Accelo_x, 2)
accelo_y_2 = np.power(Accelo_y, 2)
accelo_z_2 = np.power(Accelo_z, 2)

# using a rule to get the absolute Acceleration of x,y,z
abs_accelo = np.sqrt( accelo_x_2 + accelo_y_2 + accelo_z_2)

# printing the absolute accelo value in the terminal
# print(abs_accelo)

# counting the number of readings
number_of_readings = len(abs_accelo)
# getting the sum of the readings
sum_of_all_Accelo = np.sum( abs_accelo )
# getting the mean using the sum divided by the number
mean_value_of_Accelo = sum_of_all_Accelo / number_of_readings
mean_value_of_Accelo = np.full(shape=number_of_readings, fill_value=mean_value_of_Accelo)

# ploting the x axis label
plt.xlabel("Number of Readings")
# ploting the y axis label
plt.ylabel("Acceleration (G)")
# ploting the abs_accelo ray
plt.plot(abs_accelo, label="Accelo")
# ploting the abs_accelo's mean 
plt.plot(mean_value_of_Accelo, label="mean")
# adding a title to the graph
plt.title("CLOUD-LAB: Accelometer Graph")
plt.legend()
plt.show()
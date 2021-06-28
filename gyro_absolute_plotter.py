# Importing the liberaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# shortening the data.csv to data
data = pd.read_csv('data.csv')

# reading the time from the data file
time =  data['Time']

# getting the data from Gyroscopes x,y,z
Gyro_x = data['Gyroscope_x']
Gyro_y = data['Gyroscope_y']
Gyro_z = data['Gyroscope_z']

# giving the data a power of 2
gyro_x_2 = np.power(Gyro_x, 2)
gyro_y_2 = np.power(Gyro_y, 2)
gyro_z_2 = np.power(Gyro_z, 2)

# using a rule to get the absolute gyronetic field of x,y,z
abs_gyro = np.sqrt( gyro_x_2 + gyro_y_2 + gyro_z_2)

# printing the absolute gyro value in the terminal
# print(abs_gyro)

# counting the number of readings
number_of_readings = len(abs_gyro)
# getting the sum of the readings
sum_of_all_Gyro = np.sum( abs_gyro )
# getting the mean using the sum divided by the number
mean_value_of_Gyro = sum_of_all_Gyro / number_of_readings
mean_value_of_Gyro = np.full(shape=number_of_readings, fill_value=mean_value_of_Gyro)

# ploting the x axis label
plt.xlabel("Number of Readings")
# ploting the y axis label
plt.ylabel("Angular Velocity (rad/sec)")
# ploting the abs_gyro ray
plt.plot(abs_gyro, label="Gyro")
# ploting the abs_gyro's mean 
plt.plot(mean_value_of_Gyro, label="mean")
# adding a title to the graph
plt.title("CLOUD-LAB: Gyroscope Graph")
plt.legend()
plt.show()
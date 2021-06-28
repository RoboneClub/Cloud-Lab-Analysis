# Importing the liberaries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# shortening the data.csv to data
data = pd.read_csv('data.csv')

# reading the time from the data file
time =  data['Time']

# gathering and shortening the accelometer's data to acce_x ,acce_y ,acce_z
acce_x = data['Accelerometer_x']
acce_y = data['Accelerometer_y']
acce_z = data['Accelerometer_z']

# counting the number of readings of the magnetometer
number_of_readings = len(acce_x)

# printing the number of readings in the terminal
print("number_of_readings: ", number_of_readings)

# getting the sum of the readings in x,y,z
sum_of_all_acce_x = np.sum( acce_x )
sum_of_all_acce_y = np.sum( acce_y )
sum_of_all_acce_z = np.sum( acce_z )

# printing the sum of acce_x readings in the terminal
print("sum_of_all_acce_x: ", sum_of_all_acce_x)

# getting the mean using the sum divided by the number
mean_value_of_acce_x = sum_of_all_acce_x / number_of_readings
mean_value_of_acce_y = sum_of_all_acce_y / number_of_readings
mean_value_of_acce_z = sum_of_all_acce_z / number_of_readings
# printing the mean of acce_x readings in the terminal
print("mean_value_of_acce_x: ", mean_value_of_acce_x)
mean_value_of_acce_x = np.full(shape=number_of_readings, fill_value=mean_value_of_acce_x)
mean_value_of_acce_y = np.full(shape=number_of_readings, fill_value=mean_value_of_acce_y)
mean_value_of_acce_z = np.full(shape=number_of_readings, fill_value=mean_value_of_acce_z)

# ploting accelometers x,y,z's ray
plt.plot( acce_x, label="acce_x")
plt.plot( acce_y, label="acce_y")
plt.plot( acce_z, label="acce_z")
# ploting accelometers x,y,z's mean
plt.plot( mean_value_of_acce_x, label="Mean_x")
plt.plot( mean_value_of_acce_y, label="Mean_y")
plt.plot( mean_value_of_acce_z, label="Mean_z")
# adding a title to the graph
plt.title("CLOUD-LAB: Accelometer Graph")

plt.xlabel("Number of readings")
plt.ylabel("Acceleration (G)")
plt.legend()
plt.show()
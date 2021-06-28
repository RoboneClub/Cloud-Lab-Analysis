# Importing the liberaries
import pandas as pd
import matplotlib.pyplot as plt

# shortening the data.csv to data
data = pd.read_csv('data.csv')

# reading the time from the data file
time =  data['Time']

# gathering and shortening the gyroscope data to gyro_x ,gyro_y ,gyro_z
gyro_x = data['Gyroscope_x']
gyro_y = data['Gyroscope_y']
gyro_z = data['Gyroscope_z']

# ploting the gyro_x , gyro_y , gyro_z rays
plt.plot( gyro_x, label="gyro_x")
plt.plot( gyro_y, label="gyro_y")
plt.plot( gyro_z, label="gyro_z")

# adding a title and labels to the graph
plt.title("CLOUD-LAB: Gyroscope Graph")
plt.xlabel("Number of readings")
plt.ylabel("Angular rates (rad/s)")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Data for Average Rainfall and Year
year = np.array([2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
                 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024])
average_rainfall = np.array([85.42333333, 102.4, 100.779, 89.56, 102.954, 102.94, 
                             103.427, 93.579, 95.38, 96.68, 84.08, 66.87, 72.866, 
                             84.47, 111.86, 100.845, 111.527, 107.79, 121.235, 
                             72.21, 105.64])

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(year, average_rainfall, marker='o', linestyle='-', color='b', label='Average Rainfall')
plt.fill_between(year, average_rainfall, color='skyblue', alpha=0.3)

# Adding labels and title
plt.title('Average Rainfall (mm) for Karnataka Area (2004-2024)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Rainfall (mm)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)

# Highlighting trends and significant points
plt.axhline(y=np.mean(average_rainfall), color='r', linestyle='--', label=f'Average: {np.mean(average_rainfall):.2f} mm')
plt.legend()

# Showing the plot
plt.tight_layout()
plt.show()

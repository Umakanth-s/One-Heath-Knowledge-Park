import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Dog Bites.csv')

# Print the first few rows to verify data
print(data.head())

# Filter data for 'All India' and the years 2018 to 2023
filtered_data = data[(data['state'] == 'All India') & (data['year'] >= 2018) & (data['year'] <= 2023)]

# Print filtered data to ensure it's correct
print(filtered_data)

# Plot the data
plt.figure(figsize=(10,6))
plt.plot(filtered_data['year'], filtered_data['dog_bite_cases'], marker='o', linestyle='-', color='b')

# Add titles and labels
plt.title('Dog Bite Cases in All India (2018-2023)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Dog Bite Cases', fontsize=12)

# Annotate each point with the respective value
for i in range(len(filtered_data)):
    plt.text(filtered_data['year'].iloc[i], filtered_data['dog_bite_cases'].iloc[i], 
             str(filtered_data['dog_bite_cases'].iloc[i]), 
             fontsize=10, ha='center', va='bottom')

# Display the plot with grid
plt.grid(True)
plt.show()
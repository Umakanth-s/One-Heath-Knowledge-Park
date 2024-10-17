import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
initial_population = 350
sex_ratio = 2 / 3  # Male to total ratio
female_ratio = 1 / 3  # Female to total ratio
lifespan = 5  # years
start_reproduction_age = 1  # years
end_reproduction_age = lifespan - 1  # years
average_puppies_per_year_per_female = 4
puppy_survival_rate = 0.6  # 60% survive to reproductive age
annual_mortality_rate = 0.2  # 20% annual mortality rate
neutralization_rate = 0.65  # 65% neutralization of females
rabies_infection_rate = 0.05  # 5% annual infection rate

# Initial population distribution
initial_male_population = int(initial_population * sex_ratio)
initial_female_population = int(initial_population * female_ratio)

# Simulation period (years)
years = 5  # Set to 5 for comparison

# Initialize population arrays
population_male = [initial_male_population]
population_female = [initial_female_population]

# Initialize population arrays for neutralization scenario
population_male_neutralized = [initial_male_population]
population_female_neutralized = [initial_female_population]

# Initialize rabies infected population arrays
rabies_infected = [0]
rabies_infected_neutralized = [0]

# Simulation loop
for year in range(1, years + 1):
    # Without neutralization
    reproductive_females = sum([population_female[year - age] for age in range(start_reproduction_age, end_reproduction_age + 1) if year - age >= 0])
    new_puppies = reproductive_females * average_puppies_per_year_per_female
    new_puppies_surviving = int(new_puppies * puppy_survival_rate)
    
    new_male_puppies = int(new_puppies_surviving * sex_ratio)
    new_female_puppies = new_puppies_surviving - new_male_puppies
    
    deaths_male = int(population_male[-1] * annual_mortality_rate)
    deaths_female = int(population_female[-1] * annual_mortality_rate)
    
    population_male.append(population_male[-1] + new_male_puppies - deaths_male)
    population_female.append(population_female[-1] + new_female_puppies - deaths_female)
    
    # Rabies infections
    new_infections = int((population_male[-1] + population_female[-1]) * rabies_infection_rate)
    rabies_infected.append(rabies_infected[-1] + new_infections)
    
    # With neutralization
    reproductive_females_neutralized = sum([population_female_neutralized[year - age] for age in range(start_reproduction_age, end_reproduction_age + 1) if year - age >= 0])
    reproductive_females_neutralized = int(reproductive_females_neutralized * (1 - neutralization_rate))
    new_puppies_neutralized = reproductive_females_neutralized * average_puppies_per_year_per_female
    new_puppies_surviving_neutralized = int(new_puppies_neutralized * puppy_survival_rate)
    
    new_male_puppies_neutralized = int(new_puppies_surviving_neutralized * sex_ratio)
    new_female_puppies_neutralized = new_puppies_surviving_neutralized - new_male_puppies_neutralized
    
    deaths_male_neutralized = int(population_male_neutralized[-1] * annual_mortality_rate)
    deaths_female_neutralized = int(population_female_neutralized[-1] * annual_mortality_rate)
    
    population_male_neutralized.append(population_male_neutralized[-1] + new_male_puppies_neutralized - deaths_male_neutralized)
    population_female_neutralized.append(population_female_neutralized[-1] + new_female_puppies_neutralized - deaths_female_neutralized)
    
    # Rabies infections with neutralization
    new_infections_neutralized = int((population_male_neutralized[-1] + population_female_neutralized[-1]) * rabies_infection_rate)
    rabies_infected_neutralized.append(rabies_infected_neutralized[-1] + new_infections_neutralized)

# Create a DataFrame for the results
years_list = list(range(years + 1))
total_population = [m + f for m, f in zip(population_male, population_female)]
total_population_neutralized = [m + f for m, f in zip(population_male_neutralized, population_female_neutralized)]
rabies_percentage = [i / t * 100 if t > 0 else 0 for i, t in zip(rabies_infected, total_population)]
rabies_percentage_neutralized = [i / t * 100 if t > 0 else 0 for i, t in zip(rabies_infected_neutralized, total_population_neutralized)]

data = {
    'Year': years_list,
    'Total Population': total_population,
    'Total Population Neutralized': total_population_neutralized,
    'Rabies Infected': rabies_infected,
    'Rabies Infected Neutralized': rabies_infected_neutralized,
    'Rabies Percentage': rabies_percentage,
    'Rabies Percentage Neutralized': rabies_percentage_neutralized
}
df = pd.DataFrame(data)

# Plot the results
fig, ax = plt.subplots(figsize=(12, 10))

ax.plot(df['Year'], df['Total Population'], label='Without Neutralization', marker='o')
ax.plot(df['Year'], df['Total Population Neutralized'], label='With Neutralization', marker='o')
ax.plot(df['Year'], df['Rabies Infected'], label='Rabies Infected Without Neutralization', marker='x')
ax.plot(df['Year'], df['Rabies Infected Neutralized'], label='Rabies Infected With Neutralization', marker='x')

ax.set_xlabel('Years')
ax.set_ylabel('Number of Dogs')
ax.set_title('Predicted Increase in Stray Dogs and Rabies Infections')
ax.legend()
ax.grid(True)

# Create table data
table_data = []
for year in years_list:
    row = [
        year,
        df.loc[df['Year'] == year, 'Rabies Infected'].values[0],
        df.loc[df['Year'] == year, 'Rabies Percentage'].values[0],
        df.loc[df['Year'] == year, 'Rabies Infected Neutralized'].values[0],
        df.loc[df['Year'] == year, 'Rabies Percentage Neutralized'].values[0]
    ]
    table_data.append(row)

column_labels = ['Year', 'Rabies Infected', 'Rabies Percentage (%)', 'Rabies Infected Neutralized', 'Rabies Percentage Neutralized (%)']
table = plt.table(cellText=table_data, colLabels=column_labels, cellLoc='center', loc='bottom', bbox=[0.0, -0.4, 1.0, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.subplots_adjust(left=0.2, bottom=0.35)

plt.show()
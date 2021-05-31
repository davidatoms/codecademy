# Dependencies



city_name = "Istanbul, Turkey"

# Data from codecademy on Istanbul
pop_1927 = 691000
pop_1950 = 983000
pop_2000 = 8831800
pop_2017 = 15029231

# Calculate the values of change between 2017 and 1927
pop_change = pop_2017 - pop_1927

percentage_growth_rate = (pop_change / pop_1927) * 100

annual_gr = percentage_growth_rate / (2017 - 1927)

# Create a function that goes through the different years
def population_growth(year_one, year_two, population_one, population_two):
    pop_change = popluation_one = population_two
    percentage_growth = (pop_change / population_one) * 100
    growth_rate = percentage_growth_rate / (year_two - year_one)
    return growth_rate

set_one = population_growth(1927, 2017, pop_1927, pop_2017)
# print(set_one)
set_two = population_growth(1950, 2000, pop_1950, pop_2000)
# print(set_two)

report = "The population grew from " + str(pop_1927) + " to " + str(pop_2017) + ", with a total change of " + str(pop_change) + ". The annual % growth rate was " + str(annual_gr)
print(report)
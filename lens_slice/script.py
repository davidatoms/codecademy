# Pizza dictionaries
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]


# Calculations
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
asc_pizza_prices = pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]


# Actions
# Man walks in and wants pricest pizza
print(priciest_pizza)
# Delete the priciest pizza from menu
pizza_and_prices.pop()
# Print new menu
print(pizza_and_prices)
# New topping with peppers
pizza_and_prices.insert(4, [2.5, "peppers"])
# Three mice walk in and need the pizza sliced by three lowest
three_cheapest = pizza_and_prices[:3]


# Print it out
# print(num_two_dollar_slices)
# print(num_pizzas)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
print("-----")
print(pizza_and_prices)
print(three_cheapest)
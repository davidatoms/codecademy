# receipts for lovely loveseats

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Comes in red or white."
lovely_loveseat_price = 254.00
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.12

sales_tax = .088

customer_1_total = 0

customer_1_itemization = ""

customer_1_total += lovely_loveseat_price
customer_1_total += luxurious_lamp_price

print("Customer Copy")
print("-------------")
print("Thank you for shopping with us!")
print("-------------")
print("Your items:")
print(str(lovely_loveseat_description) + " " + "$" + str(lovely_loveseat_price))
print(str(luxurious_lamp_description) + " " + "$" + str(luxurious_lamp_price))
print("Tax: 8.8%")
print("$"+str(round(customer_1_total*sales_tax, 2)))

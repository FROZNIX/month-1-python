def calculate_profit(rent, diesel) :
    profit = rent - diesel
    return profit

bachat1 = calculate_profit(4000, 1500)
bachat2 = calculate_profit(300, 1400)

print(f"bachat1 : ${bachat1}")
print (f"bachat2 : ${bachat2}")

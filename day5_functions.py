def calculate_profit(diesel,rent):
    return rent-diesel

try:
    rent_input=float(input("Car Rent (Rs):"))
    diesel_input=float(input("Fuel Cost (Rs):"))

    bachat = calculate_profit(diesel_input, rent_input)
    print(f"Asli Bachat (profit): Rs {bachat:.2f}")

except ValueError:
        print("Bhai, dhayn se! sirf No.(digits) type kar")
    
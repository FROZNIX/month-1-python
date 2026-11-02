# Day 2 Part 2: Papa ki 3 Gaadiyon ka Profit Tracker (Loop ke sath)

# 1. Khali list (har gaadi ka bacha hua paisa rakhne ke liye)
car_profits = []

# 2. Khali Galla (kul kamayi jodne ke liye shuru mein 0 rakha)
total_profits = 0

print("--- Papa Fleet Daily Hisab ---")

# 3. 3 Gaadiyon ke liye loop (1, 2, aur 3)
for car_num in range(1, 4):
    # User se kamayi aur diesel ka kharcha integer (int) mein maango
    rent = int(input(f"\nGaadi {car_num} ne aaj kitna kiraya kamaya (₹): "))
    fuel = int(input(f"Gaadi {car_num} mein kitne ka diesel laga (₹): "))
    
    # Asli bachat (kamayi mein se diesel ghatao)
    total = rent - fuel
    
    # List mein is gaadi ki bachat jod do
    car_profits.append(total)
    
    # Galle (total_profits) mein yeh bachat jod do
    total_profits += total

print("\n--- Aaj ki Final Report ---")
for index, profit in enumerate(car_profits, start=1):
    print(f"Gaadi {index} ki shuddh bachat: ₹{profit}")

print(f"\n💰 Aaj ka Kul Munafa (Total Profit): ₹{total_profits}")
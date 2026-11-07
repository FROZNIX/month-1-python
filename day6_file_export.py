import csv
import os

def calculate_profit(rent, diesel):
    return rent-diesel

try:
    
    rent_input = float(input("Gaadi ka Rent Rs."))
    diesel_input = float(input("Fuel Cost Rs."))

    bachat = calculate_profit(rent_input,diesel_input)
    print(f"Asli Bachat (Profit): Rs {bachat:.2f}")
# File mein record save karne ka code (CSV Export)
    file_name = "papa_record.csv"
    file_exists = os.path.exists(file_name)

    with open(file_name, mode="a", newline ="")as file:
        writer = csv.writer(file)
# Agar file pehli baar ban rahi hai toh heading likho
        if not file_exists : 
            writer.writerow(["Rent (Rs)", "Diesel (Rs)", "Bachat (Rs)"])
        # Data row likho
        writer.writerow([rent_input, diesel_input, f"{bachat:.2f}"])
    
    print("SUCCESS: Yeh hisaab 'papa_record.csv' file mein securely save ho gaya hai!")

except ValueError:
    print("Bhai, dhyan se! Sirf numbers (digits) type kar, text mat daal.")
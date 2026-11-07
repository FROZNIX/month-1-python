import csv
import os

FILE_NAME = "papa_record.csv"

def calculate_profit(rent, diesel):
    return rent - diesel

while True:
    print("\n=== PAPA FLEET EXPENSE TRACKER ===")
    print("1. Naya Trip Hisaab Jodo (Save to CSV)")
    print("2. Ab Tak Ka Total Profit Dekho (Read CSV)")
    print("3. Bahar Niklo (Exit)")
    
    choice = input("Apna option chuno (1/2/3): ")

    if choice == "1":
        try:
            rent_input = float(input("Gaadi ka Rent (Rs): "))
            diesel_input = float(input("Fuel Cost (Rs): "))
            bachat = calculate_profit(rent_input, diesel_input)
            print(f"Is Trip Ki Bachat: Rs {bachat:.2f}")

            file_exists = os.path.exists(FILE_NAME)
            with open(FILE_NAME, mode="a", newline="") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["Rent (Rs)", "Diesel (Rs)", "Bachat (Rs)"])
                writer.writerow([rent_input, diesel_input, f"{bachat:.2f}"])
            print("Saved to papa_record.csv!")
        except ValueError:
            print("Galti! Sirf numbers (digits) type kar.")

    elif choice == "2":
        if not os.path.exists(FILE_NAME):
            print("Abhi tak koi record save nahi hua hai!")
        else:
            total_profit = 0.0
            trips = 0
            with open(FILE_NAME, mode="r") as file:
                reader = csv.reader(file)
                next(reader, None)  # Pehli heading row ko skip karne ke liye
                for row in reader:
                    if len(row) == 3:
                        total_profit += float(row[2])
                        trips += 1
            print(f"\nTotal Trips: {trips} | Ab Tak Ki Kul Bachat: Rs {total_profit:.2f}")

    elif choice == "3":
        print("System band ho raha hai. Jai Hind!")
        break

    else:
        print("Galat button! Sirf 1, 2, ya 3 daba.")
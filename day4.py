def calculate_profit(rent,diesel):
    return rent- diesel

papa_fleet = [
              {"model": "Ertiga", "Dvr.": "vinod", "rent": 4000, "diesel": 1500},
              {"model": "Innovs", "Dvr.": "sanjeet", "rent": 3000, "diesel": 2000},
              {"model": "Innova_Crysta", "Dvr.": "Pramod", "rent": 4000, "diesel": 2300}
]
total_profit = 0
file=open("papa_record.csv","w")
file.write("Gaadi,Rent,Diesel,Bachat,Status\n")
print("papa_fleet_report")
for car in papa_fleet:
            bachat = calculate_profit(car["rent"], car["diesel"])
            total_profit += bachat

            if bachat < 0:
                status = "LOSS"
            else:
               status = "PROFIT"

            print(f"Gaadi: {car['model']} | Driver: {car['Dvr.']} | Bachat: Rs.{bachat} ({status})")
            file.write(f"{car['model']},{car['rent']},{car['diesel']},{bachat},{status}\n")

file.close()
print(f"\nKul Company Munafa: Rs.{total_profit}")
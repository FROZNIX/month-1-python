papa_car = {
    "car_model" : "Ertiga",
    "driver_name" : "Vinod",
    "daily_rent" : 3000,
    "diesel_cost" : 500
}
net_profit = papa_car["daily_rent"] - papa_car["diesel_cost"]

print("--- Smart Fleet Register ---")
print(f"Gaadi Model: {papa_car['car_model']}")
print(f"Driver: {papa_car['driver_name']}")
print(f"Aaj ki Shuddh Bachat: ₹{net_profit}")
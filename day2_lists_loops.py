my_daily_tasks = []
print ("____Task Tracker____")


for i in range(1,6):
    task = input ("Task {i} bata kya karega :")
    my_daily_tasks.append(task)

    print("/n---Tera AAZ ka final tasks")
    #i dont do that
    for index, t in enumerate(my_daily_tasks, start=1):
        print("index")



        # Part - 2
    car_profits = []
    total_profits = 0
print("--- Daily Hisab --- ")
for car_num in range(1,4):
    Rent = int(input("Car Rent:"))
    Fuel = int(input("Fuel:"))

    Total = Rent - Fuel
    car_profits.append(Total)
    total_profits += Total
print("Total Amount")
for index, profit in enumerate(car_profits, start=1):
    print("Total Profit")
print("GTP:" , total_profits)

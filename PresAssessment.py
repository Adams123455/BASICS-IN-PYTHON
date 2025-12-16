#Question 1
inventory = {
    "Tomatoes": {"stock": 150, "price_per_unit": 5.0},
    "Onions": {"stock": 80, "price_per_unit": 3.5},
    "Garden Eggs": {"stock": 200, "price_per_unit": 1.0}
}


while True:
    print("Welcome to Makola Market!")
    print("1. Make a Purchase")
    print("2. View Stock")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        item = input("Enter item name to purchase (Tomatoes, Onions, Garden Eggs): ")

        if item in inventory:
            quantity = int(input("Enter quantity to buy: "))
            available = inventory[item]["stock"]

            if quantity > available:
                print(f"Sorry, only {available} units of {item} remaining.")
            else:
                cost = quantity * inventory[item]["price_per_unit"]
                inventory[item]["stock"] -= quantity
                new_stock = inventory[item]["stock"]

                print(f"Sale successful! Cost: GHS {round(cost, 2)}. {new_stock} units of {item} remaining.")
               
        else:
            print("Item not found in stock. Check spelling.")

    elif choice == '2':
        print("Current Stock:")
        for item, details in inventory.items():
            print(f"{item}: {details['stock']} units at GHS {details['price_per_unit']} per unit")

    elif choice == '3':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")

            
# Question 2
consumption = float(input("Total water consumption for the month (in cubic meters): "))

service_charge = 15.00
consumption_cost = 0.0

if consumption <= 15:
    consumption_cost = consumption * 0.90

elif consumption <= 30:
    consumption_cost = 15 * 0.90
    consumption_cost += (consumption - 15) * 1.20

else:
    consumption_cost = 15 * 0.90
    consumption_cost += 15 * 1.20
    consumption_cost += (consumption - 30) * 1.80


total_bill = service_charge + consumption_cost

print("--- Monthly Water Bill Summary ---")
print(f"Consumption: {consumption} m³")
print(f"Service Charge: GHS {round(service_charge, 2)}")
print(f"Consumption Cost: GHS {round(consumption_cost, 2)}")
print(f"Total Bill: GHS {round(total_bill, 2)}")






#Question 3
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100


speeding_violations = []


for speed in recorded_speeds:
    if speed > SPEED_LIMIT:
        print(f"WARNING: Vehicle recorded at {speed} km/h. Exceeded limit of {SPEED_LIMIT} km/h.")
        speeding_violations.append(speed)


total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)


speed_sum = 0
for current_speed in recorded_speeds:
    speed_sum += current_speed

average_speed = speed_sum / total_vehicles


percentage_speeding = (total_violations / total_vehicles) * 100

print("\n--- Traffic Speed Analysis Summary ---")
print(f"Total vehicles recorded: {total_vehicles}")
print(f"Total speeding violations: {total_violations}")
print(f"Percentage speeding: {percentage_speeding:.2f}%")
print(f"Average speed: {average_speed:.2f} km/h")


focused_segment = recorded_speeds[2:8]  

print(f"\nSpeeds for focused inspection segment (3rd to 8th vehicle): {focused_segment}")





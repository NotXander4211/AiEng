# Name:Lucas Escobar
# Period:PM
# Disneyland Trip Budget Calculator

#introducce
print("Welcome!")
print("This is my disney land calc")
print("this program estimated total cost for u")

#name
name = input("Enter your name: ")
# people and days
num_people = int(input("How many ppl are going: "))
park_days = int(input("How many days are you going to the park: "))
hotel_nights = int(input("how many nights in the hotel: "))
park_hopper_price = float(input("How much is a hopper pass: "))
total_ticket_cost = park_hopper_price * num_people
food_cost_perperson = float(input("How much will one person spend on food each day: ")) * park_days
total_food_cost = food_cost_perperson * num_people
souvenir_cost = float(input("how much will one person spend on souvenirs: "))
total_souvenir_cost = souvenir_cost * num_people
hotel_cost_per_room = float(input("how much does one room cost per night: "))
#calc hotel costs
total_hotel_cost = float(input("how many room do your group need: ")) * hotel_cost_per_room * hotel_nights
one_way_dist = float(input("how far do you live from disneyland"))
vehicle_mpg = float(input("how many mpg does your vehicle get: "))
round_trip_dist = one_way_dist * 2
gas_price = float(input("what is todays average gas price per gallon: "))
gallons_needed = round_trip_dist / vehicle_mpg
total_gas_price = gallons_needed * gas_price
parking_cost_per_day = float(input("how much does disneyland parking cost per day: ")) 
#calc final parking and final trip costs
total_parking_cost = parking_cost_per_day * park_days
final_trip_cost = total_parking_cost + total_gas_price + total_hotel_cost + total_souvenir_cost + total_food_cost + total_ticket_cost
#calc cost per person for the park
cost_per_person = final_trip_cost / num_people
cost_per_day = final_trip_cost / park_days
trip_budget = float(input("What is your budget: "))
budget_diff = trip_budget - final_trip_cost
# end report
print("\n--------- DISNEYLAND TRIP REPORT ---------\n")
# use f strings cause they are good
print(f"Traveler: {name}")
print(f"People Going: {num_people}")
print(f"Park Days: {park_days}")
print(f"Hotel Nights: {hotel_nights}")

print("\n--------- PARK HOPPER TICKETS ---------")
#use :,.2f to format like money
print(f"Park Hopper Price Per Person: ${park_hopper_price:,.2f}")
print(f"Total Ticket Cost: ${total_ticket_cost:,.2f}")

print("\n--------- FOOD AND SOUVENIRS ---------")
print(f"Total Food Cost: ${total_food_cost:,.2f}")
print(f"Total Souvenir Cost: ${total_souvenir_cost:,.2f}")

print("\n--------- HOTEL ---------")
print(f"Total Hotel Cost: ${total_hotel_cost:,.2f}")

print("\n--------- DRIVING ---------")
print(f"One Way Distance: {one_way_dist:.2f} miles")
print(f"Round Trip Distance: {round_trip_dist:.2f} miles")
print(f"Vehicle MPG: {vehicle_mpg:.2f}")
print(f"Gas Price: ${gas_price:,.2f}")
print(f"Gallons Needed: {gallons_needed:.2f}")
print(f"Total Gas Cost: ${total_gas_price:,.2f}")
print(f"Total Parking Cost: ${total_parking_cost:,.2f}")

print("\n--------- TRIP TOTAL ---------")
print(f"Final Trip Cost: ${final_trip_cost:,.2f}")
print(f"Cost Per Person: ${cost_per_person:,.2f}")
print(f"Cost Per Park Day: ${cost_per_day:,.2f}")

print("\n--------- BUDGET ---------")
print(f"Trip Budget: ${trip_budget:,.2f}")
print(f"Budget Difference: ${budget_diff:,.2f}")
# ending words
print(f"\nThanks for using my disneyland calc!")
print(f"Have fun at disneyland {name}!")

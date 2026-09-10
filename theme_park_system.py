# Name: Lucas Escobar
# Period: PM
# Theme Park Admission & Ride Eligibility System

# intro for the park
print("Welcome to Lunar Lights Adventure Park!")
print("Get ready for a day filled with glowing rides and exciting attractions.")
print("This system will calculate your admission price and highest ride level.")


# gets the normal price from their age
def calculate_admission(age):
    if age <= 4:
        return 0
    elif age <= 12:
        return 15
    elif age <= 64:
        return 30
    else:
        return 20


# checks what discount they get
def calculate_discount(price, member, visit_time):
    if member == "yes" and visit_time == "evening":
        discount = 10
    elif member == "yes":
        discount = 5
    elif visit_time == "evening":
        discount = 3
    else:
        discount = 0

    final_price = price - discount

    # makes sure the price cant go below 0
    if final_price < 0:
        final_price = 0

    return final_price


# finds the highest rides they can go on
def ride_level(age, height):
    if height >= 54 and age >= 16:
        return "Extreme Rides"
    elif height >= 48 and age >= 12:
        return "Thrill Rides"
    elif height >= 42 and age >= 8:
        return "Family Rides"
    elif height >= 36:
        return "Kiddie Rides"
    else:
        return "No Rides"


# checks if they need an adult to enter
def check_supervision(age, visiting_with_adult):
    if age < 13 and visiting_with_adult == "no":
        return "Adult Required"
    else:
        return "Approved"


# extra credit vip check
def check_vip(ticket_type, member, age):
    if (ticket_type == "premium" and member == "yes") or (age >= 65 and ticket_type == "premium"):
        return "VIP ACCESS"
    else:
        return "STANDARD ACCESS"


# asks for all the guest information
guest_name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you in inches? "))
ticket_type = input("Did you purchase a regular or premium ticket? ")
park_member = input("Are you a park member? Enter yes or no: ")
visiting_with_adult = input("Are you visiting with an adult? Enter yes or no: ")
visit_time = input("Are you visiting during the morning or evening? ")

# runs the functions and saves what they return
admission_price = calculate_admission(age)
final_admission_price = calculate_discount(admission_price, park_member, visit_time)
highest_ride_level = ride_level(age, height)
supervision_status = check_supervision(age, visiting_with_adult)
vip_status = check_vip(ticket_type, park_member, age)

# checks if they get the premium bonus
if ticket_type == "premium":
    premium_status = "PREMIUM BONUS: Free snack and priority ride access!"
else:
    premium_status = "Regular ticket: Standard park access included."

# prints the final guest report
print("\n========================================")
print("       LUNAR LIGHTS ADVENTURE PARK")
print("               GUEST REPORT")
print("========================================")
print(f"Guest Name: {guest_name}")
print(f"Age: {age}")
print(f"Height: {height} inches")
print(f"Ticket Type: {ticket_type}")
print(f"Park Member: {park_member}")
print(f"Admission Price Before Discount: ${admission_price}")
print(f"Final Admission Price: ${final_admission_price}")
print(f"Highest Ride Level: {highest_ride_level}")
print(f"Supervision Status: {supervision_status}")
print(f"Premium Ticket Status: {premium_status}")
print(f"VIP Status: {vip_status}")

# picks a final message for the guest
if supervision_status == "Adult Required":
    personalized_message = "Please return with an adult so you can enter the park safely."
elif highest_ride_level == "No Rides":
    personalized_message = "Enjoy our shows, games, food, and other ground attractions!"
elif highest_ride_level == "Extreme Rides":
    personalized_message = "You qualify for every ride level. Get ready for our wildest rides!"
elif ticket_type == "premium":
    personalized_message = "Enjoy your premium perks and skip ahead to more fun!"
elif age <= 4:
    personalized_message = "Your admission is free today. Have a magical first adventure!"
elif age >= 65:
    personalized_message = "Thank you for visiting. We hope you have a wonderful day!"
else:
    personalized_message = "Have an amazing adventure at Lunar Lights!"

print(f"Personalized Message: {personalized_message}")
print("========================================")
print("Thank you for visiting Lunar Lights Adventure Park!")
print("========================================")

import datetime  # get the date for the final receipt
# Date research: https://docs.python.org/3/library/datetime.html#datetime.date.today
# date.today() gets the local date, and strftime("%m/%d/%Y") formats it as month/day/year.

products = {  # connect five snack-store products to their unit prices
    "BBQ Chips": 2.25,  # price for one bag of chips
    "Root Beer": 2.75,  # price for one bottle of root beer
    "Gummy Bears": 1.75,  # price for one bag of candy
    "Chocolate Cookies": 3.50,  # price for one pack of cookies
    "Turkey Sandwich": 5.50,  # price for one sandwich
}
shopping_cart = {}  # store each selected product name with its positive integer quantity


def display_menu():  # show the main menu
    print("\n========== SMART SHOPPING CART ==========\n")  # print the menu title
    print("1. View Available Products")  # option to see the store items
    print("2. Add Product to Cart")  # option to add an item
    print("3. Remove Product from Cart")  # option to remove one item
    print("4. View Shopping Cart")  # option to see the cart
    print("5. View Current Total")  # option to check the subtotal
    print("6. Checkout\n")  # option to finish shopping


def get_valid_number(prompt, maximum, error_message):  # ask until the number is valid
    while True:  # keep asking if they enter something invalid
        answer = input(prompt).strip()  # get the answer without extra spaces
        if answer.isdecimal():  # check if they entered a whole number
            choice = int(answer)  # change the answer into an integer
            if 1 <= choice <= maximum:  # make sure the number is in range
                return choice  # give back the valid choice
        print(error_message)  # show why the choice was rejected
        print(f"Please choose a number between 1 and {maximum}.\n")  # show the valid range


def display_products(products):  # show all products with their prices
    print("\n========== AVAILABLE PRODUCTS ==========\n")  # print the inventory title
    for number, (product, price) in enumerate(products.items(), start=1):  # number each product and price pair
        print(f"{number}. {product:<20} ${price:.2f}")  # show the matching name and price
    print()  # leave a space after the inventory


def get_price(product, products):  # find the price of a product
    return products[product]  # look up the unit price using the product name as the key


def add_product(products, shopping_cart):  # add the requested quantity of a product
    display_products(products)  # let the customer see what they can buy
    choice = get_valid_number("Enter product number: ", len(products), "Invalid product!")  # get a valid product number
    product_names = list(products)  # keep only names in the same order as the numbered inventory
    product = product_names[choice - 1]  # change the validated menu number into a product name
    while True:  # keep asking until the quantity is a positive whole number
        answer = input(f"How many {product} would you like to add? ").strip()  # ask for the number of units
        if answer.isdecimal():  # reject text, fractions, and negative numbers
            quantity = int(answer)  # convert the whole-number answer to an integer
            if quantity > 0:  # do not allow zero units
                break  # stop asking once the quantity is valid
        print("Please enter a whole number greater than 0.\n")  # explain which quantities are allowed
    if product in shopping_cart:  # check if the item is already there
        shopping_cart[product] += quantity  # add the requested units to the existing quantity
    else:  # handle products that are not in the cart yet
        shopping_cart[product] = quantity  # create one entry with the requested quantity
    print(f"\nAdded {quantity} {product} to your cart!")  # confirm the number of units added
    print(f"{product} quantity is now {shopping_cart[product]}.\n")  # show the updated quantity


def calculate_total(shopping_cart, products):  # calculate the cart subtotal
    subtotal = 0.0  # start the total at zero
    for product, quantity in shopping_cart.items():  # go through each product and its quantity
        price = get_price(product, products)  # get its inventory price
        subtotal += price * quantity  # add the price times its quantity
    return subtotal  # send the calculated subtotal back


def display_cart(shopping_cart, products):  # show the cart with quantities
    print("\n========== YOUR SHOPPING CART ==========\n")  # print the cart title
    if len(shopping_cart) == 0:  # check if there is anything in the cart
        print("Your shopping cart is empty!\n")  # explain why there are no items
        return  # stop because there is nothing to display
    print(f"   {'Product':<20} {'Unit Price':>10}   {'Quantity':>8}   {'Line Total':>10}")  # label the cart columns
    for number, (product, quantity) in enumerate(shopping_cart.items(), start=1):  # display each product and quantity once
        price = get_price(product, products)  # get its normal price
        item_total = price * quantity  # calculate the total for this product
        print(f"{number}. {product:<20} ${price:>9.2f}   {quantity:>8}   ${item_total:>9.2f}")  # show its unit price, quantity, and line total
    print(f"\nTotal Items: {sum(shopping_cart.values())}")  # count all units instead of just different products
    print(f"Subtotal: ${calculate_total(shopping_cart, products):.2f}\n")  # show the full cart subtotal


def remove_product(shopping_cart):  # remove one copy of a selected product
    if len(shopping_cart) == 0:  # check whether anything can be removed
        print("\nYour shopping cart is empty!")  # tell the customer the cart has no items
        print("There is nothing to remove.\n")  # explain why nothing changed
        return  # go back without changing the cart dictionary
    print("\n========== YOUR SHOPPING CART ==========\n")  # show the cart before removing
    for number, (product, quantity) in enumerate(shopping_cart.items(), start=1):  # number the products in the cart
        print(f"{number}. {product} - Quantity: {quantity}")  # show each product and quantity
    print()  # leave a space before asking
    choice = get_valid_number("Enter item number to remove: ", len(shopping_cart), "That item does not exist in your cart!")  # validate the cart position
    product_names = list(shopping_cart)  # match the numbered choices to the current cart keys
    product = product_names[choice - 1]  # look up the selected product after validation
    shopping_cart[product] -= 1  # remove exactly one unit
    print(f"\nRemoved 1 {product} from your cart!")  # confirm what was removed
    if shopping_cart[product] == 0:  # remove products that have no units left
        del shopping_cart[product]  # delete the name and quantity together
        print(f"{product} is no longer in your cart.\n")  # explain why the entry disappeared
    else:  # keep products that still have a positive quantity
        print(f"{product} quantity is now {shopping_cart[product]}.\n")  # show the amount left


def display_total(shopping_cart, products):  # show the current subtotal
    print("\n========== CURRENT TOTAL ==========\n")  # print the total title
    if len(shopping_cart) == 0:  # check if there are no items to calculate
        print("Your shopping cart is empty!")  # show the empty cart message
    for product, quantity in shopping_cart.items():  # list everything included in the total
        price = get_price(product, products)  # look up the item price
        print(f"{product:<20} x {quantity}    ${price * quantity:.2f}")  # show the quantity and line total
    subtotal = calculate_total(shopping_cart, products)  # add up the cart
    print(f"\nSubtotal: ${subtotal:.2f}\n")  # display the subtotal with two decimals


def calculate_discount(subtotal):  # find the discount rate from the subtotal
    if subtotal >= 40:  # orders of forty dollars or more save fifteen percent
        return 0.15  # give back the fifteen percent rate
    elif subtotal >= 20:  # orders of twenty to under forty save ten percent
        return 0.10  # give back the ten percent rate
    elif subtotal >= 10:  # orders of ten to under twenty save five percent
        return 0.05  # give back the five percent rate
    else:  # orders under ten dollars do not get a discount
        return 0.0  # give back a zero percent rate


def checkout(shopping_cart, products):  # print the final receipt if the cart is not empty
    if len(shopping_cart) == 0:  # block checkout if nothing was purchased
        print("\nYour shopping cart is empty! Add a product before checking out.\n")  # explain why checkout cannot finish
        return False  # tell the menu to keep running
    subtotal = calculate_total(shopping_cart, products)  # get the subtotal before discounts
    discount_rate = calculate_discount(subtotal)  # find which discount applies
    amount_saved = subtotal * discount_rate  # calculate how much money is saved
    final_total = subtotal - amount_saved  # subtract the savings from the subtotal
    today = datetime.date.today().strftime("%m/%d/%Y")  # format today's date for the receipt
    print("\n========== RECEIPT ==========\n")  # print the receipt title
    print(f"Date: {today}\n")  # print the current date
    print(f"{'Product':<20} {'Unit Price':>10}   {'Quantity':>8}   {'Line Total':>10}")  # label all required receipt columns
    for product, quantity in shopping_cart.items():  # print each purchased product on the receipt
        price = get_price(product, products)  # look up its price
        item_total = price * quantity  # calculate the cost of all units of this product
        print(f"{product:<20} ${price:>9.2f}   {quantity:>8}   ${item_total:>9.2f}")  # show its name, unit price, quantity, and line total
    print(f"\nTotal Items:    {sum(shopping_cart.values())}")  # include every purchased unit in the item count
    print(f"Subtotal:       ${subtotal:.2f}")  # show the cost before the discount
    print(f"Discount:       {discount_rate * 100:.0f}%")  # show the discount percent
    print(f"Amount Saved:   ${amount_saved:.2f}")  # show the actual savings
    print(f"\nFinal Total:    ${final_total:.2f}")  # show what the customer pays
    print("\nThank you for shopping!")  # finish the receipt
    return True  # tell the menu that checkout is complete


def main():  # run the shopping cart menu
    while True:  # repeat the menu until checkout succeeds
        display_menu()  # show the six options
        choice = get_valid_number("Enter your choice: ", 6, "Invalid option!")  # make sure the menu choice is valid
        if choice == 1:  # option one shows the inventory
            display_products(products)  # list every product and its price
        elif choice == 2:  # option two adds a product
            add_product(products, shopping_cart)  # add or increase its quantity
        elif choice == 3:  # option three removes a product
            remove_product(shopping_cart)  # remove one copy of the chosen product
        elif choice == 4:  # option four views the cart
            display_cart(shopping_cart, products)  # show the items and amounts
        elif choice == 5:  # option five calculates the current total
            display_total(shopping_cart, products)  # show all item totals and the subtotal
        elif choice == 6:  # option six attempts checkout
            if checkout(shopping_cart, products):  # only exit if the cart has items
                break  # stop repeating the menu after successful checkout


if __name__ == "__main__":  # only start the menu when this file is run directly
    main()  # launch the shopping cart program

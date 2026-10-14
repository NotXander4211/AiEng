import datetime  # get the date for the final receipt

products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]  # store the product names
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]  # keep each price at the same index as its product
shopping_cart = []  # start with an empty cart
quantities = []  # keep track of how many of each item are in the cart


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


def display_products(products, prices):  # show all products with their prices
    print("\n========== AVAILABLE PRODUCTS ==========\n")  # print the inventory title
    for i in range(len(products)):  # go through each product index
        print(f"{i + 1}. {products[i]:<12} ${prices[i]:.2f}")  # show the matching name and price
    print()  # leave a space after the inventory


def get_price(product, products, prices):  # find the price of a product
    index = products.index(product)  # find where the product is in the inventory
    return prices[index]  # get the price from the same index


def add_product(products, prices, shopping_cart, quantities):  # add one item to the cart
    display_products(products, prices)  # let the customer see what they can buy
    choice = get_valid_number("Enter product number: ", len(products), "Invalid product!")  # get a valid product number
    product = products[choice - 1]  # change the menu number into a product name
    if product in shopping_cart:  # check if the item is already there
        index = shopping_cart.index(product)  # find its position in the cart
        quantities[index] += 1  # add one to its quantity
        print(f"\n{product} quantity increased to {quantities[index]}!\n")  # show the new quantity
    else:  # handle products that are not in the cart yet
        shopping_cart.append(product)  # add the product name once
        quantities.append(1)  # start its quantity at one
        print(f"\n{product} was added to your cart!\n")  # confirm the new item


def calculate_total(shopping_cart, quantities, products, prices):  # calculate the cart subtotal
    subtotal = 0.0  # start the total at zero
    for i in range(len(shopping_cart)):  # go through each different product in the cart
        price = get_price(shopping_cart[i], products, prices)  # get its inventory price
        subtotal += price * quantities[i]  # add the price times its quantity
    return subtotal  # send the calculated subtotal back


def display_cart(shopping_cart, quantities, products, prices):  # show the cart with quantities
    print("\n========== YOUR SHOPPING CART ==========\n")  # print the cart title
    if len(shopping_cart) == 0:  # check if there is anything in the cart
        print("Your shopping cart is empty!\n")  # explain why there are no items
        return  # stop because there is nothing to display
    print("   Product       Price    Quantity    Total")  # label the cart columns
    for i in range(len(shopping_cart)):  # display each product once
        price = get_price(shopping_cart[i], products, prices)  # get its normal price
        item_total = price * quantities[i]  # calculate the total for this product
        print(f"{i + 1}. {shopping_cart[i]:<12} ${price:>5.2f}    {quantities[i]:<11} ${item_total:.2f}")  # show its price, amount, and total
    print(f"\nTotal Items: {sum(quantities)}")  # count every item including duplicates
    print(f"Subtotal: ${calculate_total(shopping_cart, quantities, products, prices):.2f}\n")  # show the full cart subtotal


def remove_product(shopping_cart, quantities):  # remove one copy of a selected product
    if len(shopping_cart) == 0:  # check whether anything can be removed
        print("\nYour shopping cart is empty!")  # tell the customer the cart has no items
        print("There is nothing to remove.\n")  # explain why nothing changed
        return  # go back without changing the lists
    print("\n========== YOUR SHOPPING CART ==========\n")  # show the cart before removing
    for i in range(len(shopping_cart)):  # number the products in the cart
        print(f"{i + 1}. {shopping_cart[i]} - Quantity: {quantities[i]}")  # show each product and quantity
    print()  # leave a space before asking
    choice = get_valid_number("Enter item number to remove: ", len(shopping_cart), "That item does not exist in your cart!")  # validate the cart position
    index = choice - 1  # turn the chosen number into a list index
    product = shopping_cart[index]  # save the product name before changing the cart
    if quantities[index] > 1:  # keep the product if there is more than one
        quantities[index] -= 1  # remove only one copy
        print(f"\nOne {product} was removed!")  # confirm what was removed
        print(f"{product} quantity is now {quantities[index]}.\n")  # show the amount left
    else:  # remove the entry completely if only one was left
        shopping_cart.pop(index)  # remove the product name
        quantities.pop(index)  # remove its matching quantity too
        print(f"\n{product} was removed from your cart!\n")  # confirm the product is gone


def display_total(shopping_cart, quantities, products, prices):  # show the current subtotal
    print("\n========== CURRENT TOTAL ==========\n")  # print the total title
    if len(shopping_cart) == 0:  # check if there are no items to calculate
        print("Your shopping cart is empty!")  # show the empty cart message
    for i in range(len(shopping_cart)):  # list everything included in the total
        price = get_price(shopping_cart[i], products, prices)  # look up the item price
        print(f"{shopping_cart[i]:<12} x {quantities[i]}    ${price * quantities[i]:.2f}")  # show the quantity and line total
    subtotal = calculate_total(shopping_cart, quantities, products, prices)  # add up the cart
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


def checkout(shopping_cart, quantities, products, prices):  # print the final receipt if the cart is not empty
    if len(shopping_cart) == 0:  # block checkout if nothing was purchased
        print("\nYour shopping cart is empty! Add a product before checking out.\n")  # explain why checkout cannot finish
        return False  # tell the menu to keep running
    subtotal = calculate_total(shopping_cart, quantities, products, prices)  # get the subtotal before discounts
    discount_rate = calculate_discount(subtotal)  # find which discount applies
    amount_saved = subtotal * discount_rate  # calculate how much money is saved
    final_total = subtotal - amount_saved  # subtract the savings from the subtotal
    today = datetime.date.today().strftime("%m/%d/%Y")  # format today's date for the receipt
    print("\n========== RECEIPT ==========\n")  # print the receipt title
    print(f"Date: {today}\n")  # print the current date
    for i in range(len(shopping_cart)):  # print each purchased product on the receipt
        price = get_price(shopping_cart[i], products, prices)  # look up its price
        print(f"{shopping_cart[i]:<12} x {quantities[i]}    ${price * quantities[i]:.2f}")  # show the quantity and item total
    print(f"\nSubtotal:       ${subtotal:.2f}")  # show the cost before the discount
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
            display_products(products, prices)  # list every product and its price
        elif choice == 2:  # option two adds a product
            add_product(products, prices, shopping_cart, quantities)  # add or increase its quantity
        elif choice == 3:  # option three removes a product
            remove_product(shopping_cart, quantities)  # remove one copy of the chosen product
        elif choice == 4:  # option four views the cart
            display_cart(shopping_cart, quantities, products, prices)  # show the items and amounts
        elif choice == 5:  # option five calculates the current total
            display_total(shopping_cart, quantities, products, prices)  # show all item totals and the subtotal
        elif choice == 6:  # option six attempts checkout
            if checkout(shopping_cart, quantities, products, prices):  # only exit if the cart has items
                break  # stop repeating the menu after successful checkout


if __name__ == "__main__":  # only start the menu when this file is run directly
    main()  # launch the shopping cart program

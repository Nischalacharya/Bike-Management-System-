# Importing for a regular expression
import re

# Defining a function to order bikes from the library that accepts the following 2D list as the parameter
def bike_order(listed_items):
    global initial_amount1, initial_amount2, initial_amount3, initial_amount4, initial_amount5
    global initial_amount6, initial_amount7, initial_amount8, initial_amount9, initial_amount10
    # Assigning the parameter list to the new variable and declaring an empty dictionary
    list_data = listed_items
    dictionary_data = {}
    print()
    print("We would like to greet you with a warm welcome to our Bike Store.")
    print()
    # Asking the user to input their company names and checking through the regular expression if correct values are entered
    shipment_company = input("What is the name of your Shipping Company? ")
    shipment_address = input("What is the address of your Shipping company? ")
    #Use of a loop in order for the user to input their valid names
    while True:
        try:
            # Asking the user to input their contact and checking through the regular expression if correct values are entered
            shipment_contact = int(input("What is the conatct of your Shipping Company? "))
            break
        except:
            print()
            print("Add only integer values for contact")
        
    

    ordering_bike = True
    while ordering_bike:
        print()
        bike_id = (input("Enter the ID of the bike you wish to order: ")).upper()
        # Iterating the code entered with every element's first index stored on the list
        if bike_id == list_data[0][0] or bike_id == list_data[1][0] or bike_id == list_data[2][0] or\
                bike_id == list_data[3][0] or bike_id == list_data[4][0] or bike_id == list_data[5][0] or \
                bike_id == list_data[6][0] or bike_id == list_data[7][0] or bike_id == list_data[8][0] or \
                bike_id == list_data[9][0]:
            while True:
                 # Exception Handling to handle for any other values than integer
                try:
                    bike_quantity = int(input("Enter the number of bikes you wish to order: "))
                    if bike_quantity > 0:
                        break
                    elif bike_quantity < 0:
                        print("Please enter a positive integer value.")
                        print()
                    elif bike_quantity == 0:
                        print("Print enter a positive integer value.")
                        print()
                except:
                    print("Please enter an integer value.")
                    print()

            # Iterating through the lists to check if the inserted bike quantity has the actual number of stocks in the store
            # Adding the quantity of bike as the value and bike code as its key on the dictionary initialized

            if bike_id == list_data[0][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[1][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[2][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[3][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[4][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[5][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[6][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[7][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[8][0]:
                dictionary_data[bike_id] = bike_quantity
            elif bike_id == list_data[9][0]:
                dictionary_data[bike_id] = bike_quantity
            # Error message when the quantity inputted is greater than the bikes in stock
            else:
                print("Sorry, the Bike is out of stock.")

        # Error message when an invalid bike code has been entered

        else:
            print()
            print("Sorry, the bike with the ID " + bike_id + " has not been added on our store. You can only order the "
                                                             "bikes present in our store.")
        # Use of while loop in order to iterate through the user interface till a correct value is entered
        while True:
            print()
            supplement = input("Do you wish to order any more bikes (Y/N)? ").upper()
            # if yes loop through the top
            if supplement == "Y":
                ordering_bike = True
                break
             # if not, break the loop
            elif supplement == "N":
                ordering_bike = False
                break
            # if an invalid value is provided loop through it again
            else:
                print("Invalid input, try again.")
                continue
    # Calculation of the price to be paid and the grand total due

    print()
    amount = 0
    # Iterating through the keys of the dictionary to calculate the total amount by multiplying the value with its unit price
    # Iterating through every elements stored on the dictionary and calculating the amount of each bike and grand total
    for keys in dictionary_data.keys():
        if keys == list_data[0][0]:
            price = int(list_data[0][5])
            number1 = int(dictionary_data[keys])
            initial_amount1 = (price * number1)
            amount = amount + (price * number1)
            print("The total cost for the bike with ID" + list_data[0][0] + " and title " + list_data[0][
                1] + "is:" + "$" + str(initial_amount1))

        if keys == list_data[1][0]:
            price = int(list_data[1][5])
            number2 = int(dictionary_data[keys])
            initial_amount2 = (price * number2)
            amount = amount + (price * number2)
            print("The total cost for the bike with ID" + list_data[1][0] + " and title " + list_data[1][
                1] + "is:" + "$" + str(initial_amount2))

        if keys == list_data[2][0]:
            price = int(list_data[2][5])
            number3 = int(dictionary_data[keys])
            initial_amount3 = (price * number3)
            amount = amount + (price * number3)
            print("The total cost for the bike with ID" + list_data[2][0] + " and title " + list_data[2][
                1] + "is:" + "$" + str(initial_amount3))

        if keys == list_data[3][0]:
            price = int(list_data[3][5])
            number4 = int(dictionary_data[keys])
            initial_amount4 = (price * number4)
            amount = amount + (price * number4)
            print("The total cost for the bike with ID" + list_data[3][0] + " and title " + list_data[3][
                1] + "is:" + "$" + str(initial_amount4))

        if keys == list_data[4][0]:
            price = int(list_data[4][5])
            number5 = int(dictionary_data[keys])
            initial_amount5 = (price * number5)
            amount = amount + (price * number5)
            print("The total cost for the bike with ID" + list_data[4][0] + " and title " + list_data[4][
                1] + "is:" + "$" + str(initial_amount5))

        if keys == list_data[5][0]:
            price = int(list_data[5][5])
            number6 = int(dictionary_data[keys])
            initial_amount6 = (price * number6)
            amount = amount + (price * number6)
            print("The total cost for the bike with ID" + list_data[5][0] + " and title " + list_data[5][
                1] + "is:" + "$" + str(initial_amount6))

        if keys == list_data[6][0]:
            price = int(list_data[6][5])
            number7 = int(dictionary_data[keys])
            initial_amount7 = (price * number7)
            amount = amount + (price * number7)
            print("The total cost for the bike with ID" + list_data[6][0] + " and title " + list_data[6][
                1] + "is:" + "$" + str(initial_amount7))

        if keys == list_data[7][0]:
            price = int(list_data[7][5])
            number8 = int(dictionary_data[keys])
            initial_amount8 = (price * number8)
            amount = amount + (price * number8)
            print("The total cost for the bike with ID" + list_data[7][0] + " and title " + list_data[7][
                1] + "is:" + "$" + str(initial_amount8))

        if keys == list_data[8][0]:
            price = int(list_data[8][5])
            number9 = int(dictionary_data[keys])
            initial_amount9 = (price * number9)
            amount = amount + (price * number9)
            print("The total cost for the bike with ID" + list_data[8][0] + " and title " + list_data[8][
                1] + "is:" + "$" + str(initial_amount9))

        if keys == list_data[9][0]:
            price = int(list_data[9][5])
            number10 = int(dictionary_data[keys])
            initial_amount10 = (price * number10)
            amount = amount + (price * number10)
            print("The total cost for the bike with ID" + list_data[9][0] + " and title " + list_data[9][
                1] + "is:" + "$" + str(initial_amount10))
    # Printing the output as the total amount or sum of all bikes as the grand total
    print("Hence the total amount for all the bikes is: " + "$" + str(amount))

    # Creation of ordered notice invoice for the ordered bikes
    # Extraction of date and time to add on the txt file 
    import datetime
    date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)
    time = str(datetime.datetime.now().hour) + "-" + str(datetime.datetime.now().minute) + "-" + str(
        datetime.datetime.now().second)
    date_time = str(date) + " " + str(time)
    # File writing with the user's name, date and time and transaction made and other details
    file_write = open(shipment_company + " " + date_time + " (Ordered).txt", "w")
    file_write.write(
        "------------------------------------------------------ INVOICE NOTE ------------------------------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write(
        "------------------------------------------------------- ORDER BIKE -------------------------------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write("\n")
    file_write.write(str("\t\tName of the Company: " + str(shipment_company) + "\t\t\t" + "Date: " + str(
        date) + "\t\t\t\t " + "Time: " + str(time)))
    file_write.write("\n")
    file_write.write(str("\t\tAddress of the Company: " + str(shipment_address) + "\t\t\t" + "Contact: " + str(shipment_contact)))
    file_write.write("\n")
    file_write.write(
        "--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write(
        "\tBike ID\t\tBike Name\t\tBike Manufacturer\tBike Color\t\tBike Quantity\t\tUnit Price\t\t Amount")
    file_write.write("\n")
    # Iterating through the keys of the dictionary to find out the total amount to be paid 
    for keys in dictionary_data.keys():
        if keys == list_data[0][0]:
            file_write.write(str("\t " + str(list_data[0][0]) + "\t\t" + str(list_data[0][1]) + "\t\t  " + str(
                list_data[0][2]) + "\t\t" + str(list_data[0][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[0][5]) + "\t\t" + "$" + str(initial_amount1)))
            file_write.write("\n")
        if keys == list_data[1][0]:
            file_write.write(str("\t " + str(list_data[1][0]) + "\t\t" + str(list_data[1][1]) + "\t\t  " + str(
                list_data[1][2]) + "\t\t" + str(list_data[1][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[1][5]) + "\t\t" + "$" + str(initial_amount2)))
            file_write.write("\n")
        if keys == list_data[2][0]:
            file_write.write(str("\t " + str(list_data[2][0]) + "\t\t" + str(list_data[2][1]) + "\t\t  " + str(
                list_data[2][2]) + "\t\t" + str(list_data[2][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[2][5]) + "\t\t" + "$" + str(initial_amount3)))
            file_write.write("\n")
        if keys == list_data[3][0]:
            file_write.write(str("\t " + str(list_data[3][0]) + "\t\t" + str(list_data[3][1]) + "\t\t  " + str(
                list_data[3][2]) + "\t\t" + str(list_data[3][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[3][5]) + "\t\t" + "$" + str(initial_amount4)))
            file_write.write("\n")
        if keys == list_data[4][0]:
            file_write.write(str("\t " + str(list_data[4][0]) + "\t\t" + str(list_data[4][1]) + "\t\t  " + str(
                list_data[4][2]) + "\t\t" + str(list_data[4][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[4][5]) + "\t\t" + "$" + str(initial_amount5)))
            file_write.write("\n")
        if keys == list_data[5][0]:
            file_write.write(str("\t " + str(list_data[5][0]) + "\t\t" + str(list_data[5][1]) + "\t\t  " + str(
                list_data[5][2]) + "\t\t" + str(list_data[5][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[0][5]) + "\t\t" + "$" + str(initial_amount6)))
            file_write.write("\n")
        if keys == list_data[6][0]:
            file_write.write(str("\t " + str(list_data[6][0]) + "\t\t" + str(list_data[6][1]) + "\t\t  " + str(
                list_data[6][2]) + "\t\t" + str(list_data[6][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[6][5]) + "\t\t" + "$" + str(initial_amount7)))
            file_write.write("\n")
        if keys == list_data[7][0]:
            file_write.write(str("\t " + str(list_data[7][0]) + "\t\t" + str(list_data[7][1]) + "\t\t  " + str(
                list_data[7][2]) + "\t\t" + str(list_data[7][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[7][5]) + "\t\t" + "$" + str(initial_amount8)))
            file_write.write("\n")
        if keys == list_data[8][0]:
            file_write.write(str("\t " + str(list_data[8][0]) + "\t\t" + str(list_data[8][1]) + "\t\t  " + str(
                list_data[8][2]) + "\t\t" + str(list_data[8][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[3][5]) + "\t\t" + "$" + str(initial_amount9)))
            file_write.write("\n")
        if keys == list_data[9][0]:
            file_write.write(str("\t " + str(list_data[9][0]) + "\t\t" + str(list_data[9][1]) + "\t\t  " + str(
                list_data[9][2]) + "\t\t" + str(list_data[9][3]) + "\t\t    " + str(
                dictionary_data[keys]) + "\t\t         " + "$" + str(
                list_data[4][5]) + "\t\t" + "$" + str(initial_amount10)))
            file_write.write("\n")

            
    # Writing of the total amount to be paid with a final notice   
    file_write.write(
        "-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.write("\t\t\t\t\t\t\t\t\t Total_Amount: " + "$" + str(amount))
    file_write.write("\n")
    file_write.write(
        "------------------------------------------------------------------------THANKYOU------------------------------------------------------------------------------------")
    file_write.write("\n")
    file_write.close()
    # It returns the dictionary that stored the details of bike code and bike ordered
    return dictionary_data

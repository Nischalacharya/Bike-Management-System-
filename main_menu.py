# Importing all the python files which includes file handling, bike transcation and overwriting the txt files along with the date and time
import read_file
import order_bike
import overwrite_list
import datetime
import sell_bike

# Defining a main menu to compile all the functions and call them accordingly
def main_menu():
    # Display of the main menu interface after the program is executed 
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------|")
    print()
    print("\t\t\t\t\t\t\t\t BIKE MANAGEMENT SYSTEM \n ")
    print("\t\t\t\t\t\t\t\t Today's Date: " + str(datetime.datetime.now().year) + "/" + str(
        datetime.datetime.now().month) + "/" + str(datetime.datetime.now().day))
    
    # Provide details to perform a specific action the user wants
    while True:
        print()
        print("\t\t\t\t\t\t\t\tPress [1] to view all the available bikes. ")
        print("\t\t\t\t\t\t\t\tPress [2] to order bikes. ")
        print("\t\t\t\t\t\t\t\tPress [3] to sell all the bikes.")
        print("\t\t\t\t\t\t\t\tPress [4] to exit the store.")
        print()
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print()
        
        # Ask for the user to input the action to be performed
        action = input("Enter the action you want to perform: ")
        # Calling the function of file reading when the user wants to view all the available bikes
        if action == "1":
            read_file.read_file()
        # Calling the function of file reading when the user wants to order all the available bikes
        elif action == "2":
            x = read_file.read_file()
            y = order_bike.bike_order(x)
            overwrite_list.over_writing_order(x, y)
            print()
            ask_again = input("Do you wish to proceed for more transactions (Y/N)? ")
            print()
            print("-----------------------------------------------------")
            if ask_again == "N":
                break
        # Calling the function of file reading when the user wants to sell all the available bikes
        elif action == "3":
            x = read_file.read_file()
            y = sell_bike.sell_bike(x)
            overwrite_list.over_writing_sell(x, y)
            # Ask the user to if they'd wish to progress with another transaction or not
            print()
            ask_again = input("Do you wish to proceed for more transactions (Y/N)? ")
            print()
            print("-----------------------------------------------------")
            if ask_again == "N":
                break

        elif action == "4":
            break

         # For an invalid value entered and then loop throughout

        else:
            print("Invalid input.")
            print()
            print("-----------------------------------------------")

    print()
    print("\t\t\t\t\t\t\t\tThank you for visiting our Store.")
    print()
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------|")

# Calling of the main menu function to perform all the actions  
main_menu()

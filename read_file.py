# Defining a function to read the details of a file and store it on a two dimensional list
def read_file():
    # Openining of the file that contains the information about the bikes
    file = open("bike_list.txt", "r")
    # Use of readlines function in order to store the deatils on a list
    files = file.readlines()
    list_data = []
    # Appending all the details of the book on a new list
    for line in files:
        list_data.append(line.replace("\n", "").split(","))
    file.close()
    serial_id = 1
    # Display of all the details of the bike in an appropriate matter in order to make it user friendly
    print()
    print("+---------------------------------------------------+---------------------------------------------------+-------------------------------------+--------------|")
    print("|\t\t\t\t\t\t\t\t  Bike Management System\t\t\t\t\t\t\t             |")
    print("+---------------------------------------------------+---------------------------------------------------+-------------------------------------+--------------|")
    print("|  Bike ID\t|\tBike Name\t|\tBike Manufacturer\t|\tBike Color\t|\tBike Quantity           |    Bike Price\t             |")
    print("+---------------------------------------------------+---------------------------------------------------+--------------------------------------+-------------|")
    for i in range(len(list_data)):
        print("|\t" + str(list_data[i][0]) + "\t|\t" + str(list_data[i][1]) + "\t|\t " + str(
            list_data[i][2]) + "\t\t|  " +      str(list_data[i][3]) + "\t\t|\t" + str(list_data[i][4]) + "   \t\t\t|\t " + str(
            list_data[i][5]) + "\t\t     |")
    print("+---------------------------------------------------+---------------------------------------------------+--------------------------------------+-------------|")
    return list_data
# It returns the list that stored the details of the bikes on the 2D list
read_file()

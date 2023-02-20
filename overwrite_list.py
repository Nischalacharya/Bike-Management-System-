# Defining a function to overwrite the txt file which accepts the list and dictionary as its parameters
def over_writing_order(listed_troops, dictionary_troops):
    # Assigning the returned list from bike read to a new variable
    list_data = listed_troops
    # Assigning the returned dictionary from order  to a new variable
    dictionary_data = dictionary_troops
    # Examining the index of the list and then adding from its respective key of the dictionary
    for keys in dictionary_data.keys():
        if keys == list_data[0][0]:
            list_data[0][4] = str(int(list_data[0][4]) + int(dictionary_data[keys]))
        if keys == list_data[1][0]:
            list_data[1][4] = str(int(list_data[1][4]) + int(dictionary_data[keys]))
        if keys == list_data[2][0]:
            list_data[2][4] = str(int(list_data[2][4]) + int(dictionary_data[keys]))
        if keys == list_data[3][0]:
            list_data[3][4] = str(int(list_data[3][4]) + int(dictionary_data[keys]))
        if keys == list_data[4][0]:
            list_data[4][4] = str(int(list_data[4][4]) + int(dictionary_data[keys]))
        if keys == list_data[5][0]:
            list_data[5][4] = str(int(list_data[5][4]) + int(dictionary_data[keys]))
        if keys == list_data[6][0]:
            list_data[6][4] = str(int(list_data[6][4]) + int(dictionary_data[keys]))
        if keys == list_data[7][0]:
            list_data[7][4] = str(int(list_data[7][4]) + int(dictionary_data[keys]))
        if keys == list_data[8][0]:
            list_data[8][4] = str(int(list_data[8][4]) + int(dictionary_data[keys]))
        if keys == list_data[9][0]:
            list_data[9][4] = str(int(list_data[9][4]) + int(dictionary_data[keys]))

    # Displaying of the new updated list after increasing the amount of bike stock

    print()
    print("The new updated list is as follows: ")
    for element in list_data:
        print(element)
    # File writing to update the quantity of the bike stock after ordering
    files = open("bike_list.txt", "w")
    for each in list_data:
        files.write(str(",".join(each)))
        files.write("\n")
    files.close()
    return

# Defining a function to overwrite the txt file which accepts the list and dictionary as its parameters
def over_writing_sell(listed_troops, dictionary_troops):
      # Assigning the returned list from bike read to a new variable
    
    list_data = listed_troops
     # Assigning the returned dictionary from order  to a new variable
    
    dictionary_data = dictionary_troops
    # Examining the index of the list and then substracting from its respective key of the dictionary
    for keys in dictionary_data.keys():
        if keys == list_data[0][0]:
            list_data[0][4] = str(int(list_data[0][4]) - int(dictionary_data[keys]))
        if keys == list_data[1][0]:
            list_data[1][4] = str(int(list_data[1][4]) - int(dictionary_data[keys]))
        if keys == list_data[2][0]:
            list_data[2][4] = str(int(list_data[2][4]) - int(dictionary_data[keys]))
        if keys == list_data[3][0]:
            list_data[3][4] = str(int(list_data[3][4]) - int(dictionary_data[keys]))
        if keys == list_data[4][0]:
            list_data[4][4] = str(int(list_data[4][4]) - int(dictionary_data[keys]))
        if keys == list_data[5][0]:
            list_data[5][4] = str(int(list_data[5][4]) - int(dictionary_data[keys]))
        if keys == list_data[6][0]:
            list_data[6][4] = str(int(list_data[6][4]) - int(dictionary_data[keys]))
        if keys == list_data[7][0]:
            list_data[7][4] = str(int(list_data[7][4]) - int(dictionary_data[keys]))
        if keys == list_data[8][0]:
            list_data[8][4] = str(int(list_data[8][4]) - int(dictionary_data[keys]))
        if keys == list_data[9][0]:
            list_data[9][4] = str(int(list_data[9][4]) - int(dictionary_data[keys]))

    # Displaying of the new updated list after reducing the amount of bike stock

    print()
    print("The new updated list is as follows: ")
    for element in list_data:
        print(element)

    # File writing to update the quantity of the bike stock after selling
    files = open("bike_list.txt", "w")
    for each in list_data:
        files.write(str(",".join(each)))
        files.write("\n")
    files.close()
    return

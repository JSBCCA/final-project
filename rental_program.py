""" Module Docstring """
import sys

def list_inventory():
    """
    Returns inventory as a list of lists.
    item, num in stock, total stock, price for rental, replacement cost
    """
    with open("stock_inventory.csv", "r") as file:
        stock = file.read().splitlines()
    # open the csv and read each line
    list_of_lists = []
    for line in stock:
        split_line = line.split(", ")
        for i in range(len(split_line)):
            if len(split_line[i]) <= 4:
                split_line[i] = int(split_line[i])
                # turn numbers into type int
        list_of_lists.append(split_line)
    # separate each line by comma, then put each list into one big list
    return list_of_lists

def list_to_text(list_of_list):
    """
    Converts list of lists into a string.
    """
    final_string = ""
    for line in list_of_list:
        for item in line:
            if item != line[-1]:
                final_string += str(item) + ", "
            else:
                final_string += str(item)
        if line != list_of_list[-1]:
            final_string += "\n"
    return final_string
def show_inventory(list_of_lists):
    """
    Shows the inventory to the user.
    """
    final_string = ""
    for si_list in list_of_lists:
        if si_list[1] > 0:
            final_string += si_list[0] + ": In Stock\n"
        else:
            final_string += si_list[0] + ": Out of Stock\n"
    return final_string



def th_question():
    """
    If t: make transaction
    If h: show transaction history
    If i: show inventory
    If q: quit program
    """
    print("Enter 't' to make a transaction.")
    print("Enter 'h' to show transaction history.")
    print("Enter 'i' to show the inventory.")
    print("Enter 'q' at any time to quit.")
    answer = input().lower()
    if answer == "q":
        # quit
        sys.exit()
    elif answer == "h":
        # show transaction history
        print("\n" + show_transaction_history())
    elif answer == "i":
        # show inventory
        print("\n" + show_inventory(list_inventory()))
    elif answer == "t":
        # make transaction
        item_info = item_question(r_question())
        edit_inventory(item_info)
        edit_transaction_history(item_info)
        print("Thank you for your business!")
        if item_info[1] == "returning":
            print("Your deposit has been returned to you.")
    else:
        print("\nPlease enter one of the 4 letters.\n")
        th_question()


def r_question():
    """
    Asks the user whether they’re renting, returning, or replacing an item.
    """
    answer = input("\nAre you renting, returning, or replacing the item?\n").lower()
    # if answer doesn't == one of the r's, loop
    if answer == "q":
        sys.exit()
    elif (answer != "renting") and (answer != "returning") and (answer != "replacing"):
        return r_question()
    else:
        return answer

def item_question(user_words):
    """
    Asks the user which item they are renting/returning/replacing.
    """
    answer = input("\nWhat item are you " + str(user_words) + "?\n").lower()
    if answer == "q":
        sys.exit()
    return [answer, user_words]


def edit_inventory(name_and_status):
    """
    Takes the user’s input and tells the inventory what items to take out/put in.
    """
    if name_and_status[1] == "renting":
        transaction = editfor_renting(name_and_status[0])
    elif name_and_status[1] == "returning":
        transaction = editfor_returning(name_and_status[0])
    elif name_and_status[1] == "replacing":
        transaction = editfor_replacing(name_and_status[0])
    else:
        return "Error!"
    return transaction

def editfor_renting(item_name):
    """
    If the user is renting, this should edit the inventory to account for that.
    """
    list_of_inv = list_inventory()
    namelist = []
    # make changes to the list_of_inv
    changed_inv = []
    for line in list_of_inv:
        namelist.append(line[0].lower())
        if line[0].lower() == item_name:
            if line[1] > 0:
                line[1] = line[1] - 1
            else:
                print("\nSorry, that item is out of stock!")
                return "Sorry, that item is out of stock!"
        changed_inv.append(line)
    if item_name in namelist:
        # change lists back to text
        text_inv = list_to_text(changed_inv)
        # write to file
        with open("stock_inventory.csv", "w") as file:
            file.write(text_inv)
        print("\nWe'll be taking a 10% deposit.")
        return "Grabbing item..."
    else:
        print("\nSorry, we don't have that item!")
        sys.exit()

def editfor_returning(item_name):
    """
    If the user is returning, this should edit the inventory to account for that.
    """
    list_of_inv = list_inventory()
    namelist = []
    # make changes to the list_of_inv
    changed_inv = []
    for line in list_of_inv:
        namelist.append(line[0].lower())
        if line[0].lower() == item_name:
            if line[1] < line[2]:
                line[1] = line[1] + 1
            else:
                print("\nSorry, our stock of that item is full!")
                return "Sorry, our stock of that item is full!"
        changed_inv.append(line)
    if item_name in namelist:
        # change lists back to text
        text_inv = list_to_text(changed_inv)
        # write to file
        with open("stock_inventory.csv", "w") as file:
            file.write(text_inv)
        return "Grabbing item..."
    else:
        print("\nSorry, we don't have that item!")
        sys.exit()

def editfor_replacing(item_name):
    """
    If the user is replacing, this should edit the inventory to account for that.
    """
    # with open("stock_inventory.csv", "w") as file:
    #     file.write(variable)
    return "Replacing item..."

def show_transaction_history():
    """
    Shows the user the transaction history.
    """
    with open("transactions.txt", "r") as file:
        trans = file.read()
    return trans


def edit_transaction_history(info_and_status):
    """
    Takes the item's info and status (one of the 3 r's) and updates the transaction history.
    [item name, item status]
    """
    # with open("transactions.txt", "w") as file:
    #     file.write(variable)
    return info_and_status[0]  # return that the transaction succeeded, maybe

th_question()

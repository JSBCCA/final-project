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
    print("Enter 'q' to quit.")
    answer = input()
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
        edit_inventory(item_question(r_question()))
    else:
        print("\nPlease enter one of the 4 letters.")
        # loop back over when this happens

def r_question():
    """
    Asks the user whether they’re renting, returning, or replacing an item.
    """
    answer = input("Are you renting, returning, or replacing the item?\n")
    # if answer doesn't == one of the r's, loop
    return answer

def item_question(user_words):
    """
    Asks the user which item they are renting/returning/replacing.
    """
    answer = input("What item are you " + str(user_words) + "?\n")
    return [answer, user_words]

def edit_inventory(name_and_status):
    """
    Takes the user’s input and tells the inventory what items to take out/put in.
    """
    if name_and_status[1] == "renting":
        # user needs to pay and make deposit here
        transaction = editfor_renting(name_and_status[0])
    elif name_and_status[1] == "returning":
        # deposit will be returned here
        transaction = editfor_returning(name_and_status[0])
    elif name_and_status[1] == "replacing":
        # deposit won't be returned here
        transaction = editfor_replacing(name_and_status[0])
    else:
        return "Error!"
    return transaction

def editfor_renting(something):
    """
    If the user is renting, this should edit the inventory for that
    """
    with open("stock_inventory.csv", "w") as file:
        stock = file.write()
    return something

def editfor_returning(something):
    """
    If the user is returning, this should edit the inventory for that
    """
    with open("stock_inventory.csv", "w") as file:
        stock = file.write()
    return something

def editfor_replacing(something):
    """
    If the user is replacing, this should edit the inventory for that
    """
    with open("stock_inventory.csv", "w") as file:
        stock = file.write()
    return something

def edit_transaction_history(info_and_status):
    """
    Takes the item's info and status and updates the transaction history.
    """
    with open("transactions.txt", "w") as file:
        trans = file.write()
    return info_and_status[0]

def show_transaction_history():
    """
    Shows the user the transaction history.
    """
    with open("transactions.txt", "r") as file:
        trans = file.read()
    return trans

th_question()

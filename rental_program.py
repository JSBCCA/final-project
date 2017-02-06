""" Module Docstring """

def edit_inventory(name, status):
    """
    Takes the user’s input and tells the inventory what items to take out/put in.
    """
    if status == "i":
        name = 4
        new_info = name + 1
    return new_info
    # words should be the name of an item and status is either renting/returning/replacing

def transaction_history(info, status):
    """
    Takes the item info and status and updates the transaction history.
    """
    return info + status
    # change transaction history

def read_inventory():
    """
    Reads from the inventory.
    """
    with open("stock_inventory.csv", "r") as file:
        stock = file.read()
    return stock

def show_inventory():
    """
    Returns inventory to the user.
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

def th_question():
    """
    If t: make transaction
    If h: show transaction history
    If i: show inventory
    If q: quit program
    """
    answer = input()
    if answer == "q":
        answer = answer
    return answer

def r_question():
    """
    Asks the user whether they’re renting, returning, or replacing an item.
    """
    answer = input("Are you renting, returning, or replacing the item?")
    return answer

def item_question(user_words):
    """
    Asks the user which item they are renting/returning/replacing.
    """
    answer = input("What item are you " + str(user_words) + "?")
    return answer

print(read_inventory())

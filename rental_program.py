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

def show_inventory():
    """
    Returns inventory to the user.
    """
    with open(..., ...):
        ...
    # open inventory and save as a variable. Return that variable
    return "what does this return? gotta return something"

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
    answer = input()
    return answer

def item_question(user_words):
    """
    Asks the user which item they are renting/returning/replacing.
    """
    answer = input("What item are you " + str(user_words) + "?")
    return answer

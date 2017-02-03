""" Module Docstring """

def edit_inventory(words, status):
    """
    Takes the user’s input and tells the inventory what items to take out/put in.
    """
    if status == "i":
        words = 4
        new_info = words + 1
    return new_info
    # words should be the name of an item and status is either renting/returning/replacing

def transaction_history():
    """
    Takes the item info and status and updates the transaction history.
    """
    return "what does this return?"
    # change transaction history

def show_inventory():
    """
    Returns inventory to the user.
    """
    # open inventory and save as a variable. Return that variable
    return False

def th_question():
    """
    If t: make transaction
    If h: show transaction history
    If i: show inventory
    If q: quit program
    """
    return "hi"

def r_question():
    """
    Asks the user whether they’re renting, returning, or replacing an item.
    """
    return "what the user says"

def item_question():
    """
    Asks the user which item they are renting/returning/replacing.
    """
    return "name of the item"

def return_price(pri):
    """
    Returns the price to the user.
    """
    return str(pri)

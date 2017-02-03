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
    return "what does this return? gotta return something"
    # change transaction history

def show_inventory():
    """
    Returns inventory to the user.
    """
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
    answer = input("yada yada" + str(user_words) + "yada yada")
    return answer

def return_price(pri):
    """
    Returns the price to the user.
    """
    return str(pri)

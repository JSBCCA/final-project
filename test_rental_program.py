""" Module Docstring """
import rental_program

def test_edit_inventory():
    """ Takes the user’s input and tells the inventory what items to take out/put in. """
    assert rental_program.edit_inventory("sdsaj", "dkj") == "Error!"
    assert rental_program.edit_inventory("actual item", "renting") == "Grabbing item..."
    assert rental_program.edit_inventory("actual item", "returning") == "Restocking item..."
    assert rental_program.edit_inventory('out of stock item', "renting") == """Sorry, that item
is out of stock!"""

def test_transaction_history():
    """ Takes the user’s input and adds new info to the transaction history. """
    assert rental_program.transaction_history() == "Added."

def test_show_inventory():
    """ Returns inventory to the user. """
    assert rental_program.show_inventory() is False

def test_th_question():
    """ Asks the user if they want to view transaction history,
    view inventory, make a transaction, or quit. """
    assert rental_program.th_question() == "i" or "t" or "h"
    # should return t, i, h, or q

def test_r_question():
    """ Asks the user whether they’re renting, returning, or replacing an item. """
    assert rental_program.r_question() == "fakjk"

def test_item_question():
    """ Asks the user which item they are renting/returning/replacing. """
    assert rental_program.item_question() == "one of the three r's"
    # type of rental_program.item_question() equals string

def test_return_price():
    """ Returns the price to the user. """
    assert rental_program.return_price(50) == "50"
    #  should take in the price and return a string with the price in it

""" Module Docstring """
import rental_program


def test_edit_inventory():
    """ Takes the user’s input and tells the inventory what items to take out/put in. """
    assert rental_program.edit_inventory("sdsaj", "dkj") == "Error updating inventory."
    assert rental_program.edit_inventory("actual item",
                                         "renting") == "Grabbing item..."
    assert rental_program.edit_inventory("actual item",
                                         "returning") == "Restocking item..."
    assert rental_program.edit_inventory("actual item",
                                         "replacing") == "Replacing item..."
    assert rental_program.edit_inventory('out of stock item',
                                         "renting") == """Sorry, that item is out of stock!"""


def test_edit_transaction_history():
    """ Takes the user’s input and adds new info to the transaction history. """
    assert rental_program.edit_transaction_history("item", "renting") == "Added."
    assert rental_program.edit_transaction_history("item", "returning") == "Added."
    assert rental_program.edit_transaction_history("jdanj", "klasfj") == "Error adding transaction."

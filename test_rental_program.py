""" Module Docstring """
import rental_program


def test_edit_inventory():
    """ Takes the user’s input and tells the inventory what items to take out/put in. """
    assert rental_program.edit_inventory("sdsaj", "dkj") == "Error!"
    assert rental_program.edit_inventory("actual item",
                                         "renting") == "Grabbing item..."
    assert rental_program.edit_inventory("actual item",
                                         "returning") == "Restocking item..."
    assert rental_program.edit_inventory("actual item",
                                         "replacing") == "Replacing item..."
    assert rental_program.edit_inventory('out of stock item',
                                         "renting") == """Sorry, that item is out of stock!"""


def test_transaction_history():
    """ Takes the user’s input and adds new info to the transaction history. """
    assert rental_program.transaction_history("item", "renting") == "Added."





def test_th_question():
    """ Asks the user if they want to view transaction history,
    view inventory, make a transaction, or quit. """
    assert rental_program.th_question() == "i" or "t" or "h"
    # should return t, i, h


def test_r_question():
    """ Asks the user whether they’re renting, returning, or replacing an item. """
    assert rental_program.r_question() == "fakjk"


def test_item_question():
    """ Asks the user which item they are renting/returning/replacing. """
    assert rental_program.item_question("renting") == "one of the three r's"
    # type of rental_program.item_question() equals string

def test_show_inventory():
    """
    Returns inventory to the user.
    item, num in stock, total stock, price for rental, replacement cost
    """
    assert rental_program.show_inventory() == [
        ['1995 Mario Figure Defect (2 noses)', 1, 1, 150, 400],
        ['rare Zelda NES', 5, 6, 210, 450],
        ['call of duty baseball bat', 40, 40, 22, 30],
        ['limited edition punch out boxing gloves', 3, 3, 300, 1000],
        ['elder scroll signed by bill nye', 0, 1, 400, 650],
        ['replica portal gun', 4, 5, 200, 360],
        ['replica monado', 1, 2, 230, 500]
    ]
    # How to test? Do I even need a test for this?

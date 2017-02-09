""" Module Docstring """
import rental_program

# can't test input
def test_edit_inventory():
    """ Takes the user’s input and tells the inventory what items to take out/put in. """
    assert rental_program.edit_inventory(["sdsaj", "dkj"]) == "Error!"
    assert rental_program.edit_inventory(["replica portal gun",
                                          "renting"]) == "Grabbing item..."
    assert rental_program.edit_inventory(["replica portal gun",
                                          "returning"]) == "Restocking item..."
    assert rental_program.edit_inventory(["replica portal gun",
                                          "replacing"]) == "Replacing item..."
    assert rental_program.edit_inventory(['elder scroll signed by bill nye',
                                          "renting"]) == "Sorry, that item is out of stock!"


def test_edit_transaction_history():
    """ Takes the user’s input and adds new info to the transaction history. """
    assert rental_program.edit_transaction_history(["replica portal gun", "renting"]) == "Added."
    assert rental_program.edit_transaction_history(["replica portal gun", "returning"]) == "Added."
    assert rental_program.edit_transaction_history(["elder scroll signed by bill nye",
                                                    "replacing"]) == "Added."
    assert rental_program.edit_transaction_history(["jdanj", "klasfj"]) == "Error!"

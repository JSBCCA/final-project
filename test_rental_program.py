""" Testing rental_program """
import rental_program

def test_isfloat():
    """ Checks if value is a float. """
    assert rental_program.isfloat(5) is False
    assert rental_program.isfloat(5.1) is True

def test_edit_inventory():
    """ Takes the user’s input and tells the inventory what items to take out/put in. """
    assert rental_program.edit_inventory(["sdsaj", "dkj"]) == "Error!"
    assert rental_program.edit_inventory(["replica portal gun",
                                          "renting"]) == "Grabbing item..."
    assert rental_program.edit_inventory(["replica portal gun",
                                          "returning"]) == "Restocking item..."
    assert rental_program.edit_inventory(["replica portal gun",
                                          "replacing"]) == "Replacing item..."
    assert rental_program.edit_inventory(['mario figure defect',
                                          "renting"]) == "Sorry, that item is out of stock!"
    assert rental_program.edit_inventory(['elder scroll signed by bill nye',
                                          "returning"]) == "Sorry, our stock of that item is full!"

def test_editfor_renting():
    """ If the user is renting, this should edit the inventory to account for that. """
    assert rental_program.editfor_renting("replica portal gun") == "Grabbing item..."
    assert rental_program.editfor_renting('mario figure defect') == "Sorry, that item is out of stock!"

def test_editfor_returning():
    """ If the user is returning, this should edit the inventory to account for that. """
    assert rental_program.editfor_returning("replica portal gun") == "Restocking item..."
    assert rental_program.editfor_returning('elder scroll signed by bill nye') == "Sorry, our stock of that item is full!"

def test_editfor_replacing():
    """ If the user is replacing, this should edit the inventory to account for that. """
    assert rental_program.editfor_replacing("replica portal gun") == "Replacing item..."
    assert rental_program.editfor_replacing('elder scroll signed by bill nye') == "Sorry, our stock of that item is full!"

from plates import is_valid


def test_letters_isvalid():
    assert is_valid("CS50") == True
    assert is_valid("C55AS") == False
    assert is_valid("CS") == True
    assert is_valid("C") == False

def test_6_chr():
    assert is_valid("AAA222") == True
    assert is_valid("AMMAR52YASIR") == False
    assert is_valid("A2") == False

def test_isvalid_punctuation():
    assert is_valid("AA20 5") == False
    assert is_valid("CS.50!") == False
    assert is_valid("CS50!") == False

def test_isvalid_1stnum_notzero():
    assert is_valid("AAV02") == False
    assert is_valid("AB000") == False

def test_isvalid_num_placement():
    assert is_valid("AB23CD") == False

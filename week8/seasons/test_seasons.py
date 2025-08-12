import seasons
import pytest
from unittest.mock import patch


# def test_calculate_minutes_lived():
#     assert seasons.calculate_minutes_lived("2007-03-04") == 9396000
def test_invalid_date():
    with patch('builtins.input', return_value="Invalid date"):
        with pytest.raises(SystemExit):
            seasons.get_birthdate()

def test_minutes_to_words():
    assert seasons.minutes_to_words(9396000) == "Nine million, three hundred ninety-six thousand"

from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("Ammar")   == "mmr"

def test_shorten_punctuation():
    assert shorten("Twitter!") == "Twttr!"

def test_shorten_numbers():
    assert shorten("NoobMaster69!") == "NbMstr69!"



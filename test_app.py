from app2 import guess_country, predict

def test_guess_country():
    assert guess_country("China") == "The country is not in the dataset!"
    assert guess_country("United States") == "You are correct!"
    assert guess_country("United Kingdom") == "You are wrong"

def test_predict_country():
    assert predict("China") == "The country is not in the dataset!"
    assert predict("United States") == "The average wage in 2020 is 69262.83706995238 in 2020"
    assert not predict("United Kingdom") == "The average wage in 2020 is 69262.83706995238 in 2020"


from mlproject.distance import haversine
def test_type_haversine():
    assert type(haversine(52.513169, 13.453457, 48.865070, 2.380009)) == float
def test_len_haversine():
    assert haversine(52.513169, 13.453457, 52.513169, 13.453457) >= 0

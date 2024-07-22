from seasons import convert_to_str, date_validate

def test_seasons():
    assert convert_to_str("525600") == "Five hundred twenty-five thousand, six hundred minutes"
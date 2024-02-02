import os
from project import tuser_input, is_leap_year, year_days, birthday

def test_tuser_input():
    assert tuser_input("03/07/2009") == True
    assert tuser_input("sghoihg") == False
    assert tuser_input("36/17/2008") == False
    assert tuser_input("hello") == False

def test_is_leap_year():
    assert is_leap_year(2024) == 29
    assert is_leap_year(2023) == 28
    assert is_leap_year(2020) == 29
    assert is_leap_year(712401) == 28

def test_year_days():
    assert year_days(["03" , "07" , "2009"]) == 181
    assert year_days(["03" , "11" , "2009"]) == 58
    assert year_days(["31" , "01" , "2009"]) == 334

def test_birthday():
    assert birthday(["03" , "07" , "2009"]) == False
    assert birthday(["03" , "07" , "2009"]) == False


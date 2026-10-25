# Jason Hoppal
# CIS256 Fall 2026
# Programming Assignment 4 - Test File

from guess_the_word import find_letter_indexes

def test_find_letter_indexes():
    assert find_letter_indexes("a","football") == [5]
    assert find_letter_indexes("o","football") == [1,2]
    assert find_letter_indexes("t","spaceship") == []

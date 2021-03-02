#! /usr/bin/env python3
# # coding=utf-8
"""
Testing for virus.py file.

Charlie Say
CS 162
10:00 AM

"""


from io import StringIO
import virus
import pytest


def test_target_letter(monkeypatch):
    """Test target_letter for string input."""
    letter = StringIO("he\n")
    monkeypatch.setattr('sys.stdin', letter)
    assert  virus.target_letter() == "he"

def test_target_letter_integer(monkeypatch):
    """Test target_letter for integer input."""
    integer_inputs = StringIO("123\n")
    monkeypatch.setattr('sys.stdin', integer_inputs)
    assert virus.target_letter() == "123"

def test_open_silly_word(monkeypatch):
    """Test silly word is returning same word."""
    silly_me = virus.open_silly()
    assert silly_me == str(silly_me)

def test_open_silly_type(monkeypatch):
    """Test silly word is a string type."""
    silly_me = virus.open_silly()
    assert type(silly_me) == str

def test_check_status_integer():
    x_me = virus.XehroVirus("1")
    c_me = x_me.check_status("1")
    assert c_me == None

def test_check_status_string():
    x_me = virus.XehroVirus("asd")
    c_me = x_me.check_status("asd")
    assert c_me == None

def test_check_status_other():
    x_me = virus.XehroVirus(">")
    c_me = x_me.check_status(">")
    assert c_me == None

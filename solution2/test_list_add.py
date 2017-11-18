#!/usr/bin/env python
# -*- coding: utf-8 -*-

def list_add(L):
    return sum(L)

# Test commutativity using unit tests
def test_list_add_whole_numbers_unit():
    L = [1, 2, 3, 4, 5] # integers
    assert list_add(L) == list_add(reversed(L))

def test_list_add_real_numbers_unit():
    L = [1.0, 2.0, 3.0, 4.0, 5.0] # floats
    assert list_add(L) == list_add(reversed(L))

# Test commutativity using a property-based tests
from hypothesis import given
import hypothesis.strategies as st

# EXERCISE 1: Test with a list of whole numbers
@given(st.lists(st.integers()))
def test_list_add_whole_numbers_pbt(L):
    assert list_add(L) == list_add(reversed(L))

# EXERCISE 2: Test with a list of real numbers (floats or decimals)
@given(st.lists(st.decimals(
    allow_nan = False,
    allow_infinity = False,
    places=2,
    min_value=-999999,
    max_value=999999,
    )))
def test_list_add_real_numbers_pbt(L):
    assert list_add(L) == list_add(reversed(L))

# Documentation on the different strategies:
# http://hypothesis.readthedocs.io/en/latest/data.html

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cart import ShoppingCart
from test_book import example_book
from coupon import COUPONS

import pytest
from decimal import *

# Test adding to empty cart
def test_add(example_book):
    cart = ShoppingCart()
    cart.add(example_book)
    assert cart.total == 10.00

# Test remove from empty cart
def test_remove(example_book):
    cart = ShoppingCart()
    cart.remove(example_book)
    assert cart.total == 0.00

# Test adding to empty cart and then removing
def test_add_remove(example_book):
    cart = ShoppingCart()
    cart.add(example_book)
    cart.remove(example_book)
    assert cart.total == 0.00

# Test discounting a book
def test_add_discount(example_book):
    cart = ShoppingCart()
    cart.add(example_book)
    cart.add_discount(COUPONS["10OFF"])
    assert cart.total == 9.00


# Property-based tests

from hypothesis import given
import hypothesis.strategies as st

# EXERCISE1: Recreate the three add, remove, and add+remove unit tests but as
# property-based tests
# Replace this line with your test for add

# Replace this line with your test for remove

# Replace this line with your test for add+remove


from hypothesis.stateful import rule, RuleBasedStateMachine, Bundle
# EXERCISE2: Test discount transactions using a RuleBasedStateMachine
# http://hypothesis.readthedocs.io/en/latest/stateful.html
# Replace this line with your RuleBasedStateMachine

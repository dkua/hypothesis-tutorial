#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cart import ShoppingCart
from test_book import example_book, books
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
@given(st.lists(books))
def test_add(list_of_books):
    cart = ShoppingCart()
    for book in list_of_books:
        cart.add(book)
    total = sum(book.price for book in list_of_books)
    assert cart.total == total

@given(st.lists(books))
def test_remove(list_of_books):
    cart = ShoppingCart()
    for book in list_of_books:
        cart.remove(book)
    assert cart.total == 0.00

@given(st.lists(books))
def test_add_remove(list_of_books):
    cart = ShoppingCart()
    for book in list_of_books:
        cart.add(book)
        cart.remove(book)
    assert cart.total == 0.00


from hypothesis.stateful import rule, RuleBasedStateMachine, Bundle
# EXERCISE2: Test discount transactions using a RuleBasedStateMachine
# http://hypothesis.readthedocs.io/en/latest/stateful.html
class CartMachine(RuleBasedStateMachine):
    Carts = Bundle("carts")
    BOOKS = st.lists(books, min_size=10).example()

    @rule(target=Carts)
    def new_cart(self):
        return ShoppingCart()

    @rule(cart=Carts, item=st.sampled_from(BOOKS))
    def add_item(self, cart, item):
        cart.add(item)
        assert cart.total >= 0.00

    @rule(cart=Carts, item=st.sampled_from(BOOKS))
    def remove_item(self, cart, item):
        cart.remove(item)
        assert cart.total >= 0.00

    @rule(cart=Carts, coupon=st.sampled_from(COUPONS.values()))
    def add_coupon(self, cart, coupon):
        cart.add_discount(coupon)
        assert cart.total >= 0.00

    @rule(cart=Carts, coupon=st.sampled_from(COUPONS.values()))
    def remove_discount(self, cart, coupon):
        cart.remove_discount(coupon)
        assert cart.total >= 0.00

TestCarts = CartMachine.TestCase

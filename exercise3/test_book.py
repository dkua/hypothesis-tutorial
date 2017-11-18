#!/usr/bin/env python
# -*- coding: utf-8 -*-

from book import Book

import pytest

@pytest.fixture
def example_book():
    book = Book(
            title="Python", 
            author="Kua",
            price=10.00,
            )
    return book

# Test the book has correct values and can print
def test_book(example_book):
    assert example_book.title == "Python"
    assert example_book.author == "Kua"
    assert example_book.price == 10.00
    print(example_book)


# Property-based tests

from hypothesis import given
import hypothesis.strategies as st

# EXERCISE1: Using the builds strategy, create a strategy for Book types
# http://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.builds
# Replace this line with your strategy

# EXERCISE2: Using your Book strategy, create a test to make sure unicode in
# titles and authors are supported (use print())
# Replace this line with your test

# EXERCISE3: Using your Book strategy, create a test that for the property that
# "price is never $0.00 or below it" ie. price is non-negative
# Replace this line with your test

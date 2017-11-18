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
books = st.builds(
        Book,
        title=st.text(),
        author=st.text(),
        price=st.decimals(
            allow_nan=False,
            allow_infinity=False,
            places=2,
            min_value=0.00,
            max_value=1000000.00,
            ),
        )

# EXERCISE2: Using your Book strategy, create a test to make sure unicode in
# titles and authors are supported (use print())
@given(books)
def test_unicode(book):
    print(book)

# EXERCISE3: Using your Book strategy, create a test that for the property that
# "price is never $0.00 or below it" ie. price is non-negative
@given(books)
def test_never_negative(book):
    assert book.price >= 0.00

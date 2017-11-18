#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add(x, y):
    return x + y

# Test commutativity using an unit test
def test_commutativity_unit():
    assert add(1, 2) == add(2, 1)

# Test commutativity using a property-based test
from hypothesis import given, settings
import hypothesis.strategies as st

@given(st.integers(), st.integers())
@settings(max_examples=1000)
def test_commutativity_pbt(x, y):
    assert add(x, y) == add(y, x)

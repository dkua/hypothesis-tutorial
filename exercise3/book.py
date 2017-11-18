#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
TWOPLACES = Decimal(10) ** -2 # 2 places --> '0.01'

class Book(object):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = Decimal(price).quantize(TWOPLACES)

    def __unicode__(self):
        return u"%s by %s ($%s)" % (self.title, self.author, self.price)

    def __repr__(self):
        return self.__unicode__()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
TWOPLACES = Decimal(10) ** -2 # 2 places --> '0.01'

class ShoppingCart(object):
    def __init__(self):
        self.cart = {}
        self.discounts = {}

    def __unicode__(self):
        return u"Cart(Total: $%s)" % self.total

    def __repr__(self):
        return self.__unicode__().encode("utf-8")

    @property
    def total(self):
        subtotal = Decimal(0.00)
        for item, num in self.cart.items():
            subtotal += item.price * num
        for discount in self.discounts.values():
            subtotal *= discount
        return Decimal(subtotal).quantize(TWOPLACES)

    def add(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1

    def remove(self, item):
        if item in self.cart:
            self.cart[item] -= 1
            if self.cart[item] == 0:
                del self.cart[item]

    def add_discount(self, coupon):
        if self.total >= 0 and coupon not in self.discounts:
            self.discounts[coupon] = coupon.percent

    def remove_discount(self, coupon):
        if coupon in self.discounts:
            del self.discounts[coupon]

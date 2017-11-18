#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
TWOPLACES = Decimal(10) ** -2 # 2 places --> '0.01'

class ShoppingCart(object):
    def __init__(self):
        self.cart = {}
        self.discounts = {}
        self.total = Decimal(0.00).quantize(TWOPLACES)

    def __unicode__(self):
        return u"Cart(Total: $%s)" % self.total

    def __repr__(self):
        return self.__unicode__().encode("utf-8")

    def add(self, item):
        if item in self.cart:
            self.cart[item] += 1
        else:
            self.cart[item] = 1
        self.total += item.price

    def remove(self, item):
        if item in self.cart:
            self.cart[item] -= 1
            if self.cart[item] == 0:
                del self.cart[item]
            self.total -= item.price

    def add_discount(self, coupon):
        if self.total > 0 and coupon not in self.discounts:
            self.discounts[coupon] = coupon.percent
            self.total *= Decimal(self.discounts[coupon]).quantize(TWOPLACES)

    def remove_discount(self, coupon):
        if coupon in self.discounts:
            self.total /= Decimal(self.discounts[coupon]).quantize(TWOPLACES)
            del self.discounts[coupon]

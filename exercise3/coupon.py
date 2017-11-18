#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import *
from collections import namedtuple

Coupon = namedtuple("Coupon", ["percent"])
COUPONS = {
        "10OFF": Coupon(Decimal(0.9)),
        "20OFF": Coupon(Decimal(0.8)),
        "30OFF": Coupon(Decimal(0.7)),
        "40OFF": Coupon(Decimal(0.6)),
        "50OFF": Coupon(Decimal(0.5)),
        "60OFF": Coupon(Decimal(0.4)),
        "70OFF": Coupon(Decimal(0.3)),
        "80OFF": Coupon(Decimal(0.2)),
        "90OFF": Coupon(Decimal(0.1)),
}

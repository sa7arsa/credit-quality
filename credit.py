import os
import math


def calculate_risk(revenue, debt, duration):
    ratio = debt / revenue

    if ratio > 0.6:
        return "HIGH"
    elif ratio > 0.3:
        return "MEDIUM"
    else:
        return "LOW"
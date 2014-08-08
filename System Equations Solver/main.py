__author__ = 'ddsnowboard'
import math

def solve(a, b, c, tol, d, e, f, lbound, rbound):
    done = False
    # Make sure there is sign change
    if lbound > rbound or ((a*lbound**2)+(b*lbound)+c) :
        return False
    while not done:
        mid = (rbound-lbound)/2
        if
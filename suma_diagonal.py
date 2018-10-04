#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    x = [ arr[i][i] for i in range(len(arr)) ]
    y = [ arr[i][-(i+1)] for i in range(len(arr)) ]
    print( x )
    print( y )
    return abs( sum(y)-sum(x) )
print( diagonalDifference([ [6,8],[-6,9] ]) )
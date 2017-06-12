# Name:
# Date:

# proj02_02: Fibonaci Sequence


# Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci
# sequence is a sequence of numbers where the next number in the sequence is the sum of the
# previous two numbers in the sequence. The sequence looks like this:
# 1, 1, 2, 3, 5, 8, 13...'

import time

Fn = 1
Pn = 0
count = 1
while count < 100:
    count += 1
    print Fn
    Nn = Pn + Fn
    Pn = Fn
    Fn = Nn

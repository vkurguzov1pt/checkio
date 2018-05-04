'''
You are given the lengths for each side on a triangle.
You need to find all three angles for this triangle.
If the given side lengths cannot form a triangle
(or form a degenerated triangle),
then you must return all angles as 0 (zero).
The angles should be represented as a list of integers in ascending order.
Each angle is measured in degrees
and rounded to the nearest integer number (Standard mathematical rounding).

Example:

checkio(4, 4, 4) == [60, 60, 60]
checkio(3, 4, 5) == [37, 53, 90]
checkio(2, 2, 5) == [0, 0, 0]
'''
import math


def checkio(a, b, c):
    # Check for triangle inequality a+b>c, b+c>a, c+a>b
    if max(a, b, c) >= a + b + c - max(a, b, c):
        return [0, 0, 0]
        # Check if max equals min, if so all sides are equal
    elif max(a, b, c) == min(a, b, c):
        return [60, 60, 60]
        # accoring to the law of cosines
        # the third side of a triangle if one knows two sides and the angle between them:
        # c = sqrt(pow(a,2)+pow(b,2)-2*a*b*cos(x)), so
        # x is the angle between a,b sides
        # x1 is the angle between b,c sides
    else:
        arc_cosinesX = math.acos(
            (pow(a, 2) + pow(b, 2) - pow(c, 2)) / (2 * a * b))
        arc_cosinesX1 = math.acos(
            (pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c))
        x = round(math.degrees(arc_cosinesX))
        x1 = round(math.degrees(arc_cosinesX1))
        # The sum of all the angles is 180 degrees
        x2 = 180 - (x + x1)
        return sorted([x, x1, x2])



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

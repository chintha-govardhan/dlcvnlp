"""
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3
"""

from math import pi

def find_volume(diameter):
    radius = diameter/2.0
    return (4/3 * pi * radius**3)

print(find_volume(12))
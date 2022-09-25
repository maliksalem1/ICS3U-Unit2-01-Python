#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Sep 2022
# This program calculates the area and perimeter of a circle
#    with radius 15mm

import math


def main():
    # this function calculates the area and perimeter

    print("If a circle has a radius of 15 mm: ")
    
    print("Area is {} mm².".format(math.pi * 15 ** 2))
    print("Perimeter is {} mm.".format(2 * math.pi * 15))
    print("\nDone.\n")


if __name__ == "__main__":
    main()

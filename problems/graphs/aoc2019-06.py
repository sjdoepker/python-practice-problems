"""
Starter code for Advent of Code 2019 Day #6

You must implement functions part1 and part2
"""

import sys
import os
import re

class SpaceObject:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


def part1(orbits):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """
    sum = 0
    for planet in orbits:
        sum += count_orbits(planet)
    return sum

"""    result = 0
    with open(orbits) as f:
        for i in f:
            name, orbiting = i.split(")")
            result += 1 + to_start(name, orbits)
        return result

    def to_start(dest, orbits):
        if key in orbits:
            return to_start(orbits[dest], orbits) +1
        else:
            return 0
"""

def count_orbits(planet):
    if planet.parent is None:
        return 0
    else:
        return 1 + count_orbits(planet.parent)

    

def part2(orbits):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - orbits: a dictionary mapping an object name (e.g., "B")
              to the name of the object it orbits (e.g., "COM")

    Returns an integer
    """
    ### Replace with your code
    return None



############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        lines = f.read().strip().split("\n")
        objs = [line.split(")") for line in lines]
        orbits = {}
        for p1, p2 in objs:
            orbits[p2] = p1

    print(f"Part 1:", part1(orbits))
    
    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", part2(orbits))

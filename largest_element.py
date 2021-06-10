#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: June 2021
# This program uses a list as a parameter

import random


def find_largest_element(my_numbers):

    Largest_element = my_numbers[0]

    for counter in range(0, len(my_numbers)):
        if Largest_element < my_numbers[counter]:
            Largest_element = my_numbers[counter]

    return Largest_element


def main():
    # this function uses a list

    my_numbers = []

    # input
    for loop_counter in range(1, 11):
        a_number = random.randint(1, 100)
        my_numbers.append(a_number)
        print("The element {0} is: {1} ".format(loop_counter, a_number))
    print("")

    # call the function
    Largest_element = find_largest_element(my_numbers)

    # output
    print("The largest element is: {0} ".format(Largest_element))


if __name__ == "__main__":
    main()

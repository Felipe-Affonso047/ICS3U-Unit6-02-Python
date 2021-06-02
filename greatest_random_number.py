#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program generate random numbers and shows the greatest out of them

import random


def greatest_number(list_of_numbers):
    # this function outputs the greatest number out of a list
    greatest = 0

    for counter in range(len(list_of_numbers)):
        if list_of_numbers[counter] > greatest:
            greatest = list_of_numbers[counter]

    return greatest


def main():
    # This function is the main function and generate random numbers
    number_of_random_numbers = 10
    numbers = []

    print("{} random numbers:".format(number_of_random_numbers))

    for random_numbers in range(0, number_of_random_numbers):
        temp = random.randint(1, 100)
        numbers.append(temp)
        print("{}".format(numbers[random_numbers]))

    greatest = greatest_number(numbers)

    print("\nThe greatest number is: {}".format(greatest))

    print("\nDone.")


if __name__ == "__main__":
    main()

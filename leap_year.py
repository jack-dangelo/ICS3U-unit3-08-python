#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: October 2019
# This program determines if a year is a leap year


def main():
    while True:
        try:
            # calculates if year is a leap year
            year = int(input("Enter a year: "))
            print()
        
            if year % 4 == 0 and year % 100 != 0:
                print("This is a leap year")
            if year % 4 != 0:
                print("This is not a leap year")
            if year % 4 == 0 and year % 100 == 0:
                if year % 400 != 0:
                    print("This is not a leap year")
                if year % 400 == 0 and year % 100 == 0:
                    print("This is a leap year")

        except ValueError:
            print()
            print("Invalid Year")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()

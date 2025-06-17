#!/usr/bin/env python3

from fraction import Fraction, InputError




def main():
    try:
        while True:
            numer = int(input("Please enter a numerator "))
            denom = int(input("Please enter a denominator "))
            fraction = Fraction(numer, denom)
            print(fraction)
            lanjut = input("lanjut y/n ").lower()
            if lanjut == "n":
                raise ValueError
                break
    except ZeroDivisionError:
        print("Zero Division Error")
    except ValueError:
        print("your input is false")




if __name__ == "__main__":
    main()

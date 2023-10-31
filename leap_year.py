#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 31, 2023
# This is program will tell you if it is a leap year.


def main():
    user_year = str(input("Enter the Year:\n"))
    try:
        user_year = int(user_year)
    except ValueError:
        print(f"{user_year} is not a Value.")
    else:
        if user_year % 4 == 0:
            if (user_year % 100 == 0) and (user_year % 400 == 0):
                print(f"{user_year} is a leap year.")
            elif user_year % 100 == 0:
                print(f"{user_year} is not a leap year.")
        else:
            print(f"{user_year} is not a leap year.")
    finally:
        print("Code ended")


if __name__ == "__main__":
    main()

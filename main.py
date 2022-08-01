# This is a program to determine whether a year is a leap year(>1500)


while True:
    leapYear = int(input("enter the year: "))

    if leapYear >= 1500:
        if leapYear % 4 == 0:
            if leapYear % 100 == 0:
                if leapYear % 400 == 0:
                    print(str(leapYear) + " is a leap year!")            
                else:
                    print(str(leapYear) + " is not a leap year!")
            else:
                print(str(leapYear) + " is a leap year!")
        else:
            print(str(leapYear) + " is not a leap year!")
    else:
        print("Invalid year!")
        continue

#This is a program to determine whether a given year is a leap year


while True:
    leapYear = int(input("enter the year: "))

    if leapYear >= 1000:
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

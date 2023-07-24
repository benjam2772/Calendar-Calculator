# INPUT DATE, SLICE INTO DAY, MONTH YEAR
date = input("Please enter a date between 1600 and 2099 (mm/dd/yyyy): ")
try:
    day = date[3:5]
    month = date[0:2]
    year = date[6:10]

    # SET TO INTEGERS
    day = int(day)
    month = int(month)
    year = int(year)

    # DEFINE MONTH AND YEAR CODES AS INTEGERS
    monthCode = int
    yearCode = int

    # MONTH CODE CONVERSION
    if 1 <= month <= 12:
        if month == 1:
            monthCode = 6
        elif month == 2:
            monthCode = 2
        elif month == 3:
            monthCode = 2
        elif month == 4:
            monthCode = 5
        elif month == 5:
            monthCode = 0
        elif month == 6:
            monthCode = 3
        elif month == 7:
            monthCode = 5
        elif month == 8:
            monthCode = 1
        elif month == 9:
            monthCode = 4
        elif month == 10:
            monthCode = 6
        elif month == 11:
            monthCode = 2
        elif month == 12:
            monthCode = 4

    # YEAR CODE CALCULATOR
    if 1600 <= year <= 2099:
        # GET DECADE
        year = str(year)
        decade = year[2:4]
        # RESET TO INTEGERS
        year = int(year)
        decade = int(decade)
        # GET YEAR CONVERSION CODE
        yearConv = int
        if 1600 <= year <= 1699:
            yearConv = 0
        elif 1700 <= year <= 1799:
            yearConv = 5
        elif 1800 <= year <= 1899:
            yearConv = 3
        elif 1900 <= year <= 1999:
            yearConv = 1
        elif 2000 <= year <= 2999:
            yearConv = 0
        # LEAP YEAR
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if month == 1:
                monthCode = 5
            elif month == 2:
                monthCode = 1
        # CALCUlATE YEAR CODE
        yearCode = (decade + (decade // 4) + yearConv) % 7

    # CALCULATE DAY CODE
    if 1 <= day <= 31:
        dayCode = (day + monthCode + yearCode) % 7

    # CONVERT TO DAY OF WEEK AND PRINT
    if dayCode == 0:
        print("Sunday")
    elif dayCode == 1:
        print("Monday")
    elif dayCode == 2:
        print("Tuesday")
    elif dayCode == 3:
        print("Wednesday")
    elif dayCode == 4:
        print("Thursday")
    elif dayCode == 5:
        print("Friday")
    elif dayCode == 6:
        print("Saturday")

except:
    print("Please enter a valid date.")




        





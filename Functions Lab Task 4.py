def validate_date(day, month, year): 
        if month > 12 or month < 1:
            return "Invalid"
        else:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day <= 31 and (year >= 1900 and year <= 2099):
                    return "Valid"
                else:
                    return "Invalid"
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day <= 30 and (year >= 1900 and year <= 2099):
                    return "Valid"
                else:
                    return "Invalid"
            elif month == 2:
                if day <= 29 and (year >= 1900 and year <= 2099):
                    if (year % 4) == 0 and day == 29:
                        return "Valid"
                    elif (year % 4) != 0 and day == 29:
                        return "Invalid"
                    else:
                        return "Valid"
                else:
                    return "Invalid"
    
    day = int(input("Enter Day of the month: "))
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    print(validate_date(day, month, year))

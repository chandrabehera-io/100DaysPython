# days in month
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

def days_in_month(year,month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month == 2:
        month_days[1] = 29
    return month_days[month-1]

year = int(input("Enter year: "))
month = int(input("Enter month: "))
print("Days in month: ",days_in_month(year,month))
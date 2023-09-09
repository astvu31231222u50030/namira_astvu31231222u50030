def check_leap(year): 
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 

year = 2004 

print(f"{year} is leap year")
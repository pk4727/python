def is_leap(year):
    leap = False
    leap_n = True
    if(year>=1900 and year<=1000000):
        if(year%4==0):
            if(year%100==0):
                if ((year%400)==0):                 
                  return leap_n
                else:
                    return leap
            else:
                return leap_n
        else:
            return leap
    else:
        print("invilide year range")    
year = 1935
print(is_leap(year))
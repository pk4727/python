import calendar

# print(calendar.calendar(2022))
# print(calendar.weekday(2022,11,6))
# print(calendar.isleap(2023))
# print(calendar.leapdays(2000,2010))
# help(calendar)


# from calendar import datetime
# t1= input()
# t2= input()
# a=datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
# b=datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")



n= input("Enter DD MM YEAR:-").split()
m=int(n[1])
d=int(n[0])
y=int(n[2])
print(calendar.TextCalendar(firstweekday=6).formatyear(y))
c = calendar.weekday(y,m,d)
if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c==3:
    print("THURSDAY")
elif c==4:
    print("FRIDAY")
elif c== 5:
    print("SATURDAY")
elif c==6:
    print("SUNDAY")
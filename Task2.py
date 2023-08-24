str1 = "January"
str2 = "February"
str3 = "March"
str4 = "April"
str5 = "May"
str6 = "June"
str7 = "July"
str8 = "August"
str9 = "September"
str10 = "October"
str11 = "November"
str12 = "December"
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
mon = str(input("Input the name of Month: "))
if mon == str2:
    print("Number od days: 28 days")
elif mon == str4 or str6 or str9 or str11:
    print("Number od days: 30 days")   
else:
    print("Number od days: 31 days")
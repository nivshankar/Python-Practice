import datetime

#date method used to display date after using ".date"
date = datetime.date(2026,5,17)
print(date)

#date method used to display date after using ".date"
#Not specifying the date in bracket means it will diplay current date
today=datetime.date.today()
print(today)

#Using time method to display time after using '.time' 
time=datetime.time(12,30,0)
print(time)

#For diplaying full date and time use the ".datetime" after datetime object
#also we have to use ".now" attribute
current_datetime=datetime.datetime.now()
print(current_datetime)

#string format time method can be used to display time
#first the variable should be declared for date and time
now=current_datetime.strftime("time : %H:%M:%S date: %d-%m-%Y")
print(now)
year=current_datetime.strftime("%Y")
year=int(year)
birth_year=int(input("enter birth year: "))
age=year-birth_year
print(age)


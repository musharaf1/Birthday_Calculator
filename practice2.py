           #program to calculate weekday ahead: translating days into numbers in our head
print("days of the week are represented in range 1 thru 7, eg:\n 1=sunday \n 2=mon \n 3=tue \n 4=wed \n 5=thur \n 6=fri\n 7=sat")
print("weeks and months are represented in range 1 thru 365, eg: Feb 1st 32,since it is the 32ND day of the year")

print("now, to get the wweekday ahead\n\n")
current_day=int(input("indicate the curent_day\n "))
days_ahead=int(input("indicate the days_ahead\n  "))
def get_weekday(current_day,days_ahead):
        answer=(current_day+days_ahead-1)%7+1
        print(answer)
get_weekday(current_day,days_ahead)
get_weekday(3,1)
get_weekday(6,1)
get_weekday(7,1)
get_weekday(1,0)
get_weekday(4,7)
get_weekday(7,72)


   #PROGRAM TO CALCULATE DIFFERENCES IN DAYS:for some reason we will ignore months and use the numbers1-365 to indicate the days of the year , eg we'll rep feb ist as 32,since it is the 32nd day of a year
print("to determine the difference in the days\n\n")
day1=int(input("indicate the curent_day\n "))
day2=int(input("indicate the days_ahead\n  "))
def difference_in_days(day1,day2):
        answer=(day1-day2)
        print(answer)
difference_in_days(day1,day2)
difference_in_days(200,224)
difference_in_days(50,50)
difference_in_days(100,99)



        #PROGRAM TO CALCULATE birthday weekday: if today is a thur(5th day of the week)and today is the 3rd day of the year,what day will it be on the 4th day of the year
print("to determin the birthday weekday, kindly supply the data required below\n\n")
current_weekday=int(input("please supply the current day of the week you are in\n "))
current_month=int(input("please supply the current month of the year you are in\n "))
birthday_month=int(input("please supply the your birthday month\n "))

def get_birthday_weekday(current_weekday,current_month, birthday_month):
                         ans1=current_weekday-birthday_month
                         ans2=(current_month+ans1-1)%2+1
                         print(ans2)
get_birthday_weekday(current_weekday,current_month, birthday_month)
                        

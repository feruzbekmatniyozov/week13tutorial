import datetime as dt

def exam_days_calc():
    year = int(input("Enter exam year:"))
    month = int(input("Enter exam month:"))
    day = int(input("Enter exam year:"))

    exam_date = dt.date(year=year, month=month, day=day)
    current_date = dt.date.today()

    diff = exam_date - current_date
    days = diff.days
    if days == 0:
        print("Your exam is today! Good luck buddy!")
    elif days < 0:
        print(f"The exam was {-1*days} days ago.")
    else:
        print(f"You have {days} days left to study!")

exam_days_calc()
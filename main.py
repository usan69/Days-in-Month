def is_leap(year):
  if year% 4 ==0:
    if year% 100 ==0:
      if year% 400==0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


def day_in_month(year,month):
  if month>12 or month<1 :
    return"invalid input"
  months_days=[31,28,31,30,31,30,31,31,30,31,30,31]
  if is_leap(year) and month==2 :
    return 29
  return months_days[month-1]


year=int(input("Year's number that you want to know :\n"))
month=int(input("Month's name that you want to know :\n"))
days=day_in_month (year,month)

print(f"{days} days in your selected month")
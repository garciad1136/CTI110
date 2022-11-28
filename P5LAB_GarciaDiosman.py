def days_in_feb(user_year):
    if user_year % 400 == 0:
        return 29
    elif user_year % 100 == 0:
        return 28
    elif user_year % 4 == 0:
        return 29
    else:
        return 28
    return 28

if __name__ == '__main__':
    user_year = int(input())
    days = days_in_feb(user_year)
    print(f"{user_year} has {days} days in February.")
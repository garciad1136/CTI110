input_year = int(input())

def is_leap_year(input_year):
    if(input_year % 400 == 0):
        return True
    # Not a leap year
    elif input_year % 100 == 0:
        return False
    elif input_year % 4 == 0:
        return True
    # Otherwise False
    else:
        return False
# Main OUTPUT
if __name__ == '__main__':
    if is_leap_year(input_year):
        print(input_year, "- leap year")
    else:
        print(input_year, "- not a leap year")
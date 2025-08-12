import inflect
import re
import sys
from datetime import date, datetime


def main():
    birthdate = get_birthdate()
    minutes_lived = calculate_minutes_lived(birthdate)
    print(f"{minutes_to_words(minutes_lived)} minutes")

def get_birthdate():
    while True:
        birthdate = input("Date of Birth: ")
        if re.match(r"^\d{4}-\d{2}-\d{2}$", birthdate):
            try:
                return datetime.strptime(birthdate, "%Y-%m-%d")
            except ValueError:
                print("Invalid date")
                sys.exit(1)
        else:
            print("Invalid date")
            sys.exit(1)

def calculate_minutes_lived(birthdate):
    birthdate = datetime(birthdate.year, birthdate.month, birthdate.day)
    today = date.today()
    today = datetime(today.year, today.month, today.day)
    difference = today - birthdate
    return difference.total_seconds() / 60

def minutes_to_words(minutes):
    p = inflect.engine()
    return p.number_to_words(int(minutes), andword="").capitalize()

if __name__ == "__main__":
    main()

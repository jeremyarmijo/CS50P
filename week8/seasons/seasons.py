from datetime import date, datetime
import inflect
import sys


def main():
    birthdate = input("Date of Birth: ")
    true_date = date_validate(birthdate)
    days_difference = diff_date(true_date)
    output = convert_to_str(days_difference)
    print(output)

def date_validate(birthdate):
    try:
        input = date.fromisoformat(birthdate)
        return input
    except ValueError:
        sys.exit("Invalid date")

def diff_date(days):
    today = date.today()
    difference = today - days
    difference.days * 24 * 60
    return difference.days * 24 * 60

def convert_to_str(text):
    p = inflect.engine()
    text = p.number_to_words(text, andword="")
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()
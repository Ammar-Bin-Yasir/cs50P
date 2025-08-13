# corrects the date formats

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Prompt the user for a date in month-day-year order
while True:
    try:
        date = input("Date: ").strip()
        # If the format is Month DD, YYYY
        if date[0].isalpha() and "," in date:
            month, day, year = date.split(" ")
            # Covert this format into digits
            day_num = int(day.replace(",",""))
            year_num = int(year)
            month_num = 0
            if month in months:
                month_num = months.index(month) + 1

            # Check weather the user has inputed correct dates
            if 0 < month_num <= 12 and 0 < day_num <= 31 and len(year) == 4:
                break
            else:
                raise ValueError

        # If the format is MM/DD/YYYY
        elif date[0].isdigit():
            m, d, y = date.split("/")
            m_num = int(m)
            d_num = int(d)
            y_num = int(y)

            # Check weather the user has inputed correct dates
            if 0 < m_num <= 12 and 0 < d_num <= 31 and len(y) == 4:
                break
            else:
                raise ValueError

        else:
            raise ValueError

    except ValueError:
        pass

# Output that same date in YYYY-MM-DD format
if date[0].isalpha():
    print(f"{year_num}-{month_num:02}-{day_num:02}")
else:
    print(f"{y_num}-{m_num:02}-{d_num:02}")

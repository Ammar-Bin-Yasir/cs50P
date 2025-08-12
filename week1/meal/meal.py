def main():

    time = input("What time is it? ")
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert_12to24(time):
    if time.lower().endswith("a.m"):
        newtime = time.replace("a.m","")
        hours, minutes = newtime.split(":")
        if int(hours) == 12:
            hours = 0
    elif time.lower().endswith("p.m"):
        newtime = time.replace("p.m","")
        hours, minutes = newtime.split(":")
        if int(hours) != 12:
            hours = int(hours) + 12
    ftime = str(hours)
    ftime = ftime + ":" + minutes
    return  ftime

# converts the time from 24 hour to a floating point value
def convert(time):
    if time.lower().endswith("a.m") or time.lower().endswith("p.m"):
        time = convert_12to24(time)
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__":
    main()

#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
def parse_month(month):
    if month == "January":
        return "01"
    if month == "February":
        return "02"
    if month == "March":
        return "03"
    if month == "April":
        return "04"
    if month == "May":
        return "05"
    if month == "June":
        return "06"
    if month == "July":
        return "07"
    if month == "August":
        return "08"
    if month == "September":
        return "09"
    if month == "October":
        return "10"
    if month == "November":
        return "11"
    if month == "December":
        return "12"



def FixDayCode(day):
    fatzero = "0"
    if day < 10:
        fatzero += str(day)
    else:
        fatzero = str(day)
    return fatzero
    
def parse_date(RawInput):
    parts = RawInput.split()
    month = parse_month(parts[0])
    day = FixDayCode(int(parts[1]))
    year = parts[2]
    return f"{month}/{day}/{year}"

if __name__ == '__main__':
    RawInput = input()
    while RawInput != "-1":
        parsed = parse_date(RawInput)
        print(parsed)
        RawInput = input()

    
 
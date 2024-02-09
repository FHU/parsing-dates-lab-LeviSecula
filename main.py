#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#please work
def parse_month(month):
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11",
        "December": "12"
    }
    return months.get(month, "That's Not Right")

def parse_day(day):
    day = day.replace(",", "")
    return f"{int(day):02d}"

def parse_date(user_string):
    components = user_string.split()
    
    if len(components) == 3:
        month = parse_month(components[0])
        day = parse_day(components[1])
        year = components[2]
        return f"{month}/{day}/{year}"
    else:
        return "Oopsie Daisy, that doesn't look right"

if __name__ == '__main__':
    raw_input = input()

    while raw_input != "-1":
        parsed = parse_date(raw_input)
        print(parsed)
        raw_input = input()

    
 
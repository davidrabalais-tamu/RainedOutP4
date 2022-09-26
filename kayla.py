from datetime import datetime
from datetime import timedelta
import re

FILE_NAME = './log.txt'

def days():
    fh = open(FILE_NAME)
    days = {}
    for line in open(FILE_NAME):
            #added check for year b/c there are some malformed requests
        if ("GET" in line) and ("1994" in line or "1995" in line):
            #print(line)
            # Extract the date from the request line
            date = line[(line.index("[")+1):(line.index(":"))]
            #print(date)

            # Format the date in a way we can use it for getting the day as a number
            conv = datetime.strptime(date, '%d/%b/%Y')

            # Create dictionary entry from extracted date data.
            day = "Number of requests on " + conv.strftime('%d, %b %Y') 
        
            # Will use day number to add up requests for a day.
            if day in days:
                days[day] += 1
            else:
                days[day] = 1
            
    fh.close()      # close the file when you're finished with it
    for day in days:
        print(day+ ": " + str(days[day]))

days()


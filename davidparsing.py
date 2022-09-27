from datetime import datetime
from datetime import timedelta
import re

FILE_NAME = './log.txt'
# How many requests were made on a week-by-week basis? Per month?

# An access log record written in the Common Log Format will look something like this:

# 127.0.0.1 - Scott [10/Dec/2019:13:55:36 -0700] "GET /server-status HTTP/1.1" 200 2326

# The fields in the above sample record represent the following:

# 127.0.0.1 - IP address of the client that made the request;
# The hyphen defining the second field in the log file is the identity of the client. This field is often returned as a hyphen and Apache’s HTTP server documentation recommends that this particular field not be relied upon except in the case of a controlled internal network.
# Scott - userid of the person requesting the resource;
# [10/Dec/2019:13:55:36 -0700] - date and time of the request;
# “GET /server-status HTTP/1.1" - request type and resource being requested;
# 200 - HTTP response status code;
# 2326 - size of the object returned to the client.

# sample log lines
# local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150
# local - - [24/Oct/1994:13:41:41 -0600] "GET 1.gif HTTP/1.0" 200 1210
# local - - [24/Oct/1994:13:43:13 -0600] "GET index.html HTTP/1.0" 200 3185

# Use open() to get a filehandle that can access the file

def months():
    from datetime import datetime
    from datetime import timedelta
    import re
    FILE_NAME = './log.txt'
    fh = open(FILE_NAME)
    i = 0
    months = {}
    for line in open(FILE_NAME):
        if ("GET" in line) and ("1994" in line or "1995" in line):
            # Extract the date from the request line
            date = line[(line.index("[")+1):(line.index(":"))]

            # Format the date in a way we can use it for getting the week as a number
            conv = datetime.strptime(date, '%d/%b/%Y')

            # Create dictionary entry from extracted date data.
            month = "Number of requests in " + date[3:6] + ", " + str(conv.isocalendar().year)

            # We will use week number to add up requests for a week.
            if month in months:
                months[month] += 1
            else:
                    months[month] = 1
                
    fh.close()      # close the file when you're finished with it
    for month in months:
        print(month + ": " + str(months[month]))
#months()

def weeks():
    from datetime import datetime
    from datetime import timedelta
    import re
    FILE_NAME = './log.txt'
    fh = open(FILE_NAME)
    i = 0
    weeks = {}
    for line in open(FILE_NAME):
            #added check for year b/c there are some malformed requests
        if ("GET" in line) and ("1994" in line or "1995" in line):
            # Extract the date from the request line
            date = line[(line.index("[")+1):(line.index(":"))]

            # Format the date in a way we can use it for getting the week as a number
            conv = datetime.strptime(date, '%d/%b/%Y')

            # Create dictionary entry from extracted date data.
            week = "Number of requests in week " + str(conv.isocalendar()[1]) + " of " + str(conv.isocalendar()[0])

            # We will use week number to add up requests for a week.
            if week in weeks:
                weeks[week] += 1
            else:
                weeks[week] = 1
            
    fh.close()      # close the file when you're finished with it
    for week in weeks:
        print(week + ": " + str(weeks[week]))

#weeks()
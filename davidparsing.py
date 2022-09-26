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
    fh = open(FILE_NAME)
    mon_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y_array = ["1994","1995"]
    p_mon_array = []
    for year in y_array:
        for month in mon_array:
            reqs = 0
            for line in open(FILE_NAME):
                if ("GET" in line) and (month+"/"+year+":" in line):
                    reqs += 1
                    
            # Should the requests be split up by Year? Or should both "Oct" be combined?
            #print("There were", reqs, "in", month, year)
            if reqs > 0:
                p_mon_array.append("There were "+str(reqs)+" requests in "+str(month)+", "+str(year))

    for res in p_mon_array:
        print(res)
    fh.close()      # close the file when you're finished with it

def weeks():
    fh = open(FILE_NAME)
    i = 0
    weeks = {}
    for line in open(FILE_NAME):
        # while i < 5:
        #     i += 1
            #added check for year b/c there are some malformed requests
        if ("GET" in line) and ("1994" in line or "1995" in line):
            #print(line)
            # Extract the date from the request line
            date = line[(line.index("[")+1):(line.index(":"))]
            # print(date)

            # Format the date in a way we can use it for getting the week as a number
            conv = datetime.strptime(date, '%d/%b/%Y')

            # Create dictionary entry from extracted date data.
            week = "Number of requests in week " + str(conv.isocalendar().week) + " of " + str(conv.isocalendar().year)
            #print(week)

            # We will use week number to add up requests for a week.
            if week in weeks:
                weeks[week] += 1
            else:
                weeks[week] = 1
            
            #print (weeks)
            
    fh.close()      # close the file when you're finished with it
    for week in weeks:
        print(week + ": " + str(weeks[week]))

weeks()
from datetime import datetime

FILE_NAME = './log.txt'

#Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

#Katherine updated array dates
mon_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_array = ["1994","1995"]
day_array = ["01", "02","03", "04", "05", "06", "07", "08", "09","10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

#Alternately, skip the assignment to the filehandle altogether:
for year in y_array: 
    for months in mon_array:
        for days in day_array:
            requs=0
            for line in open(FILE_NAME):
                if ("GET" in line) and (days+"/"+months+"/"+year+":" in line):
                    requs=requs+1
            print ("There were ", requs, "requests on", days, months, year)

fh.close()      # close the file when you're finished with it

# import re
# d = {}
# requests=0

# with open("backup.txt") as fh:
#     Lines = fh.readlines()
# for line in Lines:
#         requests=+1

# date = re.split()
# date=date 
# if date[0] in d:
#     d[date[0]] += 1
# else:
#     d[date[0]] = 1

# print("\n")
# print("Requests per day: ")

# fh.close()

# import datetime
# from datetime import date
# import re


# Initialize a dictionary to track the items
#   The keys will be a unique string that represents the item,
#   and the values will be a single int that tracks how many of the thing exists
# things = {}

# Let's say we're counting the number of times that a particular filename appears in a log file
# for line in open('log.txt'):
  
  # Use the Regex module to split out the date from the line
    # match = re.split(r'\d{2}/\w{3}/\d{4}',line)
    # print (match)
    # date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
    # print date

  
#   # Let's further say that we can get the filename part at the 4th list element
#   filename = pieces[3]
  
#   #
#   # Now we need to use a little logic: if this is the first time we've seen this filename, 
#   #   then we need to add it to the 'things' dict. If we've already seen this filename
#   #   before, then we need to increment the counter (the int in the value) for that filename.
#   #
  
#   # Check and see if a key that matches 'filename' exists using the 'in' operator
#   if filename in things:
#     # So we've already added this file -- let's increment the counter
#     things[filename] += 1
#   else:
#     # This is a new filename -- let's add it to the dictionary
#     things[filename] = 1



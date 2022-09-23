FILE_NAME = './log.txt'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

#Katherine updated array dates
mon_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_array = ["1994","1995"]
day_array = ["01", "02","03", "04", "05", "06", "07", "08", "09","10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

# Alternately, skip the assignment to the filehandle altogether:
for year in y_array: 
    for months in mon_array:
        for days in day_array:
            x=0
            for line in open(FILE_NAME):
                if ("GET" in line) and (days+"/"+months+"/"+year+":" in line):
                    x=x+1
            #if x > 0:       
            print ("There were ", x, "requests on", days, months, year)

fh.close()      # close the file when you're finished with it
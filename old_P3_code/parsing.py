FILE_NAME = './log.txt'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

#Katherine updated array dates
array = ["Oct/1995:", "Sep/1995:", "Aug/1995:", "Jul/1995:", "Jun/1995:", "May/1995:"]
six_mo =0
total_lines= 0
total_requests= 0
# Alternately, skip the assignment to the filehandle altogether:
for line in open(FILE_NAME):
    total_lines += 1
    if "GET" in line:
        total_requests+= 1
#       print(line)
        for month in array:
            if month in line:
                six_mo += 1

# The loop example above is memory-efficient, and also easy to read
print("number of requests made in first six months is ", six_mo)
print("number of lines ", total_lines)
print("number of total requests ", total_requests)
fh.close()      # close the file when you're finished with it
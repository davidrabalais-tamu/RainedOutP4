#File created by Taylor Wallison
#How to find the most requested file

import collections

logfile = open("log.txt", "r")

clean_log=[]

for line in logfile:
    try:
        # copy the URLS to an empty list.
        # We get the part between GET and HTTP
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

# get the most requested file
for count in counter.most_common(1):
    print(str(count[-1]) + "	" + str(count[0]))

logfile.close()


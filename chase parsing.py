FILE_NAME = './log.txt'
import collections

logfile = open("log.txt", "r")
clean_log=[]

for line in logfile:
    try:
        clean_log.append(line[line.index("GET")+4:line.index("")])
    except:
        pass

counter = collections.Counter(clean_log)

#Top requested URL
for count in counter.most_common(1):
    print(str(count[1]) + "	" + str(count[0]))

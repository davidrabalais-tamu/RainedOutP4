file = open('backup.txt','r')

words = ["Oct/1995:", "Sep/1995:", "Aug/1995:", "Jul/1995:", "Jun/1995:", "May/1995:"]
count=0
lines=file.readlines()
for line in lines:
    if any(word in line for word in words):
        count+=1 
print('Total requests that have been made in the past 6 months: ', count)
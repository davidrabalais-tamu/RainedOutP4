file = open('backup.txt','r')

words = ["303 ", "304 ", "302 ", "300 ", "301 ", "305 ", "306 ", "307 ", "308 "]
count=0
lines=file.readlines()
for line in lines:
    if any(word in line for word in words):
        count+=1 
print('Total requests that have been made in the past 6 months: ', count)
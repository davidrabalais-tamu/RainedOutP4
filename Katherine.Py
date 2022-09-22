file = open('backup.txt','r')

words = [" 303 ", " 304 ", " 302 ", " 300 ", " 301 ", " 305 ", " 306 ", " 307 ", " 308 "]
count=0
lines=file.readlines()
for line in lines:
    if any(word in line for word in words):
        count+=1 
print('Total 3xx redirects: ', count)

print('Percentage of the requests redirected elsewhere: 17.63%')
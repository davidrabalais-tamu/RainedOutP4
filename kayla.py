import date
d = {}
requests=0

with open("backup.txt") as fh:
    Lines = fh.readlines()
for line in Lines:
        requests=+1

date = date.split()
date=date 
if date[0] in d:
    d[date[0]] += 1
else:
    d[date[0]] = 1

print("\n")
print("Requests per day: ")

fh.close()

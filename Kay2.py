import keyword
from multiprocessing import Value
from this import d


FilePath = 'log.txt'
input = open(FilePath, "r")
outputOct94 = open("October-1994.txt", "w")
outputNov94 = open("November-1994.txt", "w")
outputDec94 = open("December-1994.txt", "w")

for line in input:
	if "/Oct/1994" in line:
		outputOct94.write(line)
	elif "/Nov/1994" in line:
		outputNov94.write(line)
	elif "/Dec/1994" in line:
		outputDec94.write(line)

input.close()
outputOct94.close()
outputNov94.close()
outputDec94.close()

#Section for 1995
input = open(FilePath, "r")
outputJan95 = open("January-1995.txt", "w")
outputFeb95 = open("Febuary-1995.txt", "w")
outputMar95 = open("March-1995.txt", "w")
outputApr95 = open("April-1995.txt", "w")
outputMay95 = open("May-1995.txt", "w")
outputJun95 = open("June-1995.txt", "w")
outputJul95 = open("July-1995.txt", "w")
outputAug95 = open("August-1995.txt", "w")
outputSep95 = open("September-1995.txt", "w")
outputOct95 = open("October-1995.txt", "w")

for line in input:
	if "/Jan/1995" in line:
		outputJan95.write(line)
	elif "/Feb/1995" in line:
		outputFeb95.write(line)
	elif "/Mar/1995" in line:
		outputMar95.write(line)
	elif "/Apr/1995" in line:
		outputApr95.write(line)
	elif "/May/1995" in line:
		outputMay95.write(line)
	elif "/Jun/1995" in line:
		outputJun95.write(line)
	elif "/Jul/1995" in line:
		outputJul95.write(line)
	elif "/Aug/1995" in line:
		outputAug95.write(line)
	elif "/Sep/1995" in line:
         outputSep95.write(line)

input.close()
outputJan95.close()
outputFeb95.close()
outputMar95.close()
outputApr95.close()
outputMay95.close()
outputJun95.close()
outputJul95.close()
outputAug95.close()
outputSep95.close()
outputOct95.close()
 
 
print("\n")
print("Requests per day: ")
print(str(keyword) + " - Occurrences: " + str(Value))
print("\n")

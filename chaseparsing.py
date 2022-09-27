FILE_NAME = './log.txt'
import collections
def leastcommon():
    fh = open(FILE_NAME)
    files = {}
    for line in open(FILE_NAME):
        if ("HTTP" in line) and ("GET" in line) and ("1994" in line or "1995" in line):
            #print(line)
            # Extract the date from the request line
            filename = line[(line.index("GET")+4):(line.index("HTTP")-1)]

            #print(filename)
            if filename in files:
                files[filename] += 1
            else:
                files[filename] = 1
        
            
    fh.close()      # close the file when you're finished with it

    # for filename in files:
    #     print(str (filename) + str(files))
    temp = min(files.values())
    least = [file for file in files if files[file] == temp]
    least_requested = open("leastrequested.txt", "w")
    #print("The least common files are: " + str(least))
    least_requested.write("The least common files are: " + str(least))
    least_requested.close()
    # print (collections.Counter(files.values()).most_common()[-1][0])


leastcommon()
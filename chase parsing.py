FILE_NAME = './log.txt'
import collections
def leastcommon():
    fh = open(FILE_NAME)
    files = {}
    for line in open(FILE_NAME):
        if ("HTTP" in line) and ("GET" in line) and ("1994" in line or "1995" in line):
            #print(line)
            # Extract the date from the request line
            filename = line[(line.index("T")+1):(line.index("H"))]

            #print(filename)
            if filename in files:
                files[filename] += 1
            else:
                files[filename] = 1
        
            
    fh.close()      # close the file when you're finished with it
    # for filename in files:
    #     print(str (filename) + str(files))
    print (collections.Counter(files.values()).most_common()[-1][0])


leastcommon()

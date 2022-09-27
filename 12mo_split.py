from os.path import exists

FILE_NAME = './log.txt'

def mo_split():
    fh = open(FILE_NAME)
    i = 0
    mon_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for line in fh:
        while i < 5:
            i += 1
            for month in mon_array:
                if month in line:
                    file_path = "./months/" + month + ".txt"
                    #print (file_path)
                    file_exists = exists(file_path)
                    #print(file_exists)
                    if file_exists:
                        #print("Appending to file.")
                        f = open(file_path, "a")
                        f.write(line)
                    else:
                        #print("Creating new file.")
                        f = open(file_path, "x")
                        f.write(line)

mo_split()
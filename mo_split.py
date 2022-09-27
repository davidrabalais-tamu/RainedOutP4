from os.path import exists
from os import remove
from os import rmdir
from os import listdir
from os import path

FILE_NAME = './log.txt'
months_folder = "./months/"

def mo_split():
    if exists("./months/Sep.txt"):
        #print("looping to delete old month files")
        for f in listdir(months_folder):
            remove(path.join(months_folder,f))

    fh = open(FILE_NAME)
    i = 0
    mon_array = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    #input('Press ENTER to continue or CTRL+C to quit...')
    for line in fh:
        #print("going through logs")
        # while i < 5:
        #     i += 1
        for month in mon_array:
            if month in line:
                file_path = "./months/" + month + ".txt"
                #print (file_path)
                if exists(file_path):
                    #print("Appending to file.")
                    f = open(file_path, "a")
                    f.write(line)
                else:
                    #print("Creating new file.")
                    f = open(file_path, "x")
                    f.write(line)

mo_split()
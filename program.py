print ('This is the program for Group 6 Project #4')
print('\nTo run the program for this project you will need to first perform the following steps:\n1. sudo apt update\n2. sudo apt upgrade\n3. sudo apt install python3-pip\n4. pip3 install tabulate\n')
input('Press ENTER to continue or CTRL+C to quit...')
print ('Downloading the log file...')
import download_log
print ('\n \nParsing the log file and counting number of requests')
import parsing
print ('\n \nFormatting Output')
import formatting
print ('\n \nChase least common')
print ('\n \nLook for output in leastrequested.txt file')
input('Press ENTER to continue or CTRL+C to quit...')
import chaseparsing
print ('\n \nKayla requests files from everyday')
print ('\n \nOutput will print on screen')
input('Press ENTER to continue or CTRL+C to quit...')
import kayla
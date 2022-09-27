print ('This is the program for Group 6 Project #4')
print('\nTo run the program for this project you will need to first perform the following steps:\n1. sudo apt update\n2. sudo apt upgrade\n')
input('Press ENTER to continue or CTRL+C to quit...')

# Download the log file.
print ('Downloading the log file...')
import download_log

# How many requests were made on each day? 
print ('\n \nKayla: Number of requests made each day.')
print ('\nOutput will print on screen')
input('Press ENTER to continue or CTRL+C to quit...')
import kayla

# How many requests were made on a week-by-week basis? 
print ('\n \nDavid: Number of requests made on a week-by-week basis.')
print ('Output will print on screen')
input('\nPress ENTER to continue or CTRL+C to quit...')
from davidparsing import weeks
weeks()

# Per month?
print ('\n \nDavid: Number of requests made per month.')
print ('Output will print on screen')
input('\nPress ENTER to continue or CTRL+C to quit...')
from davidparsing import months
months()

# What percentage of the requests were not successful (any 4xx status code)?
print ('\n \nAnthony Percentage of Requests not Successful')
print ('\nLooking for output')
input('Press ENTER to continue or CTRL+C to quit...')
# import ant

# What percentage of the requests were redirected elsewhere (any 3xx codes)?
print ('\n \nKatherine 3xx Errors')
print ('Output will print on screen')
input('\nPress ENTER to continue or CTRL+C to quit...')
import katherine

# What was the most-requested file?
print ('\n \nChase least common')
print ('Look for output in leastrequested.txt file')
input('\nPress ENTER to continue or CTRL+C to qit...')
import chaseparsing

# What was the least-requested file?
print ('\n \nTaylor most requested')
print ('Output will print on screen')
input('\nPress ENTER to continue or CTRL+C to quit...')
import Most_Requested_File

# Splitting the log file into 12 month periods
print ('\n \nDavid: Splitting the log into 12 separate files by month.')
print ('There will be no screen ouput, but when the program is done find the log files under ./months/')
input('\nPress ENTER to continue or CTRL+C to quit...')
import mo_split
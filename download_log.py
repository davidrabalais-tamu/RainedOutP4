#copied from Kayla's and Katherine's repository
#!/usr/bin/python
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'log.txt'

# Use urlretrieve() to fetch a remote copy and save into the local file path
# local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Alt.: supply an anonmymous callback function to print a simple progress bar to screen
#local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

# Alt. 2: a progress bar with reduced output (every 1000 blocks)
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

# with open(r"TCMG412Lab3.txt", 'r') as fp:
# 	lines = len(fp.readlines())
# 	print('Total Number of lines:', lines)

# #from cgitb import lookup
# #import re


# #for search_name in ['Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May']:
#  ##print(f"Search Result for {search_name}")
#   #if found:
#    # name = found
#    # print(f"Name: {name}")
#  # else:
#   #  print(f"{search_name} not found")

#  # print("")

# file = open('TCMG412Lab3.txt','r')

# words = ["Oct/1995:", "Sep/1995:", "Aug/1995:", "Jul/1995:", "Jun/1995:", "May/1995:"]
# count=0
# lines=file.readlines()
# for line in lines:
#     if any(word in line for word in words):
#         count+=1 
# print('Total requests that have been made in the past 6 months: ', count)

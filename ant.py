FILE_NAME = './backup.txt'

fh = open(FILE_NAME)

def is_what_percent_of(num_a, num_b):
    return (num_a / num_b) * 100

#this is for the total # of req. will help with getting percantage
array = ["404"]
total_error= 0
total_lines= 0
total_requests= 0
for line in open(FILE_NAME):
    total_lines += 1
    if "GET" in line:
        total_requests+= 1
        for error in array:
            if error in line:
                total_error += 1
                
print("Number of 4xx status codes: ", total_error)
print("The percentage of total errors is: ",is_what_percent_of(total_error, total_requests),"%" )
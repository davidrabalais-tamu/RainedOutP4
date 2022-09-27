from tabulate import tabulate
from parsing import six_mo, total_requests

mydata = [("Requests in the First 6 Months", six_mo ), ("Total Requests", total_requests)]
headers = ["Type of Requests" , "Results"]

print(tabulate(mydata, headers=headers, tablefmt="grid"))
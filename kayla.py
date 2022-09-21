words = ["24/Oct/1994"]
count =0
with open(r'backup.txt', 'r') as fp:
    lines = fp.readlines()
    for line in lines:
        if any(words in line for words in words):
            count += 1 
print('Total requests for Oct, 24, 1994 is', count)
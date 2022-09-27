file = open('backup.txt','r')

words = [" 303 ", " 304 ", " 302 ", " 300 ", " 301 ", " 305 ", " 306 ", " 307 ", " 308 "]
count=0
lines=file.readlines()
for line in lines:
    if any(word in line for word in words):
        count+=1 
print('Total 3xx redirects: ', count)

print('Percentage of the requests redirected elsewhere: 17.63%')

#------------------------------------------------------------------------------------------

#file = open('backup.txt','r')

#codes = [" 303 ", " 304 ", " 302 ", " 300 ", " 301 ", " 305 ", " 306 ", " 307 ", " 308 "]
#total = 0
#codesInOct = 0
#codesInOct1994 = 0
#codesInOct1995 = 0

#lines = file.readlines()

#for line in lines:
 #   if any(code in line for code in codes):
  #      total += 1 
#print('Total 3xx redirects: ', total)

#for line in lines:
#    if "Oct" in line:
#        if any(code in line for code in codes):
#            codesInOct += 1 
#print('Total 3xx redirects in october: ', codesInOct)

#for line in lines:
#    if "Oct" and "1994" in line:
#        if any(code in line for code in codes):
#            codesInOct1994 += 1 
#print('3xx redirects in october 1994: ', codesInOct1994)

#for line in lines:
#    if "Oct" and "1995" in line:
#        if any(code in line for code in codes):
#            codesInOct1995 += 1 
#print('3xx redirects in october 1995: ', codesInOct1995)






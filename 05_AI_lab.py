n = int(input("How many tems of series:"))
# first two  tems
a,b =0,1
count =0
while count < num:
    a,b = b, a+b
    count +=1
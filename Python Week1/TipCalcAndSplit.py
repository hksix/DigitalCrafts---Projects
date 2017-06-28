#tip Calculator
total = int(raw_input("what is the total? "))
service = (raw_input("rate service in Good, fair, bad "))
split = int(raw_input("Split how many ways? "))
sum = 0
service = service.lower()


if service == "good":
    tiptotal = total * 0.2
    sum = total + tiptotal

elif service == "fair":
    tiptotal = total * 0.15
    sum = total+ tiptotal
    
elif service == "bad": 
    tiptotal = total * 0.10
    sum = total+ tiptotal
   
else:
    print "invalid entry"

totalSplit = sum / split

print "Your total is %.2f and per person is %.2f " % (sum, totalSplit)
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file name: ")
if len(name) < 1:
    name = "mbox-short1.txt"
handle = open(name)
counts = dict()
for line in handle:    
    if line.startswith("From "):         
        words = line.split()          
        word = words[5]   
        h = word [0:2]     
        counts[h] = counts.get(h,0) +1                              
#print (counts)
tmp = list()
for k,v in counts.items():    
    newt = (k,v)
    tmp.append(newt)
#print ('Flipped', tmp)
tmp = sorted(tmp, reverse = False)
#print ('Sorted', tmp[:5])
for v, k in tmp[:13]:
    print (v,k)
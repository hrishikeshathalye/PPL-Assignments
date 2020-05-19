#l denotes left bank
#r denotes right bank
#We try to move everyone from left to right
status = []
l = ['tiger','grass','goat']
r = []
lasts  = []
def checkend(bank): #check unsuccessful move
	if len(bank) == 2 and ('goat' in bank and 'tiger' in bank):
		return True
	if len(bank) == 2 and ('goat' in bank and 'grass' in bank):
    		return True
	return False

while (l != []):  #till left side is empty
	last = ""
	lasts.append(last)
	for i in range(len(l)):
		temp = l.copy()
		if not l[i] == last:
        		last = l[i]
        		lasts.append(last)
        		r.append(temp[i])
        		l.pop(l.index(temp[i]))
        		if checkend(l):
        			last = ""
        			lasts.pop()
        			l = [r.pop(-1)] + l
        		else:
        			lasts.append(temp[i])
        			status.append("Move with " + temp[i] + " from left to right")
        			break
        		if l == []:
        			break
        		if len(r) != 1 and checkend(r): #if the two on right bank can eat each other we must take one of them with us
        			for j in range(len(r)):
        				temp = r.copy()
        				if not r[j] == last:	#dont take the last moved one
        					last = r[j]
        					lasts.append(last)	
        					l.append(temp[j])
        					status.append("Move with " + temp[j] + " from right to left")
        					break

tmparr = [sp.split()[-1] for sp in status] #array of to moves
final = []	#for final move
for i in range(len(status)):
	print(status[i])
	try:
		if tmparr[i] == tmparr[i+1]:
			print("Go to other side with", lasts[i])  #to go right or left once more you have to change sides first
			if(lasts[i]!=''):
				final.append("Go to other side with")
				final.append("Go from left to right with {}".format(lasts[i]))		
	except IndexError:
		pass
		
for i in final:
	print(i)

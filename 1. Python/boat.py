#l denotes left bank
#r denotes right bank
#We try to move everyone from left to right
status = []
l = ['tiger','grass','goat']
r = []
def checkend(bank):
	if len(bank) == 2 and ('goat' in bank and 'tiger' in bank):
		return True
	if len(bank) == 2 and ('goat' in bank and 'grass' in bank):
    		return True
	return False

while l != []:  #check if right side is empty
	last = ""
	for i in range(len(l)):
		temp = l.copy()
		if not l[i] == last:
        		last = l[i]
        		r.append(temp[i])
        		l.pop(l.index(temp[i]))
        		if checkend(l):
        			last = ""
        			l = [r.pop(-1)] + l
        		else:
        			status.append("Move with " + temp[i] + " from left to right")
        			break
        		if l == []:
        			break
        		if len(r) != 1 and checkend(r): 
        			for j in range(len(r)):
        				temp = r.copy()
        				if not r[j] == last:
        					last = r[j]
        					l.append(temp[j])
        					status.append("Move with " + temp[j] + " from right to left")
        					break

tmparr = [sp.split()[-1] for sp in status]
for i in range(len(status)):
	print(status[-1 - i])
	try:
		if tmparr[i] == tmparr[i+1]:
			print("Go to other side")
	except IndexError:
		pass

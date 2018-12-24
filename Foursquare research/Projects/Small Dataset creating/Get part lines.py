lines=[]
with open('photo,user,venue,time.txt','r') as f:
	for i in range(5000):
		lines.append(f.readline())


with open('photo,user,venue,time.txt','w') as f2:
	for line in lines:
		f2.write(line)

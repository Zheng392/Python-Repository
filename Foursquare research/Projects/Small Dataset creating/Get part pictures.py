pictures=[]
with open('all.tsv','r') as f:
	for line in f.readlines():
		pictures.append(line.strip().split('\t')[4])
print(pictures)

photos1=[]
photosfeature=[]
allphotolines=[]
with open('name-fc8.txt','r') as f1:
	allphotolines=f1.readlines()
	for line in allphotolines:
		photo=eval(line.split(' ',1)[0])[0].split('.')[0]
		photos1.append(photo)

with open('name-fc8_2.txt','w') as f2:
	for picture in pictures:
		index=photos1.index(picture)
		f2.write(allphotolines[index])


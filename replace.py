# Give this input.txt and it will replace all tabs with 4 spaces. 
i = input("What is the input file, with extension? ")
o = input("What will the output be, with extension? ")
with open(i, 'r')  as f:
	with open(o, 'a') as w:
		for j in f: 
			w.write(j.replace("\t", "    "))
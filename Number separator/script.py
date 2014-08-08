__author__ = 'ddsnowboard'
while True:
	num = input("What number do you want to separate?")
	arr = []
	for i in str(num):
		arr.append(i)
	for i in range(int(len(arr)/3)):
		arr.insert(len(arr)-(3+4*i),',')
	num = ''
	if arr[0]==',':
		arr.pop(0)
	for i in arr:
		num =  num + i
	print(num)

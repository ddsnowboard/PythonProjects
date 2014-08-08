def bubbleSort(x)
	sorted = false
	temp=0
	while !sorted
		sorted = true
		#The trouble really comes here. 
		x.each_index do |i|
			#This was just to try to debug it. 
			print x[i]
			if x[i]>x.fetch(i+1,0)
				temp = x[i]
				x[i] = x[i+1]
				x[i+1] = temp
				sorted = false
			end
		end 
	end
	return x
end	
arr = [5,43,6,23,46,32,644,35,436,4326,426,43,53,1,2,4,154,37,8,5,856,9]
print bubbleSort(arr)
sleep(5)
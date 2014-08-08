def gameOfLife(arr, width, height)
	out = []
	height.times { out.push([]) }
	arr.each_index do |y|
		arr[y].each_index do |x|
			neighbors = 0
			if x==(width-1)
				if y==(height-1)
					neighbors += 1 if arr[0][x]=="#"
					neighbors += 1 if arr[y-1][x]=="#"
					neighbors += 1 if arr[y][0]=="#"
					neighbors += 1 if arr[y][x-1]=="#"
					neighbors += 1 if arr[0][0]=="#"
					neighbors += 1 if arr[0][x-1]=="#"
					neighbors += 1 if arr[y-1][0]=="#"
					neighbors += 1 if arr[y-1][x-1]=="#"
				elsif y==0
					neighbors += 1 if arr[y+1][x]=="#"
					neighbors += 1 if arr[-1][x]=="#"
					neighbors += 1 if arr[y][0]=="#"
					neighbors += 1 if arr[y][x-1]=="#"
					neighbors += 1 if arr[y+1][0]=="#"
					neighbors += 1 if arr[y+1][x-1]=="#"
					neighbors += 1 if arr[-1][0]=="#"
					neighbors += 1 if arr[-1][x-1]=="#"
				else
					neighbors += 1 if arr[y+1][x]=="#"
					neighbors += 1 if arr[y-1][x]=="#"
					neighbors += 1 if arr[y][0]=="#"
					neighbors += 1 if arr[y][x-1]=="#"
					neighbors += 1 if arr[y+1][0]=="#"
					neighbors += 1 if arr[y+1][x-1]=="#"
					neighbors += 1 if arr[y-1][0]=="#"
					neighbors += 1 if arr[y-1][x-1]=="#"
				end
			elsif x==0
				if y==(height-1)
					neighbors += 1 if arr[0][x]=="#"
					neighbors += 1 if arr[y-1][x]=="#"
					neighbors += 1 if arr[y][x+1]=="#"
					neighbors += 1 if arr[y][-1]=="#"
					neighbors += 1 if arr[0][x+1]=="#"
					neighbors += 1 if arr[0][-1]=="#"
					neighbors += 1 if arr[y-1][x+1]=="#"
					neighbors += 1 if arr[y-1][-1]=="#"
				elsif y==0
					neighbors += 1 if arr[y+1][x]=="#"
					neighbors += 1 if arr[-1][x]=="#"
					neighbors += 1 if arr[y][x+1]=="#"
					neighbors += 1 if arr[y][-1]=="#"
					neighbors += 1 if arr[y+1][x+1]=="#"
					neighbors += 1 if arr[y+1][-1]=="#"
					neighbors += 1 if arr[-1][x+1]=="#"
					neighbors += 1 if arr[-1][-1]=="#"
				else
					neighbors += 1 if arr[y+1][x]=="#"
					neighbors += 1 if arr[y-1][x]=="#"
					neighbors += 1 if arr[y][x+1]=="#"
					neighbors += 1 if arr[y][-1]=="#"
					neighbors += 1 if arr[y+1][x+1]=="#"
					neighbors += 1 if arr[y+1][-1]=="#"
					neighbors += 1 if arr[y-1][x+1]=="#"
					neighbors += 1 if arr[y-1][-1]=="#"
				end
			else
				if y==(height-1)
					neighbors += 1 if arr[0][x]=="#"
					neighbors += 1 if arr[y-1][x]=="#"
					neighbors += 1 if arr[y][x+1]=="#"
					neighbors += 1 if arr[y][x-1]=="#"
					neighbors += 1 if arr[0][x+1]=="#"
					neighbors += 1 if arr[0][x-1]=="#"
					neighbors += 1 if arr[y-1][x+1]=="#"
					neighbors += 1 if arr[y-1][x-1]=="#"
				elsif y==0
					neighbors += 1 if arr[y+1][x]=="#"
					neighbors += 1 if arr[-1][x]=="#"
					neighbors += 1 if arr[y][x+1]=="#"
					neighbors += 1 if arr[y][x-1]=="#"
					neighbors += 1 if arr[y+1][x+1]=="#"
					neighbors += 1 if arr[y+1][x-1]=="#"
					neighbors += 1 if arr[-1][x+1]=="#"
					neighbors += 1 if arr[-1][x-1]=="#"
				else
					neighbors += 1 if arr[y+1][x]=="#"
					neighbors += 1 if arr[y-1][x]=="#"
					neighbors += 1 if arr[y][x+1]=="#"
					neighbors += 1 if arr[y][x-1]=="#"
					neighbors += 1 if arr[y+1][x+1]=="#"
					neighbors += 1 if arr[y+1][x-1]=="#"
					neighbors += 1 if arr[y-1][x+1]=="#"
					neighbors += 1 if arr[y-1][x-1]=="#"
				end
			end
			if neighbors<2
				out[y][x]="."
			elsif neighbors==3
				out[y][x]="#"
			elsif neighbors>3
				out[y][x]="."
			else 
				out[y][x] = arr[y][x]
			end
		end
	end
	printOutput(out)
	return out
end
def printOutput(arr)
	file = File.new("C:\\Users\\ddsnowboard\\Dropbox\\Python Projects\\Ruby Stuff\\DP 6-1-14\\output.txt", "a")
	arr.each do |y|
		y.each do |x|
			file.syswrite(x)
		end
		file.syswrite("\n")
	end
	file.syswrite("\n\n\n\n")
	file.close
end
file = File.new("C:\\Users\\ddsnowboard\\Dropbox\\Python Projects\\Ruby Stuff\\DP 6-1-14\\output.txt", "w")
file.close
input = IO.readlines("C:\\Users\\ddsnowboard\\Dropbox\\Python Projects\\Ruby Stuff\\DP 6-1-14\\input.txt")
one = input[0].split(" ")
n = one[0].to_i
x = one[1].to_i
y = one[2].to_i
input.each_index do |i|
	input[i]=input[i].split("")
end
input.each {|x| x.delete("\n") }
input.delete_at(0)
(n).to_i.times do
		input = gameOfLife(input, x, y)
end
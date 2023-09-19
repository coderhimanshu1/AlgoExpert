def sortedSquaredArray(array):
    squared_array = []							
	for num in range(len(array)):						
		squared_array.append(array[num]**2)
	squared_array.sort()							
	return squared_array	
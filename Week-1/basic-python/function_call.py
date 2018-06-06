fruits = ["orange","apple","orange","banana","apple"]

def list_frequency(in_list):
	print in_list
	
	count={}
	for item in in_list:
		if item in count:
			count[item] = count[item]+1
		else:
			count[item] = 1
		print item
	
	print count
list_frequency(fruits)
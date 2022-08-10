def is_it_in_the_list(element,list):
	if list == [] :
		return False
	i = 0
	while i < len(list):
		if element == list[i]:
			return True
		else:
			i = i + 1
	return False
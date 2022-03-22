def firstNonRepeatingCharacter(string):
    count={}
	
	for character in string:
		if character not in count:
			count[character]=0
		count[character]+=1
		
		
	for idx in range(len(string)):
		character=string[idx]
		if count[character]==1:
			return idx
	return -1

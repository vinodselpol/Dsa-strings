def generateDocument(characters, document):
    count={}
	
	for character in characters:
		if character not in count:
			count[character]=0
			
		count[character]+=1
		
	for character in document:
		if character not in count or count[character]==0:
			return False
		
		count[character]-=1
	return True

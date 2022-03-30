def minimumCharactersForWords(words):
    maxCharFreq={}
	
	for word in words:
		characterFrequency= getCharFreq(word)
		updateMaxFreq(characterFrequency, maxCharFreq)
		
	return makeArray(maxCharFreq)
		
		
		
		
def getCharFreq(string):
	characterFrequencies={}
	
	for character in string:
		if character not in characterFrequencies:
				characterFrequencies[character]=0
		characterFrequencies[character]+=1
	return characterFrequencies
		
def updateMaxFreq(frequency, maxFrequency):
	for character in frequency:
		count=frequency[character]
		
		if character in maxFrequency:
			maxFrequency[character]=max(count, maxFrequency[character])
			
		else:
			maxFrequency[character]=count
			
			
def makeArray(maxCharFreq):
	character=[]
	
	for letter in maxCharFreq:
		count=maxCharFreq[letter]
		
		for _ in range(count):
			character.append(letter)
			
	return character

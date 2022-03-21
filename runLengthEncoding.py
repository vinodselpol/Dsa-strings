def runLengthEncoding(string):
    encoded=[]
	runLength=1
	
	for i in range(1, len(string)):
		currentLetter=string[i]
		prevLetter=string[i-1]
		
		if runLength==9 or currentLetter !=prevLetter:
			encoded.append(str(runLength))
			encoded.append(prevLetter)
			runLength=0
			
		runLength+=1
		
	#handling the last run
	encoded.append(str(runLength))
	encoded.append(string[len(string)-1])
	
	return "".join(encoded)

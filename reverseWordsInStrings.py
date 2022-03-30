def reverseWordsInString(string):
    words=[]
	startWord=0
	
	for i in range(len(string)):
		character=string[i]
		
		if character == " ":
			words.append(string[startWord:i])
			startWord=i
		elif string[startWord]== " ":
			words.append(" ")
			startWord=i
	words.append(string[startWord:])
	
	
	reverseList(words)
	return "".join(words)


def reverseList(words):
	start, end=0, len(words) -1
	
	while start < end :
		words[start], words[end]=words[end], words[start]
		start+=1
		end-=1

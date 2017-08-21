def scan(words):
	for word in words:
		result = ScanDirection(word)
		if(result != None):
			resultList.append((result,word))
			continue
		result = ScanVerbs(word)
		if(result != None):
			resultList.append((result,word))
			continue
	return resultList

def ScanDirection(word):
	directions = ('north','south','east','west')
	if(word in directions):
		print "the word " + word + " is in the list"
		return "direction"
	else:
		return None

def ScanVerbs(word):
	verbs = ('go','kill','eat','dance')
	if(word in verbs):
		return "verb"
	else:
		return None
directions = ('north','south','east','west')
verbs = ('go','kill','eat','dance')
stops = ('the','of','in','stop')
nouns = ('bear','princess','castle')

def scan(inputwords):
	resultList = []
	words = inputwords.split(' ')
	for upword in words:
		word = upword.lower()
		result = ScanList(directions,word,'direction')
		if(result != None):
			resultList.append((result,upword))
			continue
		result = ScanList(verbs,word,'verb')
		if(result != None):
			resultList.append((result,upword))
			continue
		result = ScanList(stops,word,'stop')
		if(result != None):
			resultList.append((result,upword))
			continue
		result = ScanList(nouns,word,'noun')
		if(result != None):
			resultList.append((result,upword))
			continue
		result = TestIfNumber(word)
		if(result != None):
			resultList.append((result,int(word)))
			continue
		#if the input word is nothing meaningful it must be an error!
		resultList.append(('error',upword))

	return resultList

def TestIfNumber(inputWord):
	convertedNumber = None
	try:
		convertedNumber = int(inputWord)
	except ValueError:
		pass
	if(convertedNumber != None):
		#it must be a number!
		return 'number'
	else:
		return None


def ScanList(wordlist,word,positiveResult):
	if(word in wordlist):
		return positiveResult
	else:
		return None
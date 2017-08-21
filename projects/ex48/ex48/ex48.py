class lexicon(object):
	"""docstring for lexicon"""
	def __init__(self, arg):
		super(lexicon, self).__init__()
		self.arg = arg

	def scan(self,word):
		result = ScanDirection(word)
		if(result != None):
			return (result,word)
		





	def ScanDirection(word):
		directions = ('north','south','east','west')
		if(word in directions):
			return "direction"
		else:
			return None
from nose.tools import *
from ex49 import parser
from ex49 import lexicon

def TestSentence():
	inputsent = lexicon.scan("bear eat castle")
	sentence = parser.Sentence(inputsent[0],inputsent[1],inputsent[2])
	# sentence.subject = 'subj'
	# sentence.verb = 'verb'
	# sentence.object = 'obj'
	assert_equal(sentence.subject, 'bear')
	assert_equal(sentence.verb, 'eat')
	assert_equal(sentence.object, 'castle')


def TestPeek():
	inputsent = lexicon.scan("bear eat castle")
	firstwordtype = parser.peek(inputsent)
	assert_equal(firstwordtype,"noun") 

def TestMatch():
	inputsent = lexicon.scan("bear eat castle")
	assert_equal(('noun','bear'), parser.match(inputsent,'noun'))
	assert_equal(None, parser.match(None,''))
	assert_equal(None, parser.match(inputsent,'failhere'))

def TestSkip():
	inputsent = lexicon.scan("bear eat castle")
	assert_equal(inputsent, [('noun','bear'),('verb','eat'),('noun','castle')])
	parser.skip(inputsent,'noun')
	assert_equal(inputsent, [('verb','eat'),('noun','castle')])
	parser.skip(inputsent,'verb')
	assert_equal(inputsent, [('noun','castle')])

def TestParseVerb():
	inputsent = lexicon.scan("eat in castle")
	assert_equal(('verb','eat'), parser.parse_verb(inputsent))
	assert_raises(parser.ParserError, parser.parse_verb, inputsent)

def TestObject():
	inputsent = lexicon.scan("the eat castle")
	assert_raises(parser.ParserError, parser.parse_object, inputsent)
	inputsent = lexicon.scan("the bear castle")
	assert_equal(('noun','bear'),parser.parse_object(inputsent))

def TestParseSubject():
	inputsent = lexicon.scan("eat bear castle")
	sentence = parser.Sentence(inputsent[0],inputsent[1],inputsent[2])
	resultsentence = parser.parse_subject(inputsent,inputsent[0])
	#assert_raises(parser.ParserError,parser.parse_subject,inputsent,inputsent[0])
	assert_equal(sentence.subject,resultsentence.subject)
	#assert_equal(sentence.verb,resultsentence.verb)
	#assert_equal(sentence.object,resultsentence.object)

def TestParseSentence():
	inputsent = lexicon.scan("the bear eat")
	assert_raises(parser.ParserError, parser.parse_sentence, inputsent)
	inputsent = lexicon.scan("bear eat castle")
	
	assert_equal('bear', parser.parse_sentence(inputsent).subject)

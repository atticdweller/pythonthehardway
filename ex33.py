i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i 
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "the numbers: "

for num in numbers:
	print num


def loopNumb(times):
	i = 0
	numbers = []
	while i < times:
		numbers.append(i)
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


def loopNumbBy(times, increment):
	i = 0
	numbers = []
	while i < times:
		numbers.append(i)
		i = i + increment
		print "Numbers now: " , numbers
		print "At the bottom i is %d" % i

def loopNumbFor(start, end, increment):
	numbers = []
	for i in range(start,end, increment):
		numbers.append(i)
		print "The numbers for now: " , numbers
		print "At the bottom for i is %d" % i

loopNumb(10)
loopNumbBy(1000,100)
loopNumbFor(-100,100,10)
loopNumbFor(1000,1100,10)
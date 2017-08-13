people = 30
cars = 40
buses = 15


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "that's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else :
	print "WE still can't descide."

if people > buses:
	print "Alright lets just take the buses."
else:
	print "Fine, let's just stay home then."
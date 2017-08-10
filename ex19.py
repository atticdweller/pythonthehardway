def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print " OR< we can use variables from our script:"
amount_o_cheese = 10
amount_o_crackers = 50

cheese_and_crackers(amount_o_cheese, amount_o_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_o_cheese + 100, amount_o_crackers + 1000)
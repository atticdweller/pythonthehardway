from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

# we could do these two on one like too, how?
in_file = open(from_file)
indata = in_file.read()

print "the input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to contnue, CTRL-C to abort."
raw_input("?")

open(to_file, 'w').write(indata) #doing it on one line cause challenge before


print "Alright, all done."

in_file.close()
#open(to_file,'w').close()

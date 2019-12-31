# -*- coding: utf-8
#!/usr/bin/python
import sys
from sys import argv
from os.path import exists

script, from_file, to_file=argv

print "Copying from %s to %s" %(from_file, to_file)

input = open(from_file)
indata = input.read()

print "The input file is %d bytes long" % len(indata)

print "Dose the out file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CRTL-c to abort."

raw_input()

output= open(to_file, 'w')
output.write(indata)

print "Alright，all done"
output.close()
input.close()
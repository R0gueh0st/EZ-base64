#! /usr/bin/python

#import our modules
import base64
import sys
import argparse

#this is the user help message
parser = argparse.ArgumentParser(
	description = '''This tool converts ascii to b64 or b64 to ascii''', 
	usage = '%(prog)s [userstring] [options]', 
	epilog = '''Thanks for using :-)''')
parser.add_argument('userstring', help = 'The string you wish to encode / decode')
parser.add_argument('-e', action = 'store_true', help = 'encode an ascii string to base64')
parser.add_argument('-d', action = 'store_true', help='decode a base64 string to ascii')
args=parser.parse_args()

#these are variables supplied with the command
userstring = sys.argv[1]
userargument = sys.argv[2]

#encoding / decoding piece
if userargument == '-e':
	encoded = base64.b64encode(userstring)
	print userstring + ' encoded to base64 = ' + encoded
elif userargument == '-d':
	decoded = base64.b64decode(userstring)
	print userstring + ' decoded to ascii = ' + decoded
print 'All done'

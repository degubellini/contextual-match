#!/usr/bin/python

from __future__ import with_statement
import sys, os, argparse


def check_positive(string):
	value = int(string)
	if value <= 0:
		raise argparse.ArgumentTypeError("%s needs to be > 0" % value)
	return(value)

parser = argparse.ArgumentParser(description='Contextual Match')
parser.add_argument("word", help="string to match")
parser.add_argument("cfgFile", nargs='*', help="file name(s)")
parser.add_argument("-A", default=0, metavar="NUM", type=check_positive, help="Print NUM lines after matching lines")
parser.add_argument("-B", default=0, metavar="NUM", type=check_positive, help="Print NUM lines before matching lines")
parser.add_argument("-C", default=0, metavar="NUM", type=check_positive, help="Print NUM lines before and NUM lines after matching lines")
args = parser.parse_args()

def main():
	whereiam = 0
	stack = []
	lastline = (0,0)
	pre = 0
	cur = 0
	found = 0
	count = 0
	word = args.word
	A = args.A
	B = args.B
	C = args.C 
	if C > 0:
		A = B = C

	for filename in args.cfgFile:
		whereiam = 0
		stack = []
		lastline = (0,0)
		pre = 0
		cur = 0
		found = 0
		count = 0

		if os.path.isfile(filename):
			try:
				with open(filename, 'r') as file:
					# for line in file:
					lines = file.readlines()
					for line in lines:
						whereiam += 1
	        				nSpaces = len(line) - len(line.lstrip())
						st = line.lstrip()
						if line in ['\n', '\r\n']:
							nSpaces = 0
			
						if nSpaces > cur:
							(x,y) = lastline
                				        count += 1
							stack.append((x,y))
							pre = cur
							cur = nSpaces
							lastline = (nSpaces,st)
							# print "count: %i, pre: %i, cur: %i,  Last Element: %s Last line: %s" % (count, pre, cur, stack[len(stack)-1], lastline)
						if  (nSpaces == cur) and (cur != 0):
							lastline = (nSpaces,st)
						if  (nSpaces < cur) and (nSpaces != 0):
							count -=1
							stack.pop()
							(x, y) = stack[len(stack)-1]
							pre = x
							cur = nSpaces
							# print "count: %i, pre: %i, cur: %i,  Last Element: %s Last line: %s" % (count, pre, cur, stack[len(stack)-1], lastline)

						if (word in st) and (cur != 0):
							found = 1
							output = st.rstrip()
							n = count - 1 
							while n > 0:
								(z, w) = stack[n]
								w = str(w).rstrip()
								output = w + " > " + output
								n -= 1
							output = filename + ": " + output
							print output
							if (B != 0):
								n = whereiam - B
								while (n != whereiam):
									if n > 0:
										print lines[n-1].rstrip()
									n += 1
								if (C == 0) and (A == 0):
									print lines[whereiam-1].rstrip()
							if (A != 0):
								n = whereiam
								print lines[whereiam-1].rstrip()
								while (n != (whereiam + A)):
									n += 1
									if (n <= len(lines)):
										print lines[n-1].rstrip()
							
									
								
			except:
				print "Problem with the configuration file: %s" % (filename)
				# print "Error: %s" % sys.exc_info()[0]
				continue
			file.close
			if found:
				print "---"
	
		
if __name__ == '__main__':
	main()






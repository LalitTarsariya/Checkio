# check password strong or weak

import re
str=raw_input("Input Password:")
if(re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9]{10,}$',str)):
	return "true"
else
	return "false"

"""if (len(str)<10):
	print "false"
elif not (re.match("^.*[A-Z]+.*$",str)):
	print "false"
elif not(re.match("^.*[a-z]+.*$",str)):
	print "false"
elif not(re.match("^.*[0-9]+.*$",str)):
	print "false"
elif not(re.match("^[a-z0-9A-Z]+$",str)):
	print "false"
else:
	print "true"""
	
	10 // 20
	10 ** 2

a="AAaooo!!!!"

a=a.lower()

ch =" "
for i in a:
	if(i.isalpha() and (ch==" " or a.count(i)>a.count(ch) or (a.count(i)==a.count(ch) and ord(i)<ord(ch)))):
		ch=i
print ch

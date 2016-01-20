# print median of the list

st=raw_input("input :")

n=st.split()

a=[]

for i in n:
	a.append(int(i))
	
a.sort()

l=len(a)

if(l%2==0):
	print (a[l/2-1]+a[l/2])/2.0
else:
	print a[l/2]

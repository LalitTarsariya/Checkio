# remove unique elemr=ent from the array

st= raw_input("please input :")

n=st.split()

i=len(n)-1
while(i>=0):
	if(n.count(n[i])==1):
		n.remove(n[i])		
	i-=1

print n

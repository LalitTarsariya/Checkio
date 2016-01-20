a=["OO.","XOX","XOX"]

tmp=range(0,3)

for i in tmp:
	if(a[i][0]==a[i][1] and a[i][0]==a[i][2]):
		return a[i][0]
for i in tmp:
	if(a[0][i]==a[1][i] and a[0][i]==a[2][i]):
		return a[0][i]
if(a[1][1]==a[2][2] and a[1][1]==a[0][0]):
	return a[0][0]
if(a[0][2]==a[1][1] and a[2][0]==a[1][1]):
	return a[1][1]
return "D"

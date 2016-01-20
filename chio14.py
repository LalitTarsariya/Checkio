def boolean(x, y, str):
	
	if operation=="conjunction" : return x and y
	if operation=="disjunction" : return x or y
	if operation=="implication" : return y or not x
	if operation=="exclusive" : return x ^ y
	if operation=="equivalence" : return x == y

print boolean(1, 1, "exclusive")

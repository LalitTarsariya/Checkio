def safe_pawns(pawns):
	count=0
	for i in pawns:
		prev_position=chr(ord(i[0])+1)+str(int(i[1])-1)
		next_position=chr(ord(i[0])-1)+str(int(i[1])-1)
		if prev_position in pawns or next_position in pawns:
			count+=1
	return count

print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})

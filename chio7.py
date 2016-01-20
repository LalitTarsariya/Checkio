def count_words(text, words):
	text=text.lower()
	n=0
	for i in words:
		if(text.find(i.lower())>-1):
			n+=1
	return n

print count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})

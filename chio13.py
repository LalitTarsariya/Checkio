def check_connection(data,f1,f2):
	a=[i.split("-")[0] for i in data]
	print a

check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2","scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),"super","scout4")

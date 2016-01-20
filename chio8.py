def checkio(words):
    n=0
    for i in words.split():
        if(i.isalpha()):
            n+=1
        else:
            n=0
        if(n>=3):
            return True
    return False
    
print checkio("He is 123 man")

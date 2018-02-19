# readwritetest.py

with open("testfile", "r+") as rf:
    text = rf.read()
    print(text)
    print(text.find("hello"))

    newline = "would you like some ice cream?"

    if text.find("hello") is not -1:
        if(text.find(newline) is -1):
            rf.seek(0,2)
            rf.write(newline + "\n")
            pass
    
rf.close
eggs=9 #global variable

def spam():
    global eggs #declaring that egg is gloabal variable
    eggs=100 #override global eggs variable
    

spam()
print(eggs)
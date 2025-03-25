
print("how many cats do you have?")

try:
    Answer=int(input())
    if Answer>=1:
        print("yippee we both are cat owner")

    elif Answer==0:
        print("you dont own a pet")

except:
    print("please enter a numeric valid whole number")

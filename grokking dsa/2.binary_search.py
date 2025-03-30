


# log _{2}32

# log base 2 of the value 32 ==

# think of it same as how many 2 to the power x = 32

# exponential value is 5

arr=[9,11,62,86,36]


def binary(item,arr):

    arr=sorted(arr)

    print(arr)

    low =0

    high=len(arr)-1

    while low<=high:

        

        mid= (low+high)//2

        guess=arr[mid]


        if guess==item:
            return mid

        elif guess<item:
            #update low
            low=mid+1

        elif guess>item:
            #update high
            high=mid-1
        
        else:
            return None
        

#log n


print("input guess no to find in array")
item=int(input())
no=binary(item,arr)
print(no)


#runtime grows at different speeds
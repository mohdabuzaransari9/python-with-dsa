class YouTube:
    def __init__(self,username,subscribers=0):
        self.subscribers=subscribers
        self.username=username
        

user1=YouTube("arya")

print(user1.username)
print(user1.subscribers)
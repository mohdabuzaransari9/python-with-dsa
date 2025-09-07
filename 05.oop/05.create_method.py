class YouTube:
    def __init__(self,subscribers=0,subscriptions=0):
        self.subscribers=subscribers
        self.subscriptions=subscriptions

    def method(self,user):
        user.subscribers+=1
        self.subscriptions+=1

user1=YouTube()
user2=YouTube()


user1.method(user2)
print(user1.subscribers)
print(user1.subscriptions)
print(user2.subscribers)
print(user2.subscriptions) 
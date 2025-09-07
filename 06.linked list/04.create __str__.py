class Person:
    def __init__(self,user,age):
        
        self.user=user
        self.age=age

    def __str__(self):
        return f"Person {self.user}-->{self.age}"
        # f string classname space object_attributes

        # override the __str__ logic  provided by python by default
new_person=Person("arya",20)

print(new_person)

    
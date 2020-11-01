# class human():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age


# class rohan(human):
#     def __init__(self, name, age,year):
#         super().__init__(name,age)
#         self.year=year

#     def welcome(self):
#         print("hello "+str(self.name) + " "+str(self.age)+" " + str(self.year))



# ron=rohan("rohan",22,2019)
# ron.welcome()


class incr():
    def itr(self):
        self.a=1

    
    def next(self):
        if self.a <=5:
            print(self.a)
            self.a+=1
        else:
            raise StopIteration

zip=incr()
zip.itr()
zip.next()
zip.next()
zip.next()
zip.next()
zip.next()

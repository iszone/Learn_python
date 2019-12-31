# _*_ coding: utf-8 _*_
#!/usr/bin/python

#定义一个类
class TheThing(object):

    #初始化类的number为0
    def __init__(self):
        self.number = 0

    #定义该方法只能由类本身的一个参数既,a.some_function()=some_function(a)
    def some_function(self):
        print "I got called."

    #定义两个参数的方法
    def add_me_up(self, more):
        self.number += more #A += B => A = A + B
        return self.number

#two different things
a = TheThing()
b = TheThing()

a.some_function() #如果传参，则会报错
b.some_function()

print "a.add_me_up(20): %d" % a.add_me_up(20)
print "a.add_me_up(20): %d" % a.add_me_up(20)
print "b.add_me_up(30): %d" % b.add_me_up(30)
print "b.add_me_up(30): %d" % b.add_me_up(30)


print a.number
print b.number




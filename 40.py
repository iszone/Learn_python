# _*_ coding: utf-8 _*_
#!/usr/bin/python

#定义字典
cities = {'sh':'shanghai', 'bj':'beijing', 'gz':'guangzhou'}
cities['sz'] = 'shengzhen'
cities['cd'] = 'chengdu'

#定义查找字典的方法
def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found."

#将方法也保存为一个字典健值,python一切皆是对象
cities['_find'] = find_city

#定义输入值&根据输入查询字典
while True:
    print "state ? (enter to quit)",
    state = raw_input(">")
    #判断是否为空，为空则打断循环
    if not state: break
    #传入字典和input的关键KEY
    city_found = cities['_find'](cities, state)
    #打印出查找后值
    print city_found
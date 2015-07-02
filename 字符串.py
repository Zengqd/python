#coding=utf-8
#基本字符串操作(字符串是不可变的)
web = "http://www.baidu.com"
print web * 2
print web[7:-1]
print "baidu" in web
print len(web)
print max(web)
print min(web)
#字符串格式化
web = "http://www.%s.com"
value = "baidu"
print web % value
print web % "sina"
print "percent is %s%%" % "5"
from math import pi
print "Pi with seven decimals : %.7f" % pi
#模版字符串
from string import Template
s = Template('$a is $a!')
print s.substitute(a='mother')
url = Template('http://$a.$b.$c')
print url.substitute({'a':'www','b':'baidu','c':'com'})
#字符串方法
import string
print string.digits
print string.letters
print string.lowercase
print string.uppercase
print string.printable
print string.punctuation
web = 'www.baidu.com.cn'
print web.find('baidu')
print web.find('ai',3,9)
print '.'.join(['www','baidu','con','cn'])
dirs = '','home','akalo','java'
print dirs
print '/'.join(dirs)
print 'c:'+'\\'.join(dirs)
name = 'I\'m a men'
print name.lower()
print name.title();
print string.capwords(name)
print name.replace('en','an')
print 'www.baidu.com.cn'.split('.')
print 'hh  hah ha  hh'.strip('hh')

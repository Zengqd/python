#coding=utf-8
print "hello world"
name=raw_input("Please input your name:")
print "hello "+name
#print "I'm " + 25是不正确的 因为不可以将字符串和数字相加 应加上反引号 相当于repr()函数
print "I'm " + `25`
print 'Let\'s go!'
print '''in this case,
    you can use this style to format long string,
    is cool ,right ?
    now try it! '''
print r'c:\nowspace'#这是原始字符串 反斜线不会被转义
raw_input("press enter to exit!")

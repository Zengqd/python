#coding=utf-8
#通过名字引用值的数据类型称为映射（mapping），字典是唯一内建的映射类型
phonebook = {'dur':'185xx','doubi':'170xx','zeop':'185xx'}
print phonebook['dur']
print dict([('wangzy','156xx'),('wangj','136xx'),('huangxd','187xx')])
print dict(zhangp='185xx',shijj='136xx')
print len(phonebook)#返回键值对的数量
del phonebook['zeop']
phonebook['licy']='139XX'
print phonebook
print 'dur' in phonebook
print '==============='
people={
    'dur':{
        'Phone number' : '185xx',
        'QQ' : '707XX'
    },
    'zeop':{
        'Phone number' : '186XX',
        'QQ' : '244XX'
    },
    'doubi':{
        'Phone number' : '170XX',
        'QQ' : '465XX'
    }
}
name=raw_input('Please input your name:')
if name not in people :
    print '%s is not in books' % (name)
else :
    request = raw_input('Phone number(p) or QQ(q)')
    if request == 'p' : key = 'Phone number'
    if request == 'q' : key = 'QQ'
    print '%s\'s %s is %s.' % (name,key,people[name][key])
    

x=10
y=3
z=x/y # 在执行除法运算的时候，将运算的结果赋值给z
print(z,type(z))# 隐式转换，通过运算隐式的转了结果的类型
print('float类型转成int类型:',int(3.14))# float类型转成int类型，只保留整数部分
print('将int转成float类型：',float(10))# 将int转成float类型
print(int('100')+int('200'))# 将str转成int类型
# print(int('18a'))# 将字符串转成int或float时报错的情况
# print(int('3.14'))# 将字符串转成int或float时报错的情况
# print(float('45a.987'))# 将字符串转成int或float时报错的情况
print(ord('杨'))# 杨在unicode中对应的整数值
print(chr(26472))# 26472整数在unicode表中对应的字符是什么
print(ord('王'))# 王在unicode中对应的整数值
print(chr(29579))# 26472整数在unicode表中对应的字符是什么
print('十进制转换成十六进制：',hex(26472))# 进制之间的转换操作，十进制与其他进制之间的转换，转换的结果是字符串类型
print('十进制转换成八进制：',oct(26472))
print('十进制转换成二进制：',bin(26472))

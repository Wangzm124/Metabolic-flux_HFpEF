x=True
print(x)
print(type(x))
print(x+10)# 11--1+10
print(False+10)# 10--0+10
print(bool(18))# 测试整数18的布尔值 True
print(bool(0),bool(0.0))# False
# 总结，非0的整数的布尔值都是True
print(bool('北京欢迎你'))# True
print(bool(''))# False
# 所有非空字符串的布尔值都是True
print(bool(False))# False
print(bool(None))# False
# 布尔值为False的情况
# False 或者是 None
# 数值中的0，包含0，0.0，虚数0
# 空序列包含字符串，空元组，空字典，空列表，空集合
# 自定义对象的实例，该对象的_bool_（）方法返回False或_len_（）方法返回0
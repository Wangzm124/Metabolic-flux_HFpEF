print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('-'*40)
print(8>7 and 6>5)
print(8>7 and 5>6)
print(8<7 and 10/0)# False,10/0并没有运算，当第一个表达式结果为False时，直接得结果，不会计算and右侧的表达式
print('-'*40)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('-'*40)
print(8>7 or 10/0)# True,左侧的表达式结果为True时，or右侧的表达式不执行运算
print('-'*40)
print(not True)# False
print(not False)# True
print(not (8>7))# False

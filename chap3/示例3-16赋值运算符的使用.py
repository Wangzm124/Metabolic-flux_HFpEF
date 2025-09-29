x=20# 直接赋值，将20赋值给左侧的变量x
y=10
x=x+y# 将x+y的值重新赋给x
print(x)# x的值是30
x+=y# 40 相当于x=x+y
x-=y # 相当于x=x-y
print(x)
x*=y
print(x)
x/=y
print(x)# 30.0 发生了类型转换，x的数据类型为float类型
x%=2# 相当于x=x%2
print(x)# 0.0
z=3
y//z
print(y)# 3
y**2# 相当于y=y**2
print(y)# 9
# python支持链式赋值
a=b=c=100# 相当于a=100 b=100 c=100
print(a,b,c)
# python支持系列解包赋值
a,b=10,20# 相当于执行了a=10 b=20
print(a,b)
a,b=b,a# 将b的值赋给a，将a的值赋给b

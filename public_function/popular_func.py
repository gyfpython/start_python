# 计算操作
print(divmod(10, 3))
print(abs(-1)) # 绝对值
print(pow(2, 3)) # x 的 y 次幂
print(round(2.5555, 3)) # -修改精度，如果没有，默认取0位
# 其他函数
print(callable(max)) # --返回是否可调用返回true或false
print(range(10))
# 类型转换函数
# type()
# 
# int()
# 
# long()
# 
# float()
# 
# complex()--转换成负数
# 
print(hex(100)) #--转换成十六进制
# 
print(oct(100))# oct()--转换成八进制
# 
print(chr(100))# chr()--参数0-252，返回当前的ASCII码
# 
print(ord('d'))# ord()--参数ASCII码，返回对应的十进制整数
# 序列函数
# reduce()--对每个元素先前两个执行函数，然后结果和后一个元素进行函数操作，如阶乘，阶加
#
# map--对多个列表进行压缩组合成一个新列表，但是如果多个列表的元素个数不同，结果是将所有的元素取出来，缺少的以None代替。如果是None，直接组合，如果是函数，可以按函数进行组合
#
# zip()---对多个列表进行压缩组合成一个新列表，但是如果多个列表的元素个数不同，组合的结果按最少元素的进行组合
#
# filter()--筛选返回为true返回成序列

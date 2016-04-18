# coding=utf-8

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
#[n for n in mylist if n > 0]  最简单的过滤序列元素的方法就是使用列表推导
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])


#

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val) # 判断 是否是 number
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
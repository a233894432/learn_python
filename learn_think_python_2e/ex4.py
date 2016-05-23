fruit = 'banana'
print(len(fruit))

prefixes = 'JKLMNOPQ'
suffix = 'ack'

# for letter in prefixes:
#     print(letter + suffix)


fruit = 'banana'

print(fruit[3:])  # 取后3个item
print(fruit[:3])  # 取前3的item

print(fruit[:])  # 取全值

# 计算字母a在字符串中出现的次数：
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)

print(word.upper())


# 下面的函数打印所有既出现在 word1 中，也出现在 word2 中的字母：

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

print("-"*100)
in_both('apples', 'oranges')
print("-"*100)




# 术语表
# 对象（object）：
# 变量可以引用的东西。现在你将对象和值等价使用。
# 序列（sequence）：
# 一个有序的值的集合，每个值通过一个整数索引标识。
# 元素（item）：
# 序列中的一个值。
# 索引（index）：
# 用来选择序列中元素（如字符串中的字符）的一个整数值。 在Python中，索引从0开始。
# 切片（slice）：
# 以索引范围指定的字符串片段。
# 空字符串（empty string）：
# 一个没有字符的字符串，长度为0，用两个引号表示。
# 不可变 （immutable）：
# 元素不能被改变的序列的性质。
# 遍历（traversal）：
# 对一个序列的所有元素进行迭代， 对每一元素执行类似操作。
# 搜索（search）：
# 一种遍历模式，当找到搜索目标时就停止。
# 计数器（counter）：
# 用来计数的变量，通常初始化为0，并以此递增。
# 方法调用(invocation):
# 执行一个方法的声明.
# 可选参数（optional argument）
# 一个函数或者一个方法中不必要指定的参数。
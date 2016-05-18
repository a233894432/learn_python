import time

print(time.time())


# 递归
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)


def is_divisible(x, y):
    """
    计算整除
    :param x:
    :param y:
    :return: True or False
    """
    if x % y == 0:
        return True
    else:
        return False


# 另一种写法
# def is_divisible(x, y):
#     return x % y == 0



is_divisible(12, 3)


# 再看看递归

def factorial(n):
    """
    0!=1n!=n(n−1)!
0!=1n!=n(n−1)!
该定义指出 0 的阶乘是 1 ，任何其他值 nn 的阶乘是 nn 乘以 n−1n−1 的阶乘。

所以 3!3! 的阶乘是 3 乘以 2!2! ，它又是 2 乘以 1!1! ， 后者又是 1 乘以 0!0! 。 放到一起， 3!3! 等于 3 乘以 2 乘以 1 乘以 1 ，结果是 6 。
    :param n:
    :return:
    """
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))



# 术语表
# 临时变量（temporary variable）：
# 一个在复杂计算中用于存储过度值的变量。
# 死代码（dead code）：
# 程序中永远无法执行的那部分代码，通常是因为其出现在一个返回语句之后。
# 增量式开发（incremental development）：
# 一种程序开发计划，目的是通过一次增加及测试少量代码的方式，来避免长时间的调试。
# 脚手架代码（scaffolding）：
# 程序开发中使用的代码，但并不是最终版本的一部分。
# 监护人（guardian）：
# 一种编程模式，使用条件语句来检查并处理可能引发错误的情形。
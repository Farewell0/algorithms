# 递归
'''
递归调用栈  调用另一个函数时，当前函数暂停并处于未完成状态
'''
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


'''
使用分而治之(D&C)的策略
使用D&C解决问题的两个步骤：
（1）找出基线条件，这种条件必须尽可能简单
（2）不断将问题分解，直到符合基线条件
'''

# 递归求列表所有元素的和
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])

# 递归求列表元素个数
def length(list):
    if list == []:
        return 0
    else:
        return 1 + length(list[1:])

#  找出列表中最大的数字
def max_in_list(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    else:
        return list[0] if list[0] > max_in_list(list[1:]) else max_in_list(list[1:])

if __name__ == "__main__":
    list = [2, 115, 8, 90]
    print(sum(list))
    print(length(list))
    print(max_in_list(list))
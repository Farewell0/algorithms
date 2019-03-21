# 二分查找算法

def binary_search(list, item):
    high = len(list) - 1
    low = 0
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if item > guess:
            low = mid + 1
        elif item < guess:
            high = mid - 1
        else:
            return mid
    return None

def main():
    list = [1, 3, 6, 24, 33, 43, 46, 78, 99]
    find = 99
    result = binary_search(list, find)
    print(result)

if __name__ == "__main__":
    main()

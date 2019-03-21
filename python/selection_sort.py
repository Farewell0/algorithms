# 选择排序算法

def find_smallest(arr, sort):
    smallest = arr[0]
    smallest_index = 0;
    for i in range(1, len(arr)):
        if sort == 'Asce':
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        elif sort == 'Desc':
            if arr[i] > smallest:
                smallest = arr[i]
                smallest_index = i
    return smallest_index

def selection_sort(arr, sort):
    if sort == 'Asce' or sort == 'Desc':
        new_arr = []
        length = len(arr)
        for i in range(length):
            smallest_index = find_smallest(arr, sort)
            new_arr.append(arr.pop(smallest_index))
        return new_arr
    else:
        return None

def main():
    print(selection_sort([3, 1, 6, 23, 2, 12, 34], 'Asce'))

if __name__ == "__main__":
    main()
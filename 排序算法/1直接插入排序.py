# 直接插入排序
# 把待排序的记录按其关键码值的大小逐个插入到一个已经排好序的有序序列中，直到所有的记录插入完为止，得到一个新的有序序列。
def straight_insertion_sort(nums: list)->list:
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = temp
    return nums


def main():
    nums = [1, 4, 2, 6, 3, 8, 5, 7]
    nums = straight_insertion_sort(nums)
    print(str(nums))


if __name__ == '__main__':
    main()
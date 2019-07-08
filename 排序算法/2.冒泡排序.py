def bubble_Sort(nums: list):
    for i in range(len(nums) - 1):          # 循环次数
        for j in range(len(nums) - i - 1):  # 每次循环将最大值放在列表尾
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def main():
    nums = [1, 4, 2, 6, 3, 8, 5, 7]
    bubble_Sort(nums)
    print(str(nums))


if __name__ == '__main__':
    main()
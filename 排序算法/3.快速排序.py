def quick_sort(nums: list):
    if len(nums) >= 2:
        mid = nums[len(nums)//2]            # 选取中间为基准值
        left_list, right_list = [], []
        nums.remove(mid)
        for num in nums:
            if num < mid:
                left_list.append(num)       # left_list存储比mid小的列表
            else:
                right_list.append(num)      # right_list存储比mid大的列表
        return quick_sort(left_list) + [mid] + quick_sort(right_list)
    else:
        return nums


def main():
    nums = [1, 4, 2, 6, 3, 8, 5, 7]
    nums = quick_sort(nums)
    print(str(nums))


if __name__ == '__main__':
    main()
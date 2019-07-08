def merge_sort(nums: list):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


def main():
    nums = [1, 4, 2, 6, 3, 8, 5, 7]
    nums = merge_sort(nums)
    print(str(nums))


if __name__ == '__main__':
    main()
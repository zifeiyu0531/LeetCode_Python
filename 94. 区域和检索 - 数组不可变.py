# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

# 示例：

# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:

# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = [0]
        for index in range(len(nums)):
            self.sums.append(self.sums[index] + nums[index])


    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
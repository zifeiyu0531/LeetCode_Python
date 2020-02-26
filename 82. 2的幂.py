# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

# 示例 1:

# 输入: 1
# 输出: true
# 解释: 20 = 1
# 示例 2:

# 输入: 16
# 输出: true
# 解释: 24 = 16
# 示例 3:

# 输入: 218
# 输出: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 0:
            if n == 1 or n == 2:
                return True
            if n % 2 == 1:
                return False
            n /= 2
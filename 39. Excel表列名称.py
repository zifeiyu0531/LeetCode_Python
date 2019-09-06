# 给定一个正整数，返回它在 Excel 表中相对应的列名称。

# 例如，

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
# 示例 1:

# 输入: 1
# 输出: "A"
# 示例 2:

# 输入: 28
# 输出: "AB"
# 示例 3:

# 输入: 701
# 输出: "ZY"

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        target = ''
        while n > 26:
            temp = n % 26
            target = array[temp-1] + target
            if temp == 0:
                n = (n-26) // 26
            else:
                n = (n-temp) // 26
        return array[n-1] + target
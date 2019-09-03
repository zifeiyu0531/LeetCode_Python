# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        array = []  
        for i in range(numRows):
            array.append([])
            temp = []
            temp.append(1)
            if i >= 2:
                for j in range(1, i):
                    temp.append(array[i-1][j-1] + array[i-1][j])
            if i > 0:
                temp.append(1)
            array[i].extend(temp)
        return array
    
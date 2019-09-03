# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:

# 输入: 3
# 输出: [1,3,3,1]
# 进阶：

# 你可以优化你的算法到 O(k) 空间复杂度吗？

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        array = []
        array.append([])
        for i in range(rowIndex+1):
            temp = []
            temp.append(1)
            if i >= 2:
                for j in range(1, i):
                    temp.append(array[j-1] + array[j])
            if i > 0:
                temp.append(1)
            array = temp
        return array 
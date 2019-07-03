# 编写一个函数来查找字符串数组中的最长公共前缀。
# 如果不存在公共前缀，返回空字符串 ""。
# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        target = ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs)-1):
            j = 1
            while(strs[i][0:j] == strs[i+1][0:j] and j <= len(strs[i]) and j <= len(strs[i+1]) and strs[i][0:j] != ""):
                j = j + 1
            if (target == "" and i == 0) or j <= len(target):
                target = strs[i+1][0:j-1]
        return target
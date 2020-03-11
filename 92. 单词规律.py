# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

# 示例1:

# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:

# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 示例 3:

# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 示例 4:

# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split(" ")
        str_dict = {}
        search = []
        if len(str_list) != len(pattern):
            return False
        for p, st in zip(pattern, str_list):
            if p not in str_dict.keys():
                if st not in search:
                    str_dict[p] = st
                    search.append(st)
                else:
                    return False
            else:
                if str_dict[p] != st:
                    return False
        return True
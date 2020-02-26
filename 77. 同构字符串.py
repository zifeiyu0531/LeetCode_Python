# 给定两个字符串 s 和 t，判断它们是否是同构的。

# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

# 示例 1:

# 输入: s = "egg", t = "add"
# 输出: true
# 示例 2:

# 输入: s = "foo", t = "bar"
# 输出: false
# 示例 3:

# 输入: s = "paper", t = "title"
# 输出: true
# 说明:
# 你可以假设 s 和 t 具有相同的长度。

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch_dict1 = {}
        ch_dict2 = {}
        index1 = index2 = 1
        str1 = str2 = ""
        for ch1, ch2 in zip(s, t):
            if ch1 not in ch_dict1.keys():
                ch_dict1[ch1] = str(index1)
                index1 += 1
            if ch2 not in ch_dict2.keys():
                ch_dict2[ch2] = str(index2)
                index2 += 1
            str1 += ch_dict1[ch1]
            str2 += ch_dict2[ch2]
        if str1 == str2:
            return True
        return False
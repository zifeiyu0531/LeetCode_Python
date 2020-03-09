# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。

# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_dict = {}
        for w in s:
            if w not in word_dict.keys():
                word_dict[w] = 1
            else:
                word_dict[w] += 1
        for w in t:
            if w not in word_dict.keys():
                return False
            else:
                word_dict[w] -= 1
                if word_dict[w] == 0:
                    del word_dict[w]
        if len(word_dict) == 0:
            return True
        return False
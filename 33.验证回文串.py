# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:

# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:

# 输入: "race a car"
# 输出: false

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i < j:
            while i < j and self.isAlpha_digit(s[i]) == False:
                i += 1
            while i < j and self.isAlpha_digit(s[j]) == False:
                j -= 1
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        return True
    
    def isAlpha_digit(self, ch):
        return (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9')
    
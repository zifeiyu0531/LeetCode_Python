# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 示例 1:
# 输入: 123
# 输出: 321
# 示例 2:
# 输入: -123
# 输出: -321
# 示例 3:
# 输入: 120
# 输出: 21
# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
class Solution:
    def reverse(self, x: int) -> int:
        is_positive = True
        string = str(x)
        num_list = list(string)
        if num_list[0] == '-':
            num_list = num_list[1:len(num_list)]
            is_positive = False
        num_list.reverse()
        string = "".join(num_list)
        if not is_positive:
            string = '-' + string
        target = int(string)
        if target < -2**31 or target > 2**31 - 1:
            return 0
        return target
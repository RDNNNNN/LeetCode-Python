# 3110. Score of a String (字串分數)

# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# 給定一個字串 s，字串的分數定義為相鄰字元的 ASCII 值之間的絕對差之和。
# Return the score of s.
# 回傳 s 的分數


# Example 1:
# Input: s = "hello"

# Output: 13
# Explanation (解釋):
# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
# Example 2:
# Input: s = "zaz"

# Output: 50
# Explanation (解釋):
# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
# Constraints (限制):
# 2 <= s.length <= 100
# s consists only of lowercase English letters.
# s 僅由小寫字母組成
# class Solution:
#     def scoreOfString(self, s: str) -> int:


# Code
class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1]))
        return total


# 迴圈寫法
# ord(char) 將字元轉成對應的 ASCII
# 迴圈會遍歷給個相鄰字元
# 計算相鄰字元的 ASCII 差的絕對值，並將結果累加到 total 並回傳


# sum()
# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))

# sum() 將生成式的每個元素累加
# 生成式使用 for 迴圈生成每個相鄰字元的 ASCII 絕對差


# zip()
# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         return sum(abs(ord(a) - ord(b)) for a, b in zip(s, s[1:]))

# zip() 將兩個序列按照索引配對
# s 為原字串，s[1:] 為去掉第一個字元的字串
# 生成式將配對的相鄰字元計算 ASCII 絕對差並累加


# itertools.pairwise (Python 3.10)
# from itertools import pairwise

# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))

# pairwisw() 將序列中的相鄰元素自動配對
# 只支援 Python 3.10 以上的版本


# map()
# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         differences = map(lambda pair: abs(ord(pair[0]) - ord(pair[1])), zip(s, s[1:]))
#         return sum(differences)

# map() 將每個配對的相鄰字元應用 lambda 函式
# zip() 將字串的每個相鄰字元配對


# 遞迴
# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         if len(s) == 1:
#             return 0
#         return abs(ord(s[0]) - ord(s[1])) + self.scoreOfString(s[1:])

# 遞迴呼叫自身來處理剩餘的字串
# 每次遞迴計算第一個相鄰字元的 ASCII 絕對差，對剩餘的字串重複過程。


# Numpy
# import numpy as np

# class Solution:
#     def scoreOfString(self, s: str) -> int:
#         ascii_vals = np.array(list(map(ord, s)))
#         return np.sum(np.abs(np.diff(ascii_vals)))

# map(ord, s) 將字串轉成 ASCII 值列表
# np.array() 將列表轉成 Numpy 陣列
# np.diff() 計算陣列中相鄰元素的差
# np.aps() 取絕對值
# np.sum() 計算總和

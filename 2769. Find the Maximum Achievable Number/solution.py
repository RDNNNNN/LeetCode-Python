## 2769. Find the Maximum Achievable Number

# Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:
# 給兩個整數 `num` 跟 `t`，如果數字 `x` 能在最多 `t` 次運算後為 `num`，則該數字是可實現的。
# Increase or decrease `x` by `1`, and simultaneously increase or decrease `num` by `1`.
# Return the maximum possible value of `x`.
# 將 `x` 增加或減少 1 ，同時將 `num` 增加或減少 `1`，回傳 `x` 可能的最大值

### 懶人包

# 1. 每次操作可以增加或是減少 `x` 和 `num` 各 `1`
# 2. 每次操作讓 `x` 和 `num` 差異減少 `2`

### 範例

### Example 1:

# Input: num = 4, t = 1

# Output: 6

### Explanation 解釋:

# Apply the following operation once to make the maximum achievable number equal to `num`:
# 使用以下操作一次，使最大的可實現數字為 `num`
# Decrease the maximum achievable number by `1`, and increase num by `1`.
# 將最大的可實現數量減少 `1`，並將數量增加 `1`

### Example 2:

# Input: num = 3, t = 2

# Output: 7

### Explanation 解釋:

# Apply the following operation twice to make the maximum achievable number equal to `num`:
# 使用以下操作兩次，使最大的可實現數字為 `num`
# Decrease the maximum achievable number by `1`, and increase `num` by `1``.
# 將最大的可實現數量減少 `1`，並將數量增加 `1`

### Constraints 限制:

# `1 <= num, t <= 50`

### Code


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


# class Solution:
#     def theMaximumAchievableX(self, num: int, t: int) -> int:
#         x = num
#         for n = range(t):
#             x += 2
#         return x

# 模擬操作步驟
# 每次操作讓 x 增加 2


# class Solution:
#     def theMaximumAchievableX(self, num: int, t: int) -> int:
#         return (num + t) + t

# 拆解兩步
# 先讓 x 增加 t，再讓 num 增加 t


# class Solution:
#     def theMaximumAchievableX(self, num: int, t: int) -> int:
#         return num + (t << 1)

# 位運算寫法
# t << 1 將 t 左移 1 位，相當於 T * 2
# 運算會比普通乘法快一些，但在 Python 差別不大。


# class Solution:
#     def theMaximumAchievableX(self, num: int, t: int) -> int:
#         if t == 0:
#             return num
#         return self.theMaximumAchievableX(num + 2, t - 1)

# 遞迴寫法
# 如果 t 等於 0 ，返回 num
# 每次遞迴讓 x 增加 2，並減少 t。


# class Solution:
#     def theMaximumAchievableX(self, num: int, t: int) -> int:
#         x = num
#         def generator():
#             nonlocal x
#             for _ in range(t):
#                 x += 2
#                 yield x
#         return list(generator())[-1]

# 生成器 (Generator) 寫法
# 宣告 x 是外層函式有效範圍的變數，允許在產生器中修改它
# 執行 t 次迴圈，每次操作都將 x 增加 2
# yiled x 為每次計算完畢後，將目前的 x 值產生出來，供請求者使用
# list(generator()) 將產生器的結果轉換成列表
# [-1] 取出列表中的最後一個元素，也就是 x 增加到最大後的值

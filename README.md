## 3110. Score of a String 字串分數

You are given a string `s`.

The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

給定一個字串 `s`，字串的分數定義為相鄰字元的 ASCII 值之間的絕對差之和。

Return the score of `s`.

回傳 `s` 的分數

---

### 範例

### Example 1:

```py
Input: s = "hello"

Output: 13
```

### Explanation 解釋:

```py
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111.
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
```

### Example 2:

```py
Input: s = "zaz"

Output: 50
```

### Explanation 解釋:

```py
The ASCII values of the characters in s are: 'z' = 122, 'a' = 97.
So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
```

### Constraints 限制:

`2 <= s.length <= 100`

`s` consists only of lowercase English letters.

`s` 僅由小寫字母組成

```py
class Solution:
    def scoreOfString(self, s: str) -> int:
```

---

### Code

```py
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


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))

# sum() 寫法
# sum() 將生成式的每個元素累加
# 生成式使用 for 迴圈生成每個相鄰字元的 ASCII 絕對差


class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in zip(s, s[1:]))

# zip() 寫法
# zip() 將兩個序列按照索引配對
# s 為原字串，s[1:] 為去掉第一個字元的字串
# 生成式將配對的相鄰字元計算 ASCII 絕對差並累加


from itertools import pairwise

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a) - ord(b)) for a, b in pairwise(s))

# itertools.pairwise (Python 3.10)
# pairwisw() 將序列中的相鄰元素自動配對
# 只支援 Python 3.10 以上的版本


class Solution:
    def scoreOfString(self, s: str) -> int:
        differences = map(lambda pair: abs(ord(pair[0]) - ord(pair[1])), zip(s, s[1:]))
        return sum(differences)

# map() 寫法
# map() 將每個配對的相鄰字元應用 lambda 函式
# zip() 將字串的每個相鄰字元配對


class Solution:
    def scoreOfString(self, s: str) -> int:
        if len(s) == 1:
            return 0
        return abs(ord(s[0]) - ord(s[1])) + self.scoreOfString(s[1:])

# 遞迴寫法
# 遞迴呼叫自身來處理剩餘的字串
# 每次遞迴計算第一個相鄰字元的 ASCII 絕對差，對剩餘的字串重複過程。


import numpy as np

class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii_vals = np.array(list(map(ord, s)))
        return np.sum(np.abs(np.diff(ascii_vals)))

# Numpy 寫法
# map(ord, s) 將字串轉成 ASCII 值列表
# np.array() 將列表轉成 Numpy 陣列
# np.diff() 計算陣列中相鄰元素的差
# np.aps() 取絕對值
# np.sum() 計算總和
```

## 2769. Find the Maximum Achievable Number

Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:

給兩個整數 `num` 跟 `t`，如果數字 `x` 能在最多 `t` 次運算後為 `num`，則該數字是可實現的。

Increase or decrease `x` by `1`, and simultaneously increase or decrease `num` by `1`.

Return the maximum possible value of `x`.

將 `x` 增加或減少 1 ，同時將 `num` 增加或減少 1，回傳 `x` 可能的最大值

### 懶人包

1. 每次操作可以增加或是減少 `x` 和 `num` 各 `1`
2. 每次操作讓 `x` 和 `num` 差異減少 `2`

---

### Example 1:

```py
Input: num = 4, t = 1

Output: 6
```

### Explanation (解釋):

Apply the following operation once to make the maximum achievable number equal to `num`:

使用以下操作一次，使最大的可實現數字為 `num`

Decrease the maximum achievable number by `1`, and increase num by `1`.

將最大的可實現數量減少 `1`，並將數量增加 `1`

### Example 2:

```py
Input: num = 3, t = 2

Output: 7
```

### Explanation (解釋):

Apply the following operation twice to make the maximum achievable number equal to `num`:

使用以下操作兩次，使最大的可實現數字為 `num`

Decrease the maximum achievable number by `1`, and increase `num` by `1`.

將最大的可實現數量減少 `1`，並將數量增加 `1`

### Constraints (限制):

`1 <= num, t <= 50`

---

### Code

```py
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x = num
        for n = range(t):
            x += 2
        return x

# 模擬操作步驟
# 每次操作讓 x 增加 2


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return (num + t) + t

# 拆解兩步
# 先讓 x 增加 t，再讓 num 增加 t


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t << 1)

# 位運算寫法
# t << 1 將 t 左移 1 位，相當於 T * 2
# 運算會比普通乘法快一些，但在 Python 差別不大。


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        if t == 0:
            return num
        return self.theMaximumAchievableX(num + 2, t - 1)

# 遞迴寫法
# 如果 t 等於 0 ，返回 num
# 每次遞迴讓 x 增加 2，並減少 t。


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x = num
        def generator():
            nonlocal x
            for _ in range(t):
                x += 2
                yield x
        return list(generator())[-1]

# 生成器 (Generator) 寫法
# 宣告 x 是外層函式有效範圍的變數，允許在產生器中修改它
# 執行 t 次迴圈，每次操作都將 x 增加 2
# yiled x 為每次計算完畢後，將目前的 x 值產生出來，供請求者使用
# list(generator()) 將產生器的結果轉換成列表
# [-1] 取出列表中的最後一個元素，也就是 x 增加到最大後的值
```

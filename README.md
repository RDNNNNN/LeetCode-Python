## 1920. Build Array from Permutation 根據排列建立陣列

Given a zero-based permutation `nums` (0-indexed), build an array `ans` of the same length where `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length` and `return` it.

給定一個從 `0` 開始的排列 `nums` (從 `0` 開始索引)，建立一個相同長度的陣列 `ans`，每個 `0 <= i < nums.length`，`ans[i] = nums[nums[i]]` 並返回它

A zero-based permutation `nums` is an array of distinct integers from `0` to `nums.length - 1 (inclusive)`.

從 `0` 開始的排列 `nums` 是從 `0` 到 `nums.length -1` 的不同整數陣列

---

### Example 1 範例:

```py 
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
```
    
### Example 2 範例:

```py 
Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
```

---

### Constraints 限制:

```py
1 <= nums.length <= 1000

0 <= nums[i] < nums.length
```

The elements in `nums` are distinct.

`nums` 中的元素是不同的

### Follow-up 額外要求: 

Can you solve it without using an extra space (i.e., O(1) memory)? 

你能在不使用額外空間（即O(1)記憶體）的情況下解決這個問題嗎？

### 額外空間:

需要創建一個新的列表來存放結果，而且會隨著資料大小而增長，那就表示使用了 `O(n)` 的額外空間

只使用固定大小的變數，那麼就是說只有 `O(1)` 的複雜度

O 為 Order 的意思

---

### Code

```py 
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
    
# 使用額外空間，即 O(n)
# 取 nums[i] 作為索引，再去 nums[nums=[i]] 取得值並存入新串列中


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            # nums[nums[i]] % n 可以取出原始的 nums[nums[i]] 值
            nums[i] += (nums[nums[i]] % n) * n
        
        # 將新值提取出來
        for i in range(n):
            nums[i] //= n
        
        return nums
    
# 不使用額外空間，即 O(1)
```

## 1929. Concatenation of Array 陣列連接

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed).

給定一個長度為 `n` 的整數陣列，你要建立一個長度為 `2n` 的陣列 `ans`，其中 `ans[i] == nums[i]` 和 `ans[i + n] == nums[i]`，表示 `0 <= i < n` (從 0 開始索引)

Specifically, `ans` is the concatenation of two `nums` arrays.

具體來說，`ans` 是兩個陣列的連接

Return the array `ans`.

回傳陣列 `ans`

### 懶人包

給定一個整數陣列 `nums`，長度為 `n`

建立一個陣列 `ans`，長度為 `2n`

`ans` 的前 `n` 的元素等於 `nums` 的所有元素，後 `n` 個元素也等於 `nums`

最後回傳 `ans` 陣列

---

### Example 1 範例:

```py
Input: nums = [1, 2, 1]

Output: [1, 2, 1, 1, 2, 1]
```

### Explanation 解釋:

The array ans is formed as follows:

陣列的結構如下

```py
- ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]

- ans = [1, 2, 1, 1, 2, 1]
```

### Example 2 範例:

```py
Input: nums = [1, 3, 2, 1]

Output: [1, 3, 2, 1, 1, 3, 2, 1]
```

### Explanation 解釋:

The array ans is formed as follows:

陣列的結構如下

```py
- ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]

- ans = [1, 3, 2, 1, 1, 3, 2, 1]
```

### Constraints 限制:

```py
n == nums.length

1 <= n <= 1000

1 <= nums[i] <= 1000
```

---

### Code

```py
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)
        return result

# append() 寫法
# 建立一個空的串列 result，使用兩個迴圈將 nums 元素加入 result 兩次
# 每次 append() 操作都是 O(1)，但需要執行 2n 次
# 直觀但效率較低


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)
        for i in range(n):
            result[i] = nums[i]
            result[i + n] = nums[i]
        return result

# 建立一個長度為 2n 的空串列 result (只包含 0)
# 用迴圈將 nums[i] 加入對應的兩個位置 i 和 i + n


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums

# extend() 寫法
# extend() 會直接修改原本的 nums 串列，將 nums 擴充 2 倍
# 有效率但會影響原本的串列


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

# nums + nums 會串接兩個 nums 串列，產生新的 list
# 直觀但需要額外的記憶體，因為創建了一個新的 list


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

# nums * 2 會複製 nums 兩次並產生新的 list，效果與 nums + nums 相同
# 直觀但需要額外的記憶體，因為創建了新的 list
```

## 2011. Final Value of Variable After Performing Operations

There is a programming language with only four operations and one variable `X`:

有一種程式語言只有四個操作和一個變數`X`：

`++X` and `X++` increments the value of the variable `X` by `1`.

++X and X++ 將變數 X 的值增加 `1`

`--X` and `X--` decrements the value of the variable `X` by `1`.

--X and X-- 將變數 X 的值減少 `1`

Initially, the value of `X` is `0`.

最初，X 的值為 `0`

Given an array of strings `operations` containing a list of operations, return the final value of `X` after performing all the operations.

給定一個包含操作清單的字串操作數組，執行所有操作後傳回 `X` 的最終值

---

### Example 1 範例:

```py 
Input: operations = ["--X","X++","X++"]

Output: 1
```

### Explanation 解釋: 

The operations are performed as follows:

操作如下

Initially, `X = 0`.

最初 `X = 0`

`--X`: `X` is decremented by `1`, `X =  0 - 1 = -1`.

`--X`: `X` 減 `1`， `X = 0 - 1 = -1`

`X++`: `X` is incremented by `1`, `X = -1 + 1 =  0`.

`X++`: `X` 加 `1`，`X = -1 + 1 = 0`

`X++`: `X` is incremented by `1`, `X =  0 + 1 =  1`.

`X++`: `X` 加 `1`，`X = 0 + 1 = 1`

### Example 2 範例:

```py 
Input: operations = ["++X","++X","X++"]

Output: 3
```

### Explanation 解釋: 

The operations are performed as follows:

操作如下

Initially, `X = 0`.

最初 `X = 0` 

`++X`: `X` is incremented by `1`, `X = 0 + 1 = 1`.

`++X`：`X` 加 `1`，`X = 0 + 1 = 1`

`++X`: `X` is incremented by `1`, `X = 1 + 1 = 2`.

`++X`：`X` 增加 `1`，`X = 1 + 1 = 2`

`X++`: `X` is incremented by `1`, `X = 2 + 1 = 3`.

`X++`：`X` 增加 `1`，`X = 2 + 1 = 3`


### Example 3 範例:

```py 
Input: operations = ["X++","++X","--X","X--"]

Output: 0
```

### Explanation 解釋: 

The operations are performed as follows:

操作如下

Initially, `X = 0`.

最初 `X = 0`

`X++`: `X` is incremented by `1`, `X = 0 + 1 = 1`.

`X++`：X增加 `1`，`X = 0 + 1 = 1`

`++X`: `X` is incremented by `1`, `X = 1 + 1 = 2`.

`++X`：`X` 增加 `1`，`X = 1 + 1 = 2`

`--X`: `X` is decremented by `1`, `X = 2 - 1 = 1`.

`--X`：`X` 減 `1`，`X = 2 - 1 = 1`

`X--`: `X` is decremented by `1`, `X = 1 - 1 = 0`.

`X--`：`X` 減 `1`，`X = 1 - 1 = 0`

### Constraints 限制:

```py
1 <= operations.length <= 100
operations[i] will be either "++X", "X++", "--X", or "X--"
```

---

### Code

```py 
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for i in operations:
            if i == "++X" or i == "X++":
                result += 1       
            elif i == "--X" or i == "X--":
                result -= 1
        return  result
```

## 2469. Convert the Temperature 轉換溫度

You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

您將獲得一個四捨五入到小數點後兩位攝氏度的非負浮點數，表示以攝氏度為單位的溫度

You should convert Celsius into Kelvin and Fahrenheit and return it as an array `ans = [kelvin, fahrenheit]`.

您應該將攝氏度轉換為開氏溫度和華氏溫度，並將其作為陣列傳回 `ans = [kelvin, fahrenheit]`

Return the array ans. 

傳回陣列 `ans`

Answers within `10 - 5` of the actual answer will be accepted.

與實際答案相差 `10 - 5` 以內的答案將被接受

### Note that 注意: 

```py
Kelvin = Celsius + 273.15

Fahrenheit = Celsius * 1.80 + 32.00
```

---

### Example 1 範例:

```py
Input: celsius = 36.50
Output: [309.65000,97.70000]
Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
```

### Example 2 範例:

```py
Input: celsius = 122.11
Output: [395.26000,251.79800]
Explanation: Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
```

### Constraints 限制:

```py
0 <= celsius <= 1000
```

---

### Code
```py 
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
        return [kelvin, fahrenheit]
    
# 設定開氏跟華氏的溫度
    

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]

# 直接寫在 list 裡面


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result = (celsius + 273.15, celsius * 1.8 + 32)
        return list(result)

# 先用 tuple 再轉成 list


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        conversions = [lambda c: c + 273.15, lambda c: c * 1.8 + 32]
        return [func(celsius) for func in conversions]

# 使用串列推導氏搭配 lambda 表達式
```

## 2769. Find the Maximum Achievable Number 找到可實現的最大數字

Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:

給兩個整數 `num` 跟 `t`，如果數字 `x` 能在最多 `t` 次運算後為 `num`，則該數字是可實現的

Increase or decrease `x` by `1`, and simultaneously increase or decrease `num` by `1`.

Return the maximum possible value of `x`.

將 `x` 增加或減少 `1` ，同時將 `num` 增加或減少 `1`，回傳 `x` 可能的最大值

### 懶人包

1. 每次操作可以增加或是減少 `x` 和 `num` 各 `1`
2. 每次操作讓 `x` 和 `num` 差異減少 `2`

---

### Example 1 範例:

```py
Input: num = 4, t = 1

Output: 6
```

### Explanation 解釋:

Apply the following operation once to make the maximum achievable number equal to `num`:

使用以下操作一次，使最大的可實現數字為 `num`

Decrease the maximum achievable number by `1`, and increase num by `1`.

將最大的可實現數量減少 `1`，並將數量增加 `1`

### Example 2 範例:

```py
Input: num = 3, t = 2

Output: 7
```

### Explanation 解釋:

Apply the following operation twice to make the maximum achievable number equal to `num`:

使用以下操作兩次，使最大的可實現數字為 `num`

Decrease the maximum achievable number by `1`, and increase `num` by `1`.

將最大的可實現數量減少 `1`，並將數量增加 `1`

### Constraints 限制:

```py
1 <= num, t <= 50
```

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
# 運算會比普通乘法快一些，但在 Python 差別不大


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        if t == 0:
            return num
        return self.theMaximumAchievableX(num + 2, t - 1)

# 遞迴寫法
# 如果 t 等於 0 ，返回 num
# 每次遞迴讓 x 增加 2，並減少 t


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

## 2894. Divisible and Non-divisible Sums Difference

You are given positive integers `n` and `m`.

給定正整數 `n` 和 `m`

Define two integers as follows:

定義兩個整數如下：

num1: The sum of all integers in the range `[1, n]` (both inclusive) that are not divisible by `m`.

num1：`[1, n]`（包括兩者）範圍內所有不能被 `m` 整除的整數總和

num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.

num2：`[1, n]`（包括兩者）範圍內所有能被 `m` 整除的整數總和

Return the integer `num1 - num2`.

傳回整數 `num1 - num2`

---

### Example 1 範例:

```py
Input: n = 10, m = 3
Output: 19
```

### Explanation 解釋: In the given example 在給定的範例中:

- Integers in the range `[1, 10]` that are not divisible by `3` are `[1,2,4,5,7,8,10]`, `num1` is the sum of those integers = `37`.

- `[1, 10]`範圍內不能被 `3` 整除的整數是 `[1, 2, 4, 5, 7, 8, 10]`，`num1` 是這些整數的總和 `37`

- Integers in the range `[1, 10]` that are divisible by 3 are `[3,6,9]`, num2 is the sum of those integers = `18`.

- [1, 10]範圍內可以被 `3` 整除的整數是 `[3, 6, 9]`，`num2` 是這些整數的總和 `18`

- We return `37 - 18 = 19` as the answer.

- 我們返回 `37 - 18 = 19` 作為答案

### Example 2 範例:

`Input: n = 5, m = 6`
`Output: 15`

### Explanation 解釋: In the given example 在給定的範例中:

- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], `num1` is the sum of those integers = `15`.

- `[1, 5]` 範圍內不能被 `6` 整除的數字是 `[1, 2, 3, 4, 5]，`num1` 是這些數字的總和 `15`

- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.


- `[1, 5] 範圍內可以被 `6` 整除的整數是 `[]`，`num2` 是這些整數的總和 `0`

- We return `15 - 0 = 15` as the answer.

- 我們返回 `15 - 0 = 15` 作為答案

### Example 3 範例:

```py
Input: n = 5, m = 1

Output: -15
```

### Explanation 解釋: In the given example 在給定的範例中:

- Integers in the range `[1, 5]` that are not divisible by `1` are `[]`, `num1` is the sum of those integers = `0`.

    - 在 `[1, 5]` 範圍內不能被 `1` 整除的數字是 `[]`，`num1` 是這些數字的總和

- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], `num2` is the sum of those integers = `15`.

    - 在 `[1, 5] 範圍能被 `1` 整除的整數是 `[1, 2, 3, 4, 5]`， `num2` 是這些整數的總和

- We return `0 - 15 = -15` as the answer.

    - 我們返回 `0 - 15 = -15` 作為答案
 
### Constraints 限制:

`1 <= n, m <= 1000`

---

### Code
```py 
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        
        for i in range(1, n + 1):
            if i % m == 0:        
                num += i

        for j in range(1, n + 1):
            if j % m != 0:        
                num2 += j
        return num2 - num1
```

## 3110. Score of a String 字串分數

You are given a string `s`.

The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

給定一個字串 `s`，字串的分數定義為相鄰字元的 ASCII 值之間的絕對差之和

Return the score of `s`.

回傳 `s` 的分數

---

### Example 1 範例:

```py
Input: s = "hello"

Output: 13
```

### Explanation 解釋:

```py
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111.
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
```

### Example 2 範例:

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

```py
2 <= s.length <= 100

s consists only of lowercase English letters.

s 僅由小寫字母組成
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
# 每次遞迴計算第一個相鄰字元的 ASCII 絕對差，對剩餘的字串重複過程


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

## 3289. The Two Sneaky Numbers of Digitville

In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to `n - 1`. 

在 Digitville 鎮中，有一個名為 `nums` 的數字串列，其中包含從 `0` 到 `n - 1` 的整數

Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

每個數字應該只在清單中出現一次，但是兩個惡作劇的數字又偷偷出現了一次，使得清單比平常更長

As the town detective, your task is to find these two sneaky numbers. 

身為鎮上的偵探，你的任務是找到這兩個鬼鬼祟祟的數字

Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

傳回一個包含兩個數字（任意順序）的大小為 `2` 的陣列，這樣 Digitville 就可以恢復和平

---

### Example 1 範例:

```py
Input: nums = [0,1,1,0]

Output: [0,1]
```

### Explanation 解釋:

The numbers `0` and `1` each appear twice in the array.

數字 `0` 和 `1` 在陣列中各出現兩次

### Example 2 範例:

```py
Input: nums = [0,3,2,1,3,2]

Output: [2,3]
```

### Explanation 解釋:

The numbers `2` and `3` each appear twice in the array.

數字 `2` 和 `3` 在陣列中各出現兩次

### Example 3 範例:

```py
Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]

Output: [4,5]
```

### Explanation 解釋:

The numbers `4` and `5` each appear twice in the array.

數字 `4` 和 `5` 在陣列中各出現兩次

### Constraints 限制:

```py
2 <= n <= 100

nums.length == n + 2

0 <= nums[i] < n
```

The input is generated such that `nums` contains exactly two repeated elements.

輸入的產生使得 `nums` 剛好包含兩個重複元素

--- 

### Code

```py 
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        set_result = set()
        for i in nums:
            if i not in set_result:
                set_result.add(i)
            else:
                result.append(i)
        return result
```

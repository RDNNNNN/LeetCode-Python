## 2894. Divisible and Non-divisible Sums Difference 可整除和不可整除的金額差異

### 題目

You are given positive integers `n` and `m`.

Define two integers as follows:

num1: The sum of all integers in the range `[1, n]` (both inclusive) that are not divisible by `m`.

num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.

Return the integer `num1 - num2`.

### 中文

給定正整數 `n` 和 `m`

定義兩個整數如下：

num1：`[1, n]`（包括兩者）範圍內所有不能被 `m` 整除的整數總和

num2：`[1, n]`（包括兩者）範圍內所有能被 `m` 整除的整數總和

傳回整數 `num1 - num2`

---

### Example 1 範例:

```py
Input: n = 10, m = 3

Output: 19
```

### Explanation 解釋:

In the given example 在給定的範例中:

Integers in the range `[1, 10]` that are not divisible by `3` are `[1,2,4,5,7,8,10]`, `num1` is the sum of those integers = `37`.

Integers in the range `[1, 10]` that are divisible by 3 are `[3,6,9]`, num2 is the sum of those integers = `18`.

We return `37 - 18 = 19` as the answer.

### 中文

`[1, 10]`範圍內不能被 `3` 整除的整數是 `[1, 2, 4, 5, 7, 8, 10]`，`num1` 是這些整數的總和 `37`

`[1, 10]` 範圍內可以被 `3` 整除的整數是 `[3, 6, 9]` ， `num2` 是這些整數的總和 `18`

我們返回 `37 - 18 = 19` 作為答案

### Example 2 範例:

```py
Input: n = 5, m = 6

Output: 15
```

### Explanation 解釋:

In the given example 在給定範例中:

Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], `num1` is the sum of those integers = `15`.

Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.

We return `15 - 0 = 15` as the answer.

### 中文

`[1, 5]` 範圍內不能被 `6` 整除的數字是 `[1, 2, 3, 4, 5]，`num1`是這些數字的總和`15`

`[1, 5] 範圍內可以被 `6`整除的整數是`[]`，`num2`是這些整數的總和`0`

我們返回 `15 - 0 = 15` 作為答案

### Example 3 範例:

```py
Input: n = 5, m = 1

Output: -15
```

### Explanation 解釋:

In the given example 在給定範例中:

Integers in the range `[1, 5]` that are not divisible by `1` are `[]`, `num1` is the sum of those integers = `0`.

Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], `num2` is the sum of those integers = `15`.

We return `0 - 15 = -15` as the answer.

### 中文

在 `[1, 5]` 範圍內不能被 `1` 整除的數字是 `[]`，`num1` 是這些數字的總和

在 `[1, 5]` 範圍能被 `1` 整除的整數是 `[1, 2, 3, 4, 5]`， `num2` 是這些整數的總和

我們返回 `0 - 15 = -15` 作為答案

### Constraints 限制:

```py
1 <= n, m <= 1000
```

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
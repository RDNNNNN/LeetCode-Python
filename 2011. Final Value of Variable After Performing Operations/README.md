## 2011. Final Value of Variable After Performing Operations 執行操作後的變數最終值

### 題目

There is a programming language with only four operations and one variable `X`:

`++X` and `X++` increments the value of the variable `X` by `1`.

`--X` and `X--` decrements the value of the variable `X` by `1`.

Initially, the value of `X` is `0`.

Given an array of strings `operations` containing a list of operations, return the final value of `X` after performing all the operations.

### 中文

有一種程式語言只有四個操作和一個變數`X`：

`++X` and `X++` 將變數 `X` 的值增加 `1`

`--X` and `X--` 將變數 `X` 的值減少 `1`

最初，`X` 的值為 `0`

給定一個包含操作清單的字串操作陣列，執行所有操作後傳回 `X` 的最終值

---

### Example 1 範例:

```py
Input: operations = ["--X","X++","X++"]

Output: 1
```

### Explanation 解釋:

The operations are performed as follows 操作如下:

Initially 最初, `X = 0`.

```py
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.

--X: X 減少 1， X = 0 - 1 = -1
X++: X 增加 1，X = -1 + 1 = 0
X++: X 增加 1，X = 0 + 1 = 1
```

### Example 2 範例:

```py
Input: operations = ["++X","++X","X++"]

Output: 3
```

### Explanation 解釋:

The operations are performed as follows 操作如下:

Initially 最初, `X = 0`.

```py
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.

++X：X 增加 1，X = 0 + 1 = 1
++X：X 增加 1，X = 1 + 1 = 2
X++：X 增加 1，X = 2 + 1 = 3
```

### Example 3 範例:

```py
Input: operations = ["X++","++X","--X","X--"]

Output: 0
```

### Explanation 解釋:

The operations are performed as follows 操作如下:

Initially 最初, `X = 0`.

```py
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.

X++：X 增加 1，X = 0 + 1 = 1
++X：X 增加 1，X = 1 + 1 = 2
--X：X 減少 1，X = 2 - 1 = 1
X--：X 減少 1，X = 1 - 1 = 0
```

### Constraints 限制:

```py
1 <= operations.length <= 100
```

`operations[i]` will be either `"++X", "X++", "--X", or "X--"`

`operations[i]` 將是 `++X、X++、--X 或 X--`

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
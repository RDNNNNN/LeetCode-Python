## 20. Valid Parentheses 有效括號

### 題目

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

### 中文

給定一個字串 `s`，只包含字元 `'('`、`')'`、`'{'`、`'}'`、`'['` 和 `']'`，判斷輸入字串是否有效

輸入字串有效，條件是：

左括號必須由相同類型的括號閉合

左括號必須以正確的順序閉合

每個右括號都有一個與之對應的相同類型的左括號
 
### Example 1 範例

```py
Input: s = "()"

Output: true
```

### Example 2 範例

```py
Input: s = "()[]{}"

Output: true
```

### Example 3 範例

```py
Input: s = "(]"

Output: false
```

#### Example 4 範例

```py
Input: s = "([])"

Output: true
```

### Example 5 範例

```py
Input: s = "([)]"

Output: false
```

### Constraints 限制

`1 <= s.length <= 104`

`s` consists of parentheses only `'()[]{}'`.

`s` 僅由括號 `'()[]{}'` 組成

### Code 程式碼

```py
class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {')':'(',']':'[','}':'{'}
        stack = []

        for char in s:
            if char in mapp.values():
                stack.append(char)
            elif char in mapp:
                if not stack or mapp[char] != stack.pop():
                    return False
        return not stack
```
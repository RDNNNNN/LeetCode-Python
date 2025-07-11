## 3289. The Two Sneaky Numbers of Digitville 數字小鎮裡的兩個神秘數字

### 題目

In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to `n - 1`.

Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers.

Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

### 中文

在數字小鎮中，有一個名為 `nums` 的數字串列，其中包含從 `0` 到 `n - 1` 的整數

每個數字應該只在清單中出現一次，但是兩個惡作劇的數字又偷偷出現了一次，使得清單比平常更長

身為鎮上的偵探，你的任務是找到這兩個鬼鬼祟祟的數字

傳回一個包含兩個數字（任意順序）的大小為 `2` 的陣列，這樣數字小鎮就可以恢復和平

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
## 1929. Concatenation of Array 陣列連接

### 題目
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

### 中文
# 給定一個長度為 n 的整數陣列，你要建立一個長度為 2n 的陣列 ans，其中 ans[i] == nums[i] 和 ans[i + n] == nums[i]，表示 0 <= i < n (從 0 開始索引)
# 具體來說，ans 是兩個陣列的連接。
# 回傳陣列 ans

### 懶人包
# 給定一個整數陣列 nums，長度為 n
# 建立一個陣列 ans，長度為 2n
# ans 的前 n 的元素等於 nums 的所有元素，後 n 個元素也等於 nums
# 最後回傳 ans 陣列

### Example 1 範例
# Input: nums = [1, 2, 1]
# Output: [1, 2, 1, 1, 2, 1]

### Explanation 解釋
# The array ans is formed as follows 陣列結構如下:
# ans = [nums[0], nums[1], nums[2], nums[0], nums[1], nums[2]]
# ans = [1, 2, 1, 1, 2, 1]

### Example 2 範例
# Input: nums = [1, 3, 2, 1]
# Output: [1, 3, 2, 1, 1, 3, 2, 1]

### Explanation 解釋
# The array ans is formed as follows 陣列結構如下:
# ans = [nums[0], nums[1], nums[2], nums[3], nums[0], nums[1], nums[2], nums[3]]
# ans = [1, 3, 2, 1, 1, 3, 2, 1]

### Constraints 限制
# `n == nums.length`
# `1 <= n <= 1000`
# `1 <= nums[i] <= 1000`

### Code 程式碼
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
# 建立一個空的陣列 result，使用兩個迴圈將 nums 元素加入 result 兩次
# 每次 append() 操作都是 O(1)，但需要執行 2n 次
# 直觀但效率較低


# from typing import List

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         result = [0] * (2 * n)
#         for i in range(n):
#             result[i] = nums[i]
#             result[i + n] = nums[i]
#         return result

# 建立一個長度為 2n 的空陣列 result (只包含 0)
# 用迴圈將 nums[i] 加入對應的兩個位置 i 和 i + n


# from typing import List

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         nums.extend(nums)
#         return nums

# extend() 寫法
# extend() 會直接修改原本的 nums 陣列，將 nums 擴充 2 倍
# 有效率但會影響原本的陣列


# from typing import List

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums

# nums + nums 會串接兩個 nums 陣列，產生新的 list
# 直觀但需要額外的記憶體，因為創建了一個新的 list


# from typing import List

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums * 2

# nums * 2 會複製 nums 兩次並產生新的 list，效果與 nums + nums 相同
# 直觀但需要額外的記憶體，因為創建了新的 list

## 1920. Build Array from Permutation 根據排列建立陣列

### 題目
# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.
# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

### 中文
# 給定一個從 0 開始的排列 nums (從 0 開始索引)，建立一個相同長度的陣列 ans，每個 0 <= i < nums.length，ans[i] = nums[nums[i]] 並返回它
# 從 0 開始的排列 nums 是從 0 到 nums.length - 1 的不同整數陣列

### Example 1 範例
# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]

### Explanation 解釋
# The array ans is built as follows 陣列的結構如下
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]

### Example 2 範例
# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]

### Explanation 解釋
# The array ans is built as follows 陣列的結構如下
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3]

### Constraints 限制
# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.
# nums 中的元素是不同的

### Follow-up 額外要求
# Can you solve it without using an extra space (i.e., O(1) memory)?
# 你能在不使用額外空間（即 O(1) 記憶體）的情況下解決這個問題嗎？

### 額外空間
# 需要創建一個新的列表來存放結果，而且會隨著資料大小而增長，那就表示使用了 O(n) 的額外空間
# 只使用固定大小的變數，那麼就是說只有 O(1) 的複雜度
# O 為 Order 的意思

# Code 程式碼
from Typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


# 使用額外空間，即 O(n)
# 取 nums[i] 作為索引，再去 nums[nums=[i]] 取得值並存入新串列中


# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)

#         for i in range(n):
#             # nums[nums[i]] % n 可以取出原始的 nums[nums[i]] 值
#             nums[i] += (nums[nums[i]] % n) * n

#         # 將新值提取出來
#         for i in range(n):
#             nums[i] //= n

#         return nums

# 不使用額外空間，即 O(1)

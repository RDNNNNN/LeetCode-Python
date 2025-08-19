## 1. Two Sum 兩個和

### 題目
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

### 中文
# 給定一個整數數組 `nums` 和一個整數 `target`，傳回這兩個數字的索引，使得它們總和等於 `target`
# 你可以假設每個輸入只有一個解，而且不能重複使用同一個元素
# 你可以按任意順序返回答案

### Example 1 範例
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

### Explanation 解釋
# Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.
# 因為 `nums[0] + nums[1] == 9`，所以我們回傳 `[0, 1]`

### Example 2 範例
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

### Example 3 範例
# Input: nums = [3,3], target = 6
# Output: [0,1]

### Constraints 限制
# `2 <= nums.length <= 104`
# `-109 <= nums[i] <= 109`
# `-109 <= target <= 109`
# Only one valid answer exists.
# 只有一個有效答案

### Follow-up 後續問題
# Can you come up with an algorithm that is less than `O(n2)` time complexity?
# 你能想出一個時間複雜度小於 `O(n²)` 的演算法嗎？

### Code 程式碼
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

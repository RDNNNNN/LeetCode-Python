### 1920. Build Array from Permutation 根據排列建立陣列 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/1920.%20Build%20Array%20from%20Permutation)

### 題目

Given a zero-based permutation `nums` (0-indexed), build an array `ans` of the same length where `ans[i] = nums[nums[i]]` for each `0 <= i < nums.length` and `return` it.

A zero-based permutation `nums` is an array of distinct integers from `0` to `nums.length - 1 (inclusive)`.

---

### 1929. Concatenation of Array 陣列連接 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/1929.%20Concatenation%20of%20Array)

### 題目

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed).

Specifically, `ans` is the concatenation of two `nums` arrays.

Return the array `ans`.

---

### 2011. Final Value of Variable After Performing Operations 執行操作後的變數最終值 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/2011.%20Final%20Value%20of%20Variable%20After%20Performing%20Operations)

### 題目

There is a programming language with only four operations and one variable `X`:

`++X` and `X++` increments the value of the variable `X` by `1`.

`--X` and `X--` decrements the value of the variable `X` by `1`.

Initially, the value of `X` is `0`.

Given an array of strings `operations` containing a list of operations, return the final value of `X` after performing all the operations.

---

### 2469. Convert the Temperature 轉換溫度 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/2469.%20Convert%20the%20Temperature)

### 題目

You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array `ans = [kelvin, fahrenheit]`.

Return the array ans.

Answers within `10 - 5` of the actual answer will be accepted.

---

### 2769. Find the Maximum Achievable Number 找到可實現的最大數字 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/2769.%20Find%20the%20Maximum%20Achievable%20Number)

### 題目

Given two integers, num and t. A number x is achievable if it can become equal to num after applying the following operation at most t times:

Increase or decrease `x` by `1`, and simultaneously increase or decrease `num` by `1`.

Return the maximum possible value of `x`.

---

### 2894. Divisible and Non-divisible Sums Difference 可整除和不可整除的金額差異 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/2894.%20Divisible%20and%20Non-divisible%20Sums%20Difference)

### 題目

You are given positive integers `n` and `m`.

Define two integers as follows:

num1: The sum of all integers in the range `[1, n]` (both inclusive) that are not divisible by `m`.

num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.

Return the integer `num1 - num2`.

---

### 3110. Score of a String 字串分數 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/3110.%20Score%20of%20a%20String)

### 題目

You are given a string `s`.

The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of `s`.

---

### 3289. The Two Sneaky Numbers of Digitville 數字小鎮裡的兩個神秘數字 [(連結)](https://github.com/RDNNNNN/LeetCode-Python/tree/main/3289.%20The%20Two%20Sneaky%20Numbers%20of%20Digitville)

### 題目

In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to `n - 1`.

Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers.

Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

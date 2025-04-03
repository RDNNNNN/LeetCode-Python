## 2469. Convert the Temperature 轉換溫度

### 題目
# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
# Return the array ans.
# Answers within 10 - 5 of the actual answer will be accepted.

### 中文
# 您將獲得一個四捨五入到小數點後兩位攝氏溫度的非負浮點數，表示以攝氏溫度為單位的溫度
# 您應該將攝氏度轉換為克氏溫度和華氏溫度，並將其作為陣列傳回 ans = [kelvin, fahrenheit]
# 傳回陣列 ans
# 與實際答案相差 10 - 5 以內的答案將被接受

### Note that 注意:
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

### Example 1 範例:
# Input: celsius = 36.50
# Output: [309.65000,97.70000]

### Explanation 解釋:
# Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
# 36.50 攝氏度的溫度換算為克氏溫度為 309.65，換算為華氏溫度為 97.70

### Example 2 範例:
# Input: celsius = 122.11
# Output: [395.26000,251.79800]

### Explanation 解釋:
# Temperature at 122.11 Celsius converted in Kelvin is 395.26 and converted in Fahrenheit is 251.798.
# 122.11 攝氏度的溫度換算為克氏溫度為 395.26，換算為華氏溫度為 251.798

### Constraints 限制:
# 0 <= celsius <= 1000

### Code

from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.8 + 32
        return [kelvin, fahrenheit]


# 設定克氏跟華氏的溫度


# class Solution:
#     def convertTemperature(self, celsius: float) -> List[float]:
#         return [celsius + 273.15, celsius * 1.8 + 32]

# 直接寫在 list 裡面


# class Solution:
#     def convertTemperature(self, celsius: float) -> List[float]:
#         result = (celsius + 273.15, celsius * 1.8 + 32)
#         return list(result)

# 先用 tuple 再轉成 list


# class Solution:
#     def convertTemperature(self, celsius: float) -> List[float]:
#         conversions = [lambda c: c + 273.15, lambda c: c * 1.8 + 32]
#         return [func(celsius) for func in conversions]

# 使用串列推導氏搭配 lambda 表達式

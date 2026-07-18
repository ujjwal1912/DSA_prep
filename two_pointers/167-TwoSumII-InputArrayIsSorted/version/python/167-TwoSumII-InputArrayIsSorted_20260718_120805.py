# Last updated: 7/18/2026, 12:08:05 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        l, r = 0, len(numbers) - 1
4        while l < r:
5            temp_sum = numbers[l] + numbers[r]
6            if temp_sum == target:
7                return [l+1, r+1]
8            elif temp_sum > target:
9                r -= 1
10            else:
11                l += 1
12        return -1
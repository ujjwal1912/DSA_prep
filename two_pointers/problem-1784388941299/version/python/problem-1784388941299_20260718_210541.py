# Last updated: 7/18/2026, 9:05:41 PM
1MOD = 10**9 + 7
2
3class Solution:
4    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
5        if len(nums)<2:
6            return 0
7        count_left = 0
8        count_mid = 0
9        count_right = 0
10        ans = 0
11        for num in nums:
12            if num < a:
13                count_left += 1
14                ans = (ans + count_mid + count_right) % MOD
15            elif a <= num <= b:
16                count_mid += 1
17                ans = (ans + count_right) % MOD
18            else:
19                count_right += 1
20        return ans % MOD
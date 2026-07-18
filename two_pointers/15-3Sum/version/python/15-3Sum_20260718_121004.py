# Last updated: 7/18/2026, 12:10:04 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        ans = []
4        nums.sort()
5        for i in range(len(nums)):
6            if nums[i] > 0:
7                break
8            if i > 0 and nums[i] == nums[i-1]:
9                continue
10            l, r = i + 1, len(nums) - 1
11            while l < r:
12                temp_sum = nums[l] + nums[i] + nums[r]
13                if temp_sum == 0:
14                    ans.append([nums[i], nums[l], nums[r]])
15                    l += 1
16                    r -= 1
17                    while l < r and l > 0 and nums[l] == nums[l-1]:
18                        l += 1
19                elif temp_sum > 0:
20                    r -= 1
21                else:
22                    l += 1
23        return ans
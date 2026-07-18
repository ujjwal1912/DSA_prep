# Last updated: 7/18/2026, 5:41:23 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        b1 = curr = 0
7        b2 = len(nums)-1
8
9        while curr <= b2:
10            if nums[curr]==0:
11                nums[curr], nums[b1] = nums[b1], nums[curr]
12                b1+=1
13                curr+=1
14            elif nums[curr]==1:
15                curr+=1
16            else:
17                nums[curr], nums[b2] = nums[b2], nums[curr]
18                b2-=1
19
20
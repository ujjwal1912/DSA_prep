# Last updated: 7/18/2026, 5:43:01 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        ptr1 = 0
7        ptr2 = len(nums) - 1
8        i=0
9        while i <= ptr2:
10            num = nums[i] 
11            if num == 0:
12                nums[i], nums[ptr1] = nums[ptr1], nums[i]
13                ptr1 += 1
14            elif num == 2:
15                nums[i], nums[ptr2] = nums[ptr2], nums[i]
16                ptr2 -= 1
17                i -= 1
18            i += 1
19        
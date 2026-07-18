# Last updated: 7/18/2026, 5:43:31 PM
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
14                i += 1
15            elif num == 2:
16                nums[i], nums[ptr2] = nums[ptr2], nums[i]
17                ptr2 -= 1
18            else:
19                i += 1
20        
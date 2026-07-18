# Last updated: 7/18/2026, 11:50:05 AM
# sorting in nlog(n) and GCD in log(n) and extra space for recusion stack
1class Solution:
2    def findGCD(self, nums: List[int]) -> int:
3        nums.sort()
4        return self.gcd(nums[0], nums[-1])
5    def gcd(self, a: int, b: int) -> int:
6        return a if b==0 else self.gcd(b, a%b)
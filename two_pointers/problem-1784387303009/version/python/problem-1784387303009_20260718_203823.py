# Last updated: 7/18/2026, 8:38:23 PM
1class Solution:
2    def maximumValue(self, n: int, s: int, m: int) -> int:
3        if n==1:
4            return s
5        ans = s
6        if n >= 2:
7            ans += n//2*m
8        if n >= 3:
9            ans -= (n-1)//2
10        return ans + 1 if n%2 else ans
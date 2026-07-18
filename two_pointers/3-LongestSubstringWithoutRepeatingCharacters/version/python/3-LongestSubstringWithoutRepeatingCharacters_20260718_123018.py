# Last updated: 7/18/2026, 12:30:18 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        l = 0
4        max_len = 0
5        hash = defaultdict()
6        for r in range(len(s)):
7            if s[r] in hash:
8                l = max(l, hash[s[r]]+1)
9            max_len = max(max_len, r-l+1)
10            hash[s[r]] = r
11        return max_len
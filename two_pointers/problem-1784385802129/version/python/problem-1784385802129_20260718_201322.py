# Last updated: 7/18/2026, 8:13:22 PM
1class Solution:
2    def rearrangeString(self, s: str, x: str, y: str) -> str:
3        if x not in s or y not in s:
4            return s
5        cnt = Counter(s)
6        ans = ""
7        ans += y * cnt[y]
8        cnt[y] = 0
9        ans += x * cnt[x]
10        cnt[x] = 0
11        for c in cnt:
12            if cnt[c]:
13                ans += c * cnt[c]
14        return ans
15        
# Last updated: 7/19/2026, 7:53:55 AM
1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        freq = Counter(s)
4        stack = []
5        seen = set()
6        for c in s:
7            freq[c] -= 1
8            if c in seen:
9                continue
10            while stack and stack[-1] > c and freq[stack[-1]] > 0:
11                seen.remove(stack.pop())
12            stack.append(c)
13            seen.add(c)
14        return "".join(stack)
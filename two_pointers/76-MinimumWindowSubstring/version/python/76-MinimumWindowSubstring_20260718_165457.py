# Last updated: 7/18/2026, 4:54:57 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        freq_t = Counter(t)
4        freq_curr = defaultdict(int)
5        l = 0
6        need = len(freq_t)
7        matches = 0
8        best_l = 0
9        best_len = len(s) + 1
10        for r in range(len(s)):
11            freq_curr[s[r]] += 1
12            if s[r] in freq_t and freq_t[s[r]] == freq_curr[s[r]]:
13                matches += 1
14            
15            while matches >= need and l <= r:
16                if r - l + 1 < best_len:
17                    best_len = r - l + 1
18                    best_l = l
19
20                if s[l] in freq_t:
21                    freq_curr[s[l]] -= 1
22                    if freq_t[s[l]] > freq_curr[s[l]]:
23                        matches -= 1
24
25                l += 1
26        return s[best_l: best_l + best_len] if best_len != len(s) + 1 else ""
27
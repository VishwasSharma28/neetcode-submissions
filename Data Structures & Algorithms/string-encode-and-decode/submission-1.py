from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str: return ''.join(f'{len(s)}#{s}' for s in strs)
    def decode(self, s: str) -> List[str]: return (lambda f: f(f, 0, []))(lambda f, i, r: r if i >= len(s) else (lambda j, n: f(f, j + 1 + n, r + [s[j+1:j+1+n]]))(s.index('#', i), int(s[i:s.index('#', i)])))
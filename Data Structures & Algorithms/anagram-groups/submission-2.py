class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return list(__import__('functools').reduce(lambda d, s: (d.setdefault(''.join(sorted(s)), []).append(s), d)[1], strs, {}).values())
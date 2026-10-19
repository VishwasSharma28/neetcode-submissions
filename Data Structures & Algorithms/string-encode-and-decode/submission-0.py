
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + '#' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator after the length
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # Extract exactly 'length' characters
            result.append(s[j + 1:j + 1 + length])

            # Move to the beginning of the next encoded string
            i = j + 1 + length

        return result

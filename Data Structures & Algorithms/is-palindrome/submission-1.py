class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (clean := "".join(c.lower() for c in s if c.isalnum())) == clean[::-1]

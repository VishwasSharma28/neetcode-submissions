class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t1=[]
        s1 = []
        for i in t:
            t1.append(i)
        for i in s:
            s1.append(i)
        t1.sort()
        s1.sort()
        if len(t1) != len(s1):
            return False
        for i in range(len(t1)):
            if s1[i] != t1[i]:
                return False
            
        return True

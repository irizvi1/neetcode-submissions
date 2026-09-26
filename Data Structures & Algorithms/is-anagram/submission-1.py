class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #{r:2,a:2,c:1,e:1}
        if len(s) != len(t):
            return False
        
        
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for c in t:
            counts[c] = counts.get(c, 0) - 1
            
        for c in s:
            if counts[c] != 0:
                return False
        for c in t:
            if counts[c] !=0:
                return False
        return True

            

        
        
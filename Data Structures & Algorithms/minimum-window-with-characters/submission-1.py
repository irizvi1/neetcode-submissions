class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #initialize tneed {} with all characters in t with their counts 
        #while we have not met t's condition, continue to increment r, if we have, increment l until it doesnt, each time saving shortest string in resindex[l[s], r[s]] and shortestlength

        if s == "" or t == "":
            return ""
        
        
        tneed = {}
        window = {}
        l = 0
        
        have = 0
        resindex = [-1, -1]
        shortestlength = float('inf')
        

        for c in t:
            tneed[c] = tneed.get(c, 0) + 1
        need = len(tneed)
        
        for r in range(len(s)):

            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in tneed and window[s[r]] == tneed[s[r]]:
                have +=1
                    
            while have == need:

                if shortestlength > ((r-l) + 1):
                    shortestlength  = ((r-l) + 1)
                    resindex = [l, r]
                window[s[l]] -= 1
                if s[l] in tneed and window[s[l]] < tneed[s[l]]:
                    have -= 1
                l+=1
    

        if shortestlength == float('inf'):
            return ""
        start, end = resindex
        return s[start:end + 1]
                
        
            
            

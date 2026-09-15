class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #mlen gets updated to currlen whenever curr len is larger
        #currlen = (R - L) + 1
        #+ new letter into set 
        #whenever we see a duplicate in the set, move l to r and delete set
        #

        
        dupes = set()
        L = 0
        R = 0
        mlen = 0
        currlen = 0
        #pwwkew

        for R in range(len(s)):
            
            while s[R] in dupes:
                dupes.remove(s[L])
                L += 1
                
            dupes.add(s[R])
            currlen = (R-L) + 1
            mlen = max(mlen, currlen)
            
        return mlen

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        L = 0
        R = 0
        mlen = 0
        

        for R in range(len(s)):
            counts[s[R]] = counts.get(s[R], 0) + 1

            while ((R-L)+1) - (max(counts.values())) > k:
                counts[s[L]] -= 1
                L +=1
            
            mlen = max(mlen, ((R-L) + 1))
        return mlen

      

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        #move all stones accoridng to gravity and obstacles, then rotate
        #create rows and cols variables, loop thru entire matrix, row by row, for each row go in reverse, if c at stone, swap with i and i-=1, if c at obstacle i = c-1
        #create res[]
        #iterate thru boxGrid cols by row this time, and go thru rows in reverse, appening boxGrid[r][c] to populate the cols, and append the cols to res

        row = len(boxGrid)
        cols = len(boxGrid[0])
        
        res = []

        for r in range(row):
            i = cols-1
            for c in reversed(range(cols)):
                if boxGrid[r][c] == "#":
                    boxGrid[r][c], boxGrid[r][i] = boxGrid[r][i], boxGrid[r][c]
                    i-=1
                elif boxGrid[r][c] == "*":
                    i = c-1

        
        for c in range(cols):
            newcol = []
            for r in reversed(range(row)):
                newcol.append(boxGrid[r][c])
            res.append(newcol)
        return res



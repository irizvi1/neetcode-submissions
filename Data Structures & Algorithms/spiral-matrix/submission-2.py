class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        i=0
        j = 0
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

        ceiling = 0
        rwall = n
        floor = m
        lwall = -1
        
        direction = RIGHT

        while len(res) < (m*n):
            if direction == RIGHT:
                while j < rwall: 
                    res.append(matrix[i][j])
                    j+=1
                ceiling = i 
                direction = DOWN
                i, j = i+1, j-1
            elif direction == DOWN :
                while i < floor:
                    res.append(matrix[i][j])
                    i+=1
                rwall = j 
                direction = LEFT
                i, j = i-1, j-1
            elif direction == LEFT :
                while j > lwall:
                    res.append(matrix[i][j])
                    j-=1
                floor = i
                direction = UP
                i, j = i-1, j+1
            else:
                while i > ceiling:
                    res.append(matrix[i][j])
                    i-=1
                lwall  = j
                direction = RIGHT
                i, j = i+1, j+1
        return res

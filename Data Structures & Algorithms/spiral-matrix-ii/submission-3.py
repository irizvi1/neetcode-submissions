class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]

        i = 0
        j = 0

        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

        ceiling = 0
        rwall = n
        floor = n
        lwall = -1

        direction = RIGHT

        count = 1
        while count <= n*n:
            if direction == RIGHT:  
                while j < rwall:
                    mat[i][j] = count
                    count+=1
                    j+=1
                direction = DOWN
                ceiling = i
                i, j = i+1, j-1
            elif direction == DOWN:
                while i < floor:
                    mat[i][j] = count
                    count+=1
                    i+=1
                direction = LEFT
                rwall = j
                i, j = i-1, j-1
            elif direction == LEFT:
                while j > lwall:
                    mat[i][j] = count
                    count+=1
                    j-=1
                direction = UP
                floor = i
                i,j = i-1, j+1
            else:
                while i>ceiling:
                    mat[i][j] = count
                    count+=1
                    i-=1
                direction = RIGHT
                lwall = j
                i,j, = i+1, j+1
        return mat
        


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.mat = []
        for i in range(rows + 1):
            row = []
            for j in range(cols + 1):
                row.append(0)
            self.mat.append(row)

        for i in range(rows):
            presum = 0
            for j in range(cols):
                presum += matrix[i][j]
                self.mat[i+1][j+1] = presum + self.mat[i][j+1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1 + 1,col1+1,row2+1,col2+1

        bottomright = self.mat[row2][col2]
        topleftarea = self.mat[row1 -1][col1-1]
        above = self.mat[row1 -1][col2]
        left = self.mat[row2][col1-1]

        res = bottomright - above - left + topleftarea

        return res




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
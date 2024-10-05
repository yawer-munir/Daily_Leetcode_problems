class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j<=i:
                    matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
        
        for i in matrix:
            i.reverse()
        
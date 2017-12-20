class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        #先转置
        for i in range(n):
            for j in range(i+1,n):
                tmp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i] = tmp
        #再水平翻转
        for i in range(n):
            for j in range(n/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n-j-1]
                matrix[i][n-j-1] = tmp
                
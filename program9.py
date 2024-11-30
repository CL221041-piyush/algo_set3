def print_spiral(matrix):
    if not matrix:
        return
    
    m = len(matrix)  
    n = len(matrix[0])  
    
    top, bottom, left, right = 0, m - 1, 0, n - 1
    result = []

    while top <= bottom and left <= right:
    
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1 

        
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  

        if top <= bottom:
           
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1  

        if left <= right:
         
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  
    
    
    print(" ".join(map(str, result)))


matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print_spiral(matrix1)  

matrix2 = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]
]
print_spiral(matrix2)  

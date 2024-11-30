def subarray_or(A):
    N = len(A)
    result = 0
    current_or = set()  
    
    for i in range(N):
        temp_or = 0
        for j in range(i, N):
            temp_or |= A[j]
            current_or.add(temp_or)
    
    for value in current_or:
        result |= value
        
    return result
print(subarray_or([1, 4, 6]))  
print(subarray_or([10, 100, 1000]))  

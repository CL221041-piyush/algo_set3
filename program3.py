from collections import deque

def max_of_subarrays(arr, K):
    N = len(arr)
    deq = deque()  
    result = []

    for i in range(N):
        if deq and deq[0] < i - K + 1:
            deq.popleft()

        while deq and arr[deq[-1]] <= arr[i]:
            deq.pop()

        deq.append(i)
        if i >= K - 1:
            result.append(arr[deq[0]])

    return result


arr = [1, 2, 3, 1, 4, 5]
K = 3
print(max_of_subarrays(arr, K))  

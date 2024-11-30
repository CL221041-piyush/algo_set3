def count_combinations(sum, coins):
   
    dp = [0] * (sum + 1)
    
   
    dp[0] = 1
    
   
    for coin in coins:
    
        for i in range(coin, sum + 1):
            dp[i] += dp[i - coin]
    
    
    return dp[sum]


print(count_combinations(4, [1, 2, 3]))  
print(count_combinations(10, [2, 5, 3, 6]))  
print(count_combinations(10, [10]))  
print(count_combinations(5, [4]))  

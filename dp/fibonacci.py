# basic recursive solution for finding the nth fibonacci number:
def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

#################################################################

# fibonacci number using memoization
def fibRec(n, memo):
    # base case
    if n <= 1:
        return n
    # to check if output altready exists:
    if memo[n] != -1:
        return memo[n]
    
    # calculate and save output for future use:
    memo[n] = fibRec(n - 1, memo) + \
        fibRec(n - 2, memo)
    
    return memo[n]

def fib_memo(n):
    memo = [-1] * (n + 1)
    return fibRec(n, memo)


#################################################################

# fibonacci number using tabulation
def fibo_tab(n):
    dp = [0] * (n + 1)

    # storing the indipendent values in dp
    dp[0] = 0
    dp[1] = 1

    # using bottom - up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[i]


print(fibo_tab(6))
'''
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

        Example 1:
        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps

        Example 2:
        Input: n = 3
        Output: 3
        Explanation: There are three ways to climb to the top.
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
    
        Constraints:
        1 <= n <= 45
'''

def climbStairs(n: int) -> int:
    if n == 1:
            return 1
    if n < 1 | n > 45:
        return None
    sol = [0] * n
    sol[0] = 1  # floor 1 -> 1 way
    sol[1] = 2 # floor 2 -> 2 ways (1 + 1 | 2)
    # floor 3 -> 3 ways ->  #ways to arrive to 2 summed with 1 + #number of ways to arrive to 1 summed with 2
    for i in range(2, n):
        sol[i] = sol[i - 1] + sol[i - 2]
    return sol[n - 1]


print(climbStairs(6))
# Dynamic Programming Template

Date: 12/21/2024
Yilin Zhao

## Basic Templates (Top Down+Buttom Up)

**State Definition**

Define what a "state" represents in your problem
Identify what information you need to uniquely describe a subproblem
Example: In Fibonacci, the state is just n (which number in sequence)


**Recurrence Relation**

Figure out how to break problem into smaller subproblems
Write an equation showing how current state relates to previous states
Example: For Fibonacci, F(n) = F(n-1) + F(n-2)


**Base Cases**

Identify the smallest possible subproblems
Define their answers directly
Example: For Fibonacci, F(0) = 0 and F(1) = 1


**State Organization**

Decide processing order (bottom-up or top-down)
Choose data structure (array, hash table, etc.)
Make sure you can access previous states when needed


**Implementation**

Code either bottom-up (tabulation) or top-down (memoization)
Include way to reconstruct solution if needed
Optimize space/time if possible


<details>
<summary>Top-Down</summary>

### Explanation

```python
# Top-down approach (Memoization)
def solve_recursive(input_data):
    # Initialize cache/memo
    memo = {}
    
    def dp(state):
        # Base cases
        if state in base_cases:
            return base_case_value
        
        # Check if already computed
        if state in memo:
            return memo[state]
        
        # Initialize result for this state
        result = initial_value
        
        # Recurrence relation
        for next_state in get_possible_next_states(state):
            # Calculate result using subproblems
            current_result = combine_results(dp(next_state))
            result = optimize(result, current_result)
        
        # Store in memo before returning
        memo[state] = result
        return result
    
    return dp(initial_state)
```

**Notes**
To be added

</details>



<details>
<summary>Buttom Up</summary>

### Explanation

```python
# Bottom-up approach (Tabulation)
def solve_iterative(input_data):
    # Initialize dp table
    dp_table = initialize_table()
    
    # Fill base cases
    for base_case in base_cases:
        dp_table[base_case] = base_case_value
    
    # Iterate through states in order
    for state in get_states_in_order():
        # Initialize result for this state
        result = initial_value
        
        # Recurrence relation
        for prev_state in get_possible_prev_states(state):
            # Calculate result using previously computed values
            current_result = combine_results(dp_table[prev_state])
            result = optimize(result, current_result)
        
        dp_table[state] = result
    
    return dp_table[final_state]

```

**Notes**
Some variations in the middle block, we call dfs(node.left), then res.append(node.val), then dfs(node.right)


</details>

## Some Samples

<details>
<summary>Fibonacci Bottom-up</summary>

### Explanation

```python
# Example: Fibonacci sequence implementation
def fibonacci(n):
    # Top-down approach
    def fib_recursive(n, memo={}):
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = fib_recursive(n-1, memo) + fib_recursive(n-2, memo)
        return memo[n]
```

**Notes**
The memo dictionary works like a cache:

Before calculating fib(n), we check if we've seen this n before
If we have, we return the stored result instead of recalculating
If we haven't, we calculate it once and store it for future use

For example, when calculating fib(5):

First time we see fib(3), we calculate it
Later when we need fib(3) again, instead of recalculating, we just look it up in memo

</details>

<details>
<summary>Fibonacci Top-Down</summary>

### Explanation

```python
    # Bottom-up approach
    def fib_iterative(n):
        #this part handles when n is directly fed in as 0 or 1. However, it does not help much with the dp.
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```

**Notes**
ah, so for the buttom up approach, you make dp an 2d array having n entries, just like the memo, right? this is interesting!

The main differences between the top-down and buttom-up approach are:

Direction: Memo starts from n and works backwards through recursion, while dp array starts from 0 and builds up
Structure: Memo is a dictionary that only stores values we need, while dp array pre-allocates space for all values from 0 to n
Control flow: Memo fills through recursive calls, dp array fills through a loop


</details>
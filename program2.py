def decode_message( s: str, p: str) -> bool:
        n = len(s)
        m=len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Initial state
        dp[0][0] = True
        
        # Handle patterns starting with '*'
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' matches zero or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or p[j - 1] == p[i - 1]:
                    # '?' matches exactly one character or direct match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]
        return True



# write your code here
  
        

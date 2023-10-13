def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D array to store the lengths of LCS for subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp array in a bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of LCS is stored in dp[m][n]
    return dp[m][n]

# Example usage:
X = "AGGTAB"
Y = "GXTXAYB"
result = longest_common_subsequence(X, Y)
print("Length of Longest Common Subsequence:", result)

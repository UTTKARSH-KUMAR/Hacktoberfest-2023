def longest_palindromic_subsequence(s):
    n = len(s)

    # Create a 2D array to store the lengths of LPS for subproblems
    dp = [[0] * n for _ in range(n)]

    # Initialize LPS length for substrings of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the dp array in a bottom-up manner
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # The length of LPS is stored in dp[0][n-1]
    return dp[0][n - 1]

# Example usage:
s = "bbbab"
result = longest_palindromic_subsequence(s)
print("Length of Longest Palindromic Subsequence:", result)

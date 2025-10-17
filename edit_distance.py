# edit_distance.py

def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],   # delete
                                   dp[i][j-1],   # insert
                                   dp[i-1][j-1]) # replace

    return dp[m][n]

if __name__ == "__main__":
    pairs = [
        ("kitten", "sitting"),
        ("flaw", "lawn"),
        ("intention", "execution"),
        ("", "abc"),
        ("abc", "abc")
    ]
    for a, b in pairs:
        print(f"Edit distance between '{a}' and '{b}':", edit_distance(a, b))

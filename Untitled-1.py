
# def editDistRec(s1, s2, m, n, memo):
#     if m == 0:
#         return n
#     if n == 0:
#         return m
#     if memo[m][n] != -1:
#         return memo[m][n]
#     if s1[m - 1] == s2[n - 1]:
#         memo[m][n] = editDistRec(s1, s2, m - 1, n - 1, memo)
#         return memo[m][n]
#     memo[m][n] = 1 + min(
#         editDistRec(s1, s2, m, n - 1, memo),
#         editDistRec(s1, s2, m - 1, n, memo),
#         editDistRec(s1, s2, m - 1, n - 1, memo)
#     )
#     return memo[m][n]

# # Wrapper function to initiate the recursive calculation
# def editDistance(s1, s2):
#     m, n = len(s1), len(s2)
#     memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
#     return editDistRec(s1, s2, m, n, memo)

# if __name__ == "__main__":
#     s1 = "I'm fine"
#     s2 = "Im"
#     print(editDistance(s1, s2))
def lcs_tables(X, Y):
    m, n = len(X), len(Y)
    c = [[0]*(n+1) for _ in range(m+1)]
    b = [[""]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "↖"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "←"
    return c, b

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return []
    if b[i][j] == "↖":
        return print_lcs(b, X, i-1, j-1) + [X[i-1]]
    elif b[i][j] == "↑":
        return print_lcs(b, X, i-1, j)
    else:  # "←"
        return print_lcs(b, X, i, j-1)

# demo
X = list("ABCBDAB")
Y = list("BDCABA")
c, b = lcs_tables(X, Y)
lcs_seq = "".join(print_lcs(b, X, len(X), len(Y)))
print(c, b, len(lcs_seq), lcs_seq)  # -> 4 BCBA (một LCS hợp lệ)

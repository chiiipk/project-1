
def memoiz(s1, s2, m, n, mem):
    if m == 0:
        return n
    if n == 0:
        return m
    if mem[m][n] != -1:
        return mem[m][n]
    if s1[m - 1] == s2[n - 1]:
        mem[m][n] = memoiz(s1, s2, m - 1, n - 1, mem)
        return mem[m][n]
    mem[m][n] = 1 + min(
        memoiz(s1, s2, m, n - 1, mem),
        memoiz(s1, s2, m - 1, n, mem),
        memoiz(s1, s2, m - 1, n - 1, mem)
    )
    return mem[m][n]

# Wrapper function to initiate the recursive calculation
def minED(s1, s2):
    m, n = len(s1), len(s2)
    mem = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    return memoiz(s1, s2, m, n, mem)

if __name__ == "__main__":
    s1 = "I'm fine"
    s2 = "Im fine"
    print(minED(s1, s2))

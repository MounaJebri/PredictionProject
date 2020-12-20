def solution(A, B):
    # write your code in Python 2.7
    fib_end = max(A) + 2
    fib = [0] * fib_end

    fib[1] = 1
    for i in xrange(2, fib_end):
        fib[i] = fib[i - 1] + fib[i - 2]

    # print fib
    result = [0] * len(A)
    for i, a in enumerate(A):
        # print i
        # result[i] = fib[a+1] % pow(2, B[i])
        # result[i] = fib[a+1] % (1<<B[i])  # perf 75%, O(L**2)
        result[i] = fib[a + 1] & ((1 << B[i]) - 1)  # perf 100%, O(L)
    return result
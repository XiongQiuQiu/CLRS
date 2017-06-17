def fib(n):
    d = {0: 0, 1: 1}
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n],d

print fib(10)

'''native recursive squaring'''
y = (1 + 5 ** 0.5) / 2
n = int()
fn = (y ** n) / (5 ** 0.5)

'''real native recursive squating'''
'''theory'''
#[[F(n+1), F(n)],[F(n), F(n-1)]] = [[1, 1], [1, 0]] ** n
#O(n) = logn

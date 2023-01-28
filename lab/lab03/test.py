def foo(n):
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            checker = (lambda f, i : lambda x: x % i == 0 or f(x) )(checker, i)
        i = i + 1
    return checker

foo(4)(12)

def foo1(n):
    def checker(x):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(f, k):
                def inner(x):
                    return x % k == 0 or f(x)
                return inner
            checker = outer(checker,i)
        i = i + 1
    return checker

foo1(4)(6)
from pyrival.data_structures import convex_hull_trick, max_query

def brute(K, M, X):
    assert(len(K) == len(M))

    out = []
    for x in X:
        y = K[0] * x + M[0]
        for i in range(1, len(K)):
            y = max(y, K[i] * x + M[i])
        out.append(y)
    return out


def test_convex_line_hull_integral(n = 1000):
    import random
    random.seed(1337)

    K = [random.randint(-1000, 1000) for _ in range(n)]
    M = [random.randint(-1000, 1000) for _ in range(n)]
    
    X = [random.randint(-10000, 10000) for _ in range(n)]
    brute_ans = brute(K, M, X)

    hull_i, hull_x = convex_hull_trick(K, M)
    assert(len(hull_i) - 1 == len(hull_x))

    ans = [max_query(x, K, M, hull_i, hull_x) for x in X]
    assert(ans == brute_ans)

def test_convex_line_hull_float(n = 1000):
    import random
    random.seed(1337)

    K = [random.randint(-1000, 1000) for _ in range(n)]
    M = [random.randint(-1000, 1000) for _ in range(n)]
    
    X = [random.uniform(-10000, 10000) for _ in range(n)]
    brute_ans = brute(K, M, X)

    hull_i, hull_x = convex_hull_trick(K, M, integer = False)
    assert(len(hull_i) - 1 == len(hull_x))

    ans = [max_query(x, K, M, hull_i, hull_x) for x in X]
    assert(len(ans) == len(brute_ans))
    assert(all(abs(x - y) <= 1e-9 for x,y in zip(ans, brute_ans)))

def failure_fun(P):
    m = len(P)
    valor_f = [0] * m
    k = 0
    j = 1

    while j < m:
        if P[j] == P[k]:
            valor_f[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = valor_f[k - 1]
        else:
            j += 1
    return valor_f


def find_kmp(T, P):
    n, m = len(T), len(P)

    if m == 0:
        return 0

    result_failure = failure_fun(P)
    j = 0
    k = 0

    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = result_failure[k - 1]
        else:
            j += 1

    return -1

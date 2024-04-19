# Alex Shrestha
# Rod Cutting Dynamic Programming Problem

# Recursive problem, too memory intensive after n > 40
def cut_rod(p, n):
    if n == 0:
        return 0

    q = -10000

    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))

    return q


def memoized_cut_rod(p, n):
    # where solutions will be remembered
    r = [-1] * (n+1)

    return memoized_cut_rod_helper(p, n, r)

def memoized_cut_rod_helper(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -1

        for i in range(1, n+1):
            q = max(q, p[i] + memoized_cut_rod_helper(p, n-i, r))

    r[n] = q
    return q

def tabulation_cut_rod(p, n):
    r = [-1] * (n+1)
    r[0] = 0

    for j in range(1, n+1):
        q = -1

        for i in range(1, j+1):
            q = max(q, p[i] + r[j-i])

        r[j] = q

    return r[n]


def main():
    p = [0, 1, 5, 8, 9, 10, 17, 18, 20]
    

    print("Using memoization:")
    for i in range(1, 8):
        max_profit = memoized_cut_rod(p, i)
        print(f"Max profit for {i}: ${max_profit}")

    print("Using tabulation:")
    for i in range(1, 8):
        max_profit = tabulation_cut_rod(p, i)
        print(f"Max profit for {i}: ${max_profit}")


    return



if __name__ == "__main__":
    main()


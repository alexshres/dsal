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


def main():
    p = [0, 1, 5, 8, 9, 10, 17, 18, 20]
    

    for i in range(1, 8):
        max_profit = cut_rod(p, i)
        print(f"Max profit for {i}: ${max_profit}")


    return



if __name__ == "__main__":
    main()


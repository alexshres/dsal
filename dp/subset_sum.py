

def subset_sum(n, weight, mat, weight_list):
    for i in range(1, n+1):
        for w in range (0, w+1):
            not_include = mat[i-1, w]
            include_weight = w - weight_list[i]
            include = mat[i-1, include_weight] + weight_list[i]

            if include_weight < 0:
                include = 0

            mat[i, w] = max(not_include, include)


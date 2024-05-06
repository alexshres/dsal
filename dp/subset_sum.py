import numpy as np

def subset_sum(n, weight, mat, weight_list):
    for i in range(1, n+1):
        for w in range (0, w+1):
            not_include = mat[i-1, w]
            include_weight = w - weight_list[i]
            include = mat[i-1, include_weight] + weight_list[i]

            if include_weight < 0:
                include = 0

            mat[i, w] = max(not_include, include)

    return mat


def main:
    # length of arr
    rows = 10

    # weight we want to test against
    cols = 25

    matrix = np.zeros((rows, cols))     
    
    # test weight arr
    weight_list = [5, 8, 1, 4, 2, 4, 3, 1, 7, 9]

    # need to set matrix to updated one returned by subset_sum()
    matrix = subset_sum(rows, cols, matrix, weight_list)





    


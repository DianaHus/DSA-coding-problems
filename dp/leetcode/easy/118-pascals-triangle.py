'''
    https://leetcode.com/problems/pascals-triangle/description/?envType=problem-list-v2&envId=dynamic-programming
'''

from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows < 1 | numRows > 30:
        return None
    triangle = []
    triangle.append([1])
    for i in range(1, numRows):
        new_l = [1] * (i + 1)
        for j in range(1, i):
            new_l[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(new_l)
    return(triangle)

print(generate(5))

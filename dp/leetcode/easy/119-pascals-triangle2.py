'''
    https://leetcode.com/problems/pascals-triangle-ii/?envType=problem-list-v2&envId=dynamic-programming
'''
from typing import List


def getRow(rowIndex: int) -> List[int]:
    if rowIndex < 0:
        return None
    if rowIndex == 0:
        return []
    if rowIndex == 1:
        return [1]
    triangle = [[1]]
    for i in range(1, rowIndex + 1):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle[rowIndex]

def getRowoptimized(rowIndex: int) -> List[int]:
    if rowIndex < 0:
        return []
    row = [1] + [0] * rowIndex
    for i in range(1, rowIndex + 1):
        for j in range(i, 0, -1):
            row[j] += row[j - 1]
    return row

print(getRowoptimized(4))
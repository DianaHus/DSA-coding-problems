'''
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     target = 1
    l = 0, r = 9
    m = 4
    
'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        m = left + (right - left) // 2
        if arr[m] == target:
            return m
        if arr[m] < target:
            left = m + 1
        else:
            right = m - 1
    return -1

print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
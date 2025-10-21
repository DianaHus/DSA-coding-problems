'''
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
    Example 3:

    Input: nums = [1], target = 0
    Output: -1

    Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104
'''

from typing import List


'''def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if nums[r] < target :
            # left side 100% sure:
            r = m
        elif nums[m] < target: 
            # right side 100%
            l = m + 1
        elif nums[l] > target:
            #right 100%
            l = m + 1
        else:
            r = m
    return -1'''


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = l + (r - l) // 2
        
        if nums[m] == target:
            return m
            
        # Check if left half is sorted
        if nums[l] <= nums[m]:
            # Left half is sorted
            if nums[l] <= target < nums[m]:
                r = m - 1  # Target is in left half
            else:
                l = m + 1  # Target is in right half
        else:
            # Right half is sorted
            if nums[m] < target <= nums[r]:
                l = m + 1  # Target is in right half
            else:
                r = m - 1  # Target is in left half
    
    return -1


print(search([4,5,6,7,0,1,2], 2))
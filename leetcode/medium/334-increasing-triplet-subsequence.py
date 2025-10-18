'''
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


    Example 1:

    Input: nums = [1,2,3,4,5]
    Output: true
    Explanation: Any triplet where i < j < k is valid.
    Example 2:

    Input: nums = [5,4,3,2,1]
    Output: false
    Explanation: No triplet exists.
    Example 3:

    Input: nums = [2,1,5,0,4,6]
    Output: true
    Explanation: One of the valid triplet is (3, 4, 5), because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

    Constraints:

    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1

    Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
'''

from typing import List


## unacceptable complexity :( 
'''
def increasingTriplet(nums: List[int]) -> bool:
    for i in range(len(nums) - 2):
        for j in range(i, len(nums) - 1):
            for k in range(j, len(nums)):
                if nums[i] < nums[j] & nums[j] < nums[k]:
                    return True
    return False
'''

## SOOOO:
def increasingTriplet(nums: List[int]) -> bool:
    """
    Maintain two variables min1 and min2 as the smallest and second-smallest values
    seen so far. For each number:
      - if num <= min1: update min1 (we found a new smaller candidate)
      - elif num <= min2: update min2 (we found a better middle candidate)
      - else: num > min2, so there exists min1 < min2 < num and we can return True.
    This runs in O(n) time and uses O(1) extra space. The use of <= ensures duplicates
    don't produce false positives.
    """
    min1, min2 = float('inf'), float('inf')
    for num in nums:
        if num <= min1:
            min1 = num
        elif num <= min2:
            min2 = num
        else:
            return True
    return False

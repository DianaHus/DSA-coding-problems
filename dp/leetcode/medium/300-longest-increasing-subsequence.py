'''
    Given an integer array nums, return the length of the longest strictly increasing subsequence.

    Example 1:

    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    Example 2:

    Input: nums = [0,1,0,3,2,3]
    Output: 4
    Example 3:

    Input: nums = [7,7,7,7,7,7,7]
    Output: 1
    
    Constraints:

    1 <= nums.length <= 2500
    -104 <= nums[i] <= 104
    
    Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    l = [1] * len(nums)
    for i in range(1, len(nums)):
        subproblems = [l[k] for k in range(i) if nums[k] < nums[i]]
        l[i] = 1 + max(subproblems, default=0)
    return max(l, default=0)


print(lengthOfLIS([3,1,8,2,5]))
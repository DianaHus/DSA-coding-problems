"""
Given a sorted array (ascending order) and a target find arr[i], arr[j]
such that their sum is equal to target.
"""

def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [(arr[left], left), (arr[right], right)]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return None

#arr = [1, 2, 3, 4, 5]
#t = 5
#arr = [-3, -1, 0, 1, 2]
#print(two_sum(arr, t))

"""
Leetcode 125
"""

def is_palindrome(str):
    str_alpha = ""
    for c in str:
        if c.isalpha():
            str_alpha += c.lower()
    l, r = 0, len(str_alpha) - 1
    while l <= r:
        if str_alpha[l] != str_alpha[r]:
            return False
        l += 1
        r -= 1
    return True

#print(is_palindrome("race a car"))

"""
Leetcode 392
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

def isSubsequence(s, t):
    if not t and s:
            return False
    if not s:
        return True
    i, j = 0, 0
    while i < len(t):
        if s[j] == t[i]:
            i += 1
            j += 1
        else:
            i += 1
        if j >= len(s):
            return True
    return False

#t = "ahbgdc"
#s = "abc"
#print(isSubsequence(s, t))
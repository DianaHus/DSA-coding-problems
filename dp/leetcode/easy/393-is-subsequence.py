'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk 
where k >= 109, and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?
'''


def isSubsequence(s: str, t: str) -> bool:
    """Two pointers solution - O(n) time, O(1) space"""
    i = 0  # pointer for s
    j = 0  # pointer for t
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1  # found match, advance s pointer
        j += 1      # always advance t pointer
    
    return i == len(s)

#recursive solution
def isSubsequence_recursive(s: str, t: str) -> bool:
    if s and not t:
        return False
    if not s:
        return True
    if s[0] == t[0]:
        s, t = s[1:], t[1:]
    else:
        t = t[1:]
    return isSubsequence_recursive(s, t)


# Test both solutions
print("Two pointers:", isSubsequence('abc', 'ahbgdc'))
print("Recursive:", isSubsequence_recursive('abc', 'ahbgdc'))
print("Two pointers:", isSubsequence('axc', 'ahbgdc'))
print("Recursive:", isSubsequence_recursive('axc', 'ahbgdc'))
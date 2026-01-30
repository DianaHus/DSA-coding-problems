'''
    Meeting Rooms II

    Given an array of meeting time interval objects consisting of start 
    and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
    find the minimum number of days required to schedule all meetings without 
    any conflicts.

    Note: (0,8),(8,10) is not considered a conflict at 8.

    Example 1:

    Input: intervals = [(0,40),(5,10),(15,20)]

    Output: 2
    Explanation:
    day1: (0,40)
    day2: (5,10),(15,20)

    Example 2:

    Input: intervals = [(4,9)]

    Output: 1
'''

def solution(intervals):
    
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    days = 0
    max_days = 0
    s = 0
    e = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            s += 1
            days += 1
            max_days = max(days, max_days)
        else:
            days -= 1
            e += 1
    return max_days

intervals = [(0,40),(5,10),(15,20)]
print(solution(intervals))
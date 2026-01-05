from typing import Tuple
def merge_intervals(intervals: list):
    intervals = sorted(intervals)

    ans = []
    for interval in intervals:
        # no overlap
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            # merge overlap
            ans[-1][1] = max(ans[-1][1], interval[1])
    return ans

def binary_search(intervals: list, x:int):
    left, right = 0, len(intervals) - 1

    while left <= right:
        mid = (left + right) // 2
        start, end = intervals[mid]

        if start <= x <= end:
            return True
        elif x < start:
            right = mid - 1
        else:
            left = mid + 1

    return False

def solve(count_valid: bool):
    ans = 0
    ranges = []
    merged_intervals = []
    with open("input.txt", "r") as file:
        for line in file:
            input = line.strip().split('-')
            if not input[0]:
                # empty line
                merged_intervals = merge_intervals(ranges)
            elif len(input)==2:
                # range input
                l,r = input
                ranges.append([int(l), int(r)])
            elif not count_valid:
                # check if individual id is valid
                id = int(input[0])
                if binary_search(merged_intervals,id):
                    ans += 1
    # count in each range how many valid ids
    if count_valid:
        ans = 0
        for range in merged_intervals:
            ans += range[1] - range[0] + 1 

    return ans

if __name__=="__main__":
    ans = solve(True)
    print(ans)
    



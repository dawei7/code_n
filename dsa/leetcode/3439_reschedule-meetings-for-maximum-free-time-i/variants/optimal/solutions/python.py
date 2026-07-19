from typing import List

def solve(eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
    # Calculate the gaps between meetings
    # Gaps: [0 to start[0]], [end[0] to start[1]], ..., [end[n-1] to eventTime]
    gaps = []
    
    # Gap before the first meeting
    gaps.append(startTime[0])
    
    # Gaps between meetings
    for i in range(len(startTime) - 1):
        gaps.append(startTime[i+1] - endTime[i])
        
    # Gap after the last meeting
    gaps.append(eventTime - endTime[-1])
    
    # We can merge k meetings, which means we can combine k+1 gaps
    window_size = k + 1
    
    # Use sliding window to find the maximum sum of k+1 consecutive gaps
    current_gap_sum = sum(gaps[:window_size])
    max_free_time = current_gap_sum
    
    for i in range(window_size, len(gaps)):
        current_gap_sum += gaps[i] - gaps[i - window_size]
        if current_gap_sum > max_free_time:
            max_free_time = current_gap_sum
            
    return max_free_time

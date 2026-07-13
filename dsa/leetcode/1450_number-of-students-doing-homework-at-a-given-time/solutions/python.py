def solve(start_time, end_time, query_time):
    return sum(start <= query_time <= end for start, end in zip(start_time, end_time))

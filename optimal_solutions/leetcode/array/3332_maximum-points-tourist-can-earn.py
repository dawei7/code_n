def solve(n: int, k: int, stayScore: list[list[int]], travelScore: list[list[int]]) -> int:
    # dp[city] stores the max points earned ending at 'city' for the current day
    # Initialize with the first day's stay scores
    dp = [stayScore[0][i] for i in range(n)]
    
    for day in range(1, k):
        new_dp = [0] * n
        for curr_city in range(n):
            # Option 1: Stay in the same city
            best_prev = dp[curr_city] + stayScore[day][curr_city]
            
            # Option 2: Travel from any other city 'prev_city'
            for prev_city in range(n):
                if prev_city != curr_city:
                    score = dp[prev_city] + travelScore[prev_city][curr_city] + stayScore[day][curr_city]
                    if score > best_prev:
                        best_prev = score
            
            new_dp[curr_city] = best_prev
        dp = new_dp
        
    return max(dp)

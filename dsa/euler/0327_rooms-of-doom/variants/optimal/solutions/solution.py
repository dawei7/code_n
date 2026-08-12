import math


def solve(max_r: int = 30, min_c: int = 3, max_c: int = 40) -> int:
    """Find sum_{C=3..40} M(C, 30) for the minimum cards required to escape 30 rooms carrying up to C cards.
    
    Time Complexity: O(R * (max_C - min_C)) via Backward DP Recurrence
    Space Complexity: O(1)
    """

    def M(C, R):
        req = 1
        for r in range(R):
            if req < C:
                req += 1
            else:
                trips = math.ceil((req - C + 1) / (C - 2))
                req += 2 * trips + 1
        return req

    return sum(M(C, max_r) for C in range(min_c, max_c + 1))

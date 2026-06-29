# www.codechef.com/problems/LEBAMBOO


def solve():
    def lebamboo():
        """ report (minimum) number of steps for given modifier or infeasibility 
        to transform between actual and desired heights of bamboo stems
        """
        num_stems = int(input())
        heights = list(map(int, input().split()))
        targets = list(map(int, input().split()))
        # special cases - 1 and 2 stems 
        if num_stems == 1:
            # only decrease is possible 
            return max(-1, heights[0] - targets[0])
        if num_stems == 2:
            # sum must stay constant, minimum steps from individual change
            if sum(heights) == sum(targets):
                return (abs(heights[0] - targets[0]))
            else:
                return -1

        # other cases: each step increases total height by n-2
        growth = sum(targets) - sum(heights)
        if growth < 0 or growth % (num_stems - 2) != 0:
            return -1
        # steps based on net change
        steps = growth // (num_stems - 2)
        # feasibility based on individual changes: range and parity restriction 
        allowed = set(range(-steps, steps+1, 2))
        if all((d - h) in allowed for h, d in zip(heights, targets)):
            return steps
        else:
            return -1


    # ======================= #

    if __name__ == "__main__":
        T = int(input())
        for _ in range(T):
            print(lebamboo())


if __name__ == "__main__":
    solve()

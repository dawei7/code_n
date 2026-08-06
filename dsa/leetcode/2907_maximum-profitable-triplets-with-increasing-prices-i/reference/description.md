## Description

A store has $n$ items. Two 0-indexed arrays describe them: item $i$ has price `prices[i]` and yields profit `profits[i]`.

Choose exactly three items at indices $i<j<k$. Their prices must also be strictly increasing, so `prices[i] < prices[j] < prices[k]`. The value of a valid choice is `profits[i] + profits[j] + profits[k]`. Return the largest value obtainable from any valid triplet, or return `-1` when no three items meet both the index and price conditions.

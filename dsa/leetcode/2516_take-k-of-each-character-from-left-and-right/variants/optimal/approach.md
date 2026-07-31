## General

Any sequence of removals from the two ends takes some prefix and some suffix of `s`. The characters not taken therefore form one contiguous middle substring. Minimizing the number taken is equivalent to maximizing the length of that middle substring.

Count the total occurrences of `'a'`, `'b'`, and `'c'` first. If any total is smaller than `k`, no selection of ends can meet the requirement, so the answer is `-1`. Otherwise, if a character occurs `total[x]` times, the middle may retain at most `total[x] - k` copies of it. Keeping more would leave fewer than `k` copies outside the middle.

Use a sliding window for the middle substring. Extend its right edge one character at a time and maintain the three counts inside it. Only the newly added character can make the window invalid; while its count exceeds its allowed limit, move the left edge forward and remove those characters from the window counts. After this repair, the window obeys all three limits, so record its length.

The longest recorded window is feasible to leave untouched: every character count outside it is at least `k`. Conversely, every valid choice of a prefix and suffix leaves a middle window obeying the same limits, and the sliding-window scan considers its right edge and retains a window at least as long. Thus subtracting the maximum feasible middle length from $n$ gives the minimum number of taken characters.

## Complexity detail

Let $n$ be the length of `s`. The initial count and the right-edge scan each take $O(n)$ time. The left edge advances at most $n$ times in total, so the complete algorithm is $O(n)$ rather than $O(n^2)$. The two three-entry count arrays and a constant number of indices use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every kept substring:** Checking all possible middle intervals directly is correct but takes $O(n^2)$ time, which is too slow for $n$ up to $10^5$.
- **Prefix counts plus binary search:** Prefix counts can test an interval quickly, and a monotone search can find a feasible length, but this is more complicated and typically costs $O(n \log n)$ time.
- If `k` is zero, the whole string is a valid middle window and the answer is `0`.
- If any character occurs fewer than `k` times, the answer is `-1` before the window scan begins.
- The optimal selection may use only one end; representing the untouched portion as a middle window includes empty prefixes or suffixes automatically.

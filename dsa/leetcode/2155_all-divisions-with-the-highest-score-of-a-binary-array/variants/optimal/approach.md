## General

**Start at the division before the array**

At division `0`, the left part is empty, so the score is exactly the total
number of ones in `nums`. Record that division as the first best candidate.

**Move one element across the boundary**

Advance the division from $i$ to $i+1$ by moving `nums[i]` from the right part
to the left part. If that value is `0`, the left-zero count grows and the score
increases by one. If it is `1`, the right-one count shrinks and the score
decreases by one. Thus every next score follows from the previous score in
constant time.

When a score exceeds the best seen so far, discard the earlier indices and
start a new result list with the current division. When it equals the best,
append the current division. Since every division from `0` through $n$ is
visited once, the result contains exactly all maximum-scoring indices.

## Complexity detail

Let $n$ be the length of `nums`. Counting the initial ones and scanning all
$n$ elements take $O(n)$ time. The returned list can contain $n+1$ indices, so
the total output-inclusive space is $O(n)$; the algorithm uses $O(1)$ auxiliary
state beyond that output.

## Alternatives and edge cases

- **Recount every division:** Counting left zeros and right ones independently
  for all $n+1$ boundaries is correct but takes $O(n^2)$ time.
- **Prefix and suffix arrays:** Precomputing both counts also gives $O(n)$ time,
  but consumes $O(n)$ auxiliary space that the running update avoids.
- Division `0` and division $n$ are valid and must both be evaluated.
- An all-zero array has its unique best division at $n$.
- An all-one array has its unique best division at `0`.
- Several nonadjacent divisions may tie, so do not stop after finding one
  maximum.

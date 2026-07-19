## General
**Find every maximal odd palindrome**

Use Manacher's algorithm to compute `radius[center]`, the number of positions
from the center through one endpoint of the longest odd palindrome at that
center. Its full length is `2 * radius[center] - 1`. The algorithm reuses the
mirror radius inside the rightmost palindrome already discovered, then
expands only beyond that known boundary. Across the entire string, boundary
expansions take linear time.

**Record the best palindrome around every split**

For each center's maximal palindrome, record its length at its exact start and
end. Shrinking a palindrome by removing both endpoints gives another odd
palindrome, so a backward pass propagates an ending length two positions
shorter to the preceding endpoint. A forward maximum pass then makes
`ending[i]` the longest palindrome ending at or before `i`.

Apply the symmetric propagation to build `starting[i]`, the longest palindrome
starting at or after `i`. Every pair of non-overlapping substrings is separated
by some split between `i` and `i + 1`. Multiplying `ending[i]` by
`starting[i + 1]` gives the best pair crossing that split; taking the maximum
over all splits therefore considers an optimal pair and never combines
intersecting substrings.

## Complexity detail
Manacher's scan, both endpoint-propagation passes, and the final split scan are
all linear in $N$, giving $O(N)$ time. The radius, ending, and starting arrays
each contain $N$ integers, so the auxiliary space is $O(N)$.

## Alternatives and edge cases
- **Expand around every center independently:** This directly enumerates all
  odd palindromes and is easy to verify, but a uniform string requires
  $O(N^2)$ expansions.
- **Rolling hashes with binary search:** Forward and reverse hashes can test
  palindrome radii in $O(\log N)$ per center, giving $O(N\log N)$ time with
  collision considerations unless multiple robust moduli are used.
- Even-length palindromes do not qualify, even when they are longer than every
  odd palindrome nearby.
- A one-character substring is an odd palindrome, so every valid input of
  length at least two has a feasible product.
- The two chosen substrings may touch at a split, but their index ranges may
  not overlap.

## General
**Flip the main diagonal**

Build an output character for every index $i$ from `0` through `N - 1`.
Inspect the character `nums[i][i]`: write `1` when that diagonal character is
`0`, and write `0` when it is `1`.

This construction is always defined because the array has $N$ rows and each
row has length $N$. It also produces exactly $N$ binary characters.

**Why the constructed string is absent**

Compare the result with input row `nums[i]`. At position $i$, the result
contains the complement of `nums[i][i]`, so the two strings differ at that
position. This argument applies independently to every input row. The result
therefore differs from all $N$ supplied strings and must be a valid missing
binary string.

The construction is a finite form of Cantor's diagonal argument: rather than
searching the much larger space of $2^N$ candidates, it certifies one new
string through one deliberate mismatch per listed row.

## Complexity detail
The algorithm reads one diagonal character and writes one output character
for each of the $N$ rows, taking $O(N)$ time. The returned string contains
$N$ characters and therefore uses $O(N)$ space; aside from that output, only
constant auxiliary state is required.

## Alternatives and edge cases
- **Enumerate binary values:** Store the inputs and test candidates from zero
  upward. This is correct, but may inspect many candidates and does not exploit
  the square input structure.
- **Backtracking:** Generate bits until finding an absent leaf. It can explore
  an exponential candidate tree even though a direct construction exists.
- **Random generation:** Repeated trials eventually may find a missing value,
  but provide neither deterministic time nor a direct correctness guarantee.
- For `N = 1`, complementing the sole input bit returns the only other binary
  string.
- Input order may change which diagonal answer is produced, but every produced
  answer remains valid.
- The result must have exactly $N$ characters and contain no character other
  than `0` or `1`.
- Returning any absent string is correct; matching one illustrative example is
  not required.

## General
**Compare long decimal substrings without converting them**

Two leading-zero-free positive integers are ordered first by length. Only
equal-length candidates require lexicographic comparison. Build an LCP table
where `lcp[i][j]` is the length of the longest common prefix of the suffixes
starting at indices `i` and `j`. It satisfies
`lcp[i][j] = 1 + lcp[i + 1][j + 1]` when the two current digits match.

For equal-length substrings, inspect their LCP length. If it covers the whole
number, the values are equal. Otherwise, the first unequal digits determine
their order in constant time.

**Count partitions by the final number's length**

Let `prefix[end][length]` be the cumulative number of valid partitions of
`num[:end]` whose final number has length at most `length`. For a proposed
final substring `num[start:end]` of length `length`, reject it immediately if
`num[start] == "0"`.

If `start == 0`, that substring alone contributes one partition. Otherwise,
every previous number shorter than `length` is automatically smaller; their
combined count is available from
`prefix[start][min(length - 1, start)]`. A previous number of the same length
is also allowed when the LCP comparison shows
`num[start - length:start] <= num[start:end]`. Its exact count is the
difference between two adjacent cumulative entries.

Add these contributions, then accumulate them into the current prefix row.
The final entry `prefix[N][N]` sums every valid possible last length.

**Why the recurrence neither misses nor duplicates a list**

Every valid partition has a unique final substring and a unique preceding
partition. The recurrence considers that final length, rejects precisely the
leading-zero and decreasing cases, and inherits the exact count of all valid
predecessors. Conversely, every counted predecessor followed by its permitted
final substring remains non-decreasing and consumes the digits exactly once.
Thus the recurrence establishes a one-to-one correspondence with valid lists.

## Complexity detail
The upper triangle of the LCP table contains $O(N^2)$ entries and is filled in
constant time per entry. The DP examines $O(N^2)$ pairs of prefix end and final
length; cumulative counts and LCP queries make each transition constant time.
Total time is $O(N^2)$. Both tables contain $O(N^2)$ compact integer entries,
so space is $O(N^2)$.

## Alternatives and edge cases
- **Direct equal-length comparison:** Scan the two digit substrings during
  every DP transition. Repeated equal prefixes can raise the running time to
  $O(N^3)$.
- **Convert substrings to integers:** Arbitrary-length conversion is repeated
  work, creates large values, and does not meet the intended quadratic bound.
- **Backtracking over separators:** It explores exponentially many partitions
  before recognizing repeated prefix states.
- If the complete string begins with `0`, no first positive integer is valid,
  so the answer is zero.
- Zeros may occur inside a number, but no selected number may start with one.
- Equal consecutive values are allowed because the list is non-decreasing,
  not strictly increasing.
- A partition containing only the full string is valid whenever its first
  digit is nonzero.

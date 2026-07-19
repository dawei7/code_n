## General
**Count valid strings by their final bit**

Maintain `ending_zero` and `ending_one`, the numbers of distinct good strings
that start with `1` and currently end with `0` or `1`. The exceptional
one-character string `"0"` is excluded from these two counts and tracked by a
separate `has_zero` flag.

**Update the class matching the current bit**

When the next character is `1`, append it to every previously counted string
and also start the new string `"1"`. These produce
`ending_zero + ending_one + 1` distinct strings ending in `1`. Replace
`ending_one` with that total.

Replacement, rather than addition to the old total, removes duplication:
every old string ending in `1` is reproduced by choosing this later `1`, while
the new recurrence already includes one canonical occurrence of every possible
result.

When the next character is `0`, append it to every string that already starts
with `1`. This produces `ending_zero + ending_one` distinct multi-character
good strings ending in `0`, so replace `ending_zero` with that total. Also set
`has_zero` because `"0"` itself is good, but no longer string starting at that
zero is allowed.

**Combine the disjoint result classes**

After the scan, strings ending in `0`, strings ending in `1`, and the standalone
`"0"` are disjoint. Their sum therefore counts every unique good subsequence
exactly once. Reducing each update and the final sum modulo $10^9 + 7$ preserves
the requested result.

## Complexity detail
Each of the $N$ input bits triggers a constant number of arithmetic operations,
so the time complexity is $O(N)$. The two counts, the zero flag, and the fixed
modulus occupy $O(1)$ space regardless of input length.

## Alternatives and edge cases
- **Enumerate all index subsets:** Generate each of the $2^N-1$ nonempty
  subsequences and insert valid results into a set. This is correct but
  exponential and stores potentially exponentially many strings.
- **General distinct-subsequence DP:** Track last occurrences and count all
  distinct subsequences, then separately exclude every leading-zero result.
  The binary-specific ending-state recurrence is simpler and constant-space.
- A string containing only zeros has exactly one unique good subsequence:
  `"0"`.
- A string containing only $N$ ones has exactly $N$ unique good subsequences,
  with lengths from one through $N$.
- Multiple zero positions still contribute only one standalone `"0"`.
- `"01"` and every longer string beginning with `0` remain invalid even though
  `"0"` alone is allowed.
- Modular reduction is necessary during the scan because the unreduced number
  of distinct subsequences can grow exponentially.

## General

**Turn partitioning into a minimum-cost suffix problem**

At any position `i`, a valid partition must choose one beautiful prefix of the remaining suffix and then optimally partition what follows. The exact solution expresses this with `dfs(i)`:

`dfs(i)` is the minimum number of beautiful substrings needed to partition `s[i:]`.

The answer for the complete string is `dfs(0)`. Memoization through `@cache` ensures that each suffix index is solved once even when several earlier cuts lead to it.

**Represent impossible states with infinity**

When `i >= n`, the suffix is empty. It requires zero additional pieces, so the base case returns zero. This makes a beautiful piece ending at the final character contribute `1 + dfs(n) = 1`.

If `s[i] == "0"`, no valid piece can begin there because beautiful binary strings may not have leading zeros. The state returns `inf` immediately.

`inf` is also the initial answer for a nonempty state. A finite candidate replaces it only when a beautiful prefix leads to a partitionable remainder. Arithmetic is convenient: `1 + inf` remains infinite, so an impossible suffix can never win a `min` comparison.

At the end, the outer function converts an infinite result to `-1`, which is the public contract's impossible marker.

**Precompute the values that count as beautiful**

A substring is beautiful exactly when its binary value is a power of five and it has no leading zero. The code builds set `ss` starting with 1, which is `5^0`. It then multiplies by five `n` times and adds each result.

This generates `1, 5, 25, 125, ...` through `5^n`. It includes more large powers than a length-`n` binary substring can represent, but only `O(n)` of them, and membership tests remain constant expected time. Most importantly, every relevant power is present. A binary substring of at most `n` bits cannot equal a missing power beyond this generated range.

Including 1 matters: the one-character string `"1"` is the binary representation of `5^0` and is a legal beautiful piece.

**Decode candidate prefixes incrementally**

For a valid start `i`, the loop extends the endpoint `j` from `i` through `n - 1`. Variable `x` stores the integer value of `s[i:j + 1]`.

The update

`x = x << 1 | int(s[j])`

is the standard way to append one binary digit. Shifting left multiplies the old value by two, and bitwise OR adds the new bit, which is either zero or one. Thus the code does not repeatedly slice the string and convert each candidate from scratch.

After every appended bit, membership `x in ss` decides whether this prefix is a power of five. If it is, the code considers cutting after `j` and forms candidate `1 + dfs(j + 1)`. Taking the minimum across all beautiful prefixes chooses the fewest total pieces.

**A walkthrough with `"1011"`**

At index zero, incremental values are 1 for `"1"`, 2 for `"10"`, 5 for `"101"`, and 11 for `"1011"`. Values 1 and 5 are powers of five.

Choosing `"1"` leaves suffix `"011"`, whose first character is zero, so that branch is impossible. Choosing `"101"` leaves `"1"`. The latter is beautiful and reaches the empty base case, giving two pieces total. No one-piece candidate exists because 11 is not a power of five, so `dfs(0)` returns two.

**Why memoization changes exponential search into dynamic programming**

Without caching, a suffix such as `s[q:]` might be solved repeatedly from many different earlier cuts. The recursion tree could branch at every beautiful prefix. With `@cache`, the first call computes a state and later calls reuse the stored result. There are only `n + 1` possible indices.

This is top-down dynamic programming over a directed acyclic graph of positions. A beautiful substring from `i` through `j` is an edge from position `i` to `j + 1` with cost one. The task is the minimum number of edges from zero to `n`. All edges move right, so recursion cannot cycle.

**Why the minimum is correct**

Consider any suffix starting at `i`. Every legal partition has some first piece `s[i:j + 1]`. The loop enumerates every possible `j` and recognizes that piece precisely when its incrementally decoded value is in the power-of-five set; the leading-zero guard enforces the remaining beauty rule. For each legal first piece, `dfs(j + 1)` gives the optimal number of pieces for the remainder by the state definition.

Therefore `1 + dfs(j + 1)` is the best partition using that first cut, and the minimum over all such cuts is the best partition of `s[i:]`. The empty base case anchors this argument. By induction from later suffixes to earlier ones, `dfs(0)` is the global minimum.

## Complexity detail

Let `n` be `s.length`. There are `O(n)` memoized suffix states. State `i` scans at most `n - i` endpoints, and the total number of state-endpoint pairs is

$$
\sum_{i=0}^{n-1}(n-i) = O(n^2).
$$

With the problem's maximum of fifteen bits, shifts, integer conversion, set lookup, and cached lookup are constant-time. The total time is `O(n^2)`. The power-set construction costs `O(n)` and is dominated.

The cache stores one result for each suffix, the power set stores `O(n)` integers, and recursion reaches depth at most `n`. Auxiliary space is `O(n)`. Incremental decoding avoids allocating `O(n^2)` total substring objects.

For arbitrary unbounded `n`, Python big-integer operations would have a bit-length cost, but the tiny stated bound and conventional problem model justify the manifest's `O(n^2)` time.

## Alternatives and edge cases

- **Bottom-up prefix dynamic programming:** Store the minimum pieces for each prefix and extend beautiful substrings forward. It has the same `O(n^2)` time and `O(n)` space without recursion.
- **Backtracking without memoization:** It explores the same cuts but can repeat suffix work exponentially.
- **Precompute beautiful binary strings:** Generate powers of five, convert them to binary strings, and match them at each position. This is valid; the exact solution instead decodes candidates to integers.
- **Repeated slicing and base-two conversion:** It is simpler syntactically but recreates overlapping strings. Shift-and-add reuses the previous candidate value.
- **String begins with zero:** `dfs(0)` is immediately impossible, so the final answer is `-1`.
- **Zero appears after a cut:** Any recursive state beginning there is impossible; zero may still occur inside a longer beautiful binary representation.
- **Single `"1"`:** It represents `5^0`, reaches the empty suffix, and returns one.
- **Single `"0"`:** Leading-zero rejection returns `-1`.
- **Whole string is beautiful:** The loop considers the final endpoint and can return one, which no partition can improve.
- **Several valid partitions:** `min` selects the one with the fewest pieces rather than the earliest or longest first piece automatically.
- **Impossible remainder:** Its `inf` result prevents that candidate cut from being selected.
- **Extra generated powers:** Values larger than any possible substring never match and cost only linear set storage.

## General

**Turn repeated substrings into common suffixes**

A repeated substring appears at two distinct starting positions. Equivalently, it ends at two distinct ending positions and the characters immediately before those endpoints match for the substring's entire length.

The exact solution compares every pair of endpoints and records how long their equal character run extends backward. This is the same recurrence used for longest common substring, except both compared sequences are positions in the same string.

Define `f[i][j]` for `j < i` as the length of the longest equal substrings that end exactly at indices `i` and `j`. In other words, it is the length of the longest common suffix of `s[:i + 1]` and `s[:j + 1]`.

Only pairs with `j < i` are needed. They represent distinct endpoints and avoid computing both symmetric cells `f[i][j]` and `f[j][i]`.

**Allocate the endpoint-pair table**

The code begins with:

```python
n = len(s)
f = [[0] * n for _ in range(n)]
ans = 0
```

Every cell starts at zero. Zero is correct when the two endpoint characters differ, because no nonempty equal substring can end at both positions.

`ans` stores the greatest common-suffix length found anywhere. It begins at zero, which is also the required result when no character repeats.

The list comprehension creates `n` independent rows. Using `[[0] * n] * n` instead would alias every row to the same list and corrupt unrelated cells when one cell changes.

**Compare each distinct pair of endpoints**

The nested loops are:

```python
for i in range(1, n):
    for j in range(i):
```

`i` starts at one because index zero has no earlier endpoint to compare with. For each `i`, `j` ranges from zero through `i - 1`. Across the loops, every unordered pair of distinct positions is considered exactly once, with the later endpoint named `i`.

If the endpoint characters differ, `f[i][j]` remains its initialized zero. If they match, the common suffix has at least length one and may extend the common suffix ending one position earlier:

```python
if s[i] == s[j]:
    f[i][j] = 1 + (f[i - 1][j - 1] if j else 0)
```

For `j > 0`, both endpoints have predecessors. If those preceding suffixes match for `f[i - 1][j - 1]` characters, adding the equal current characters extends that run by one.

If `j == 0`, there is no earlier character before the second endpoint. The common suffix can only contain the matching character at index zero, so the previous length is treated as zero and the new cell becomes one.

The explicit `if j else 0` is also important in Python because `j - 1` would be minus one at `j == 0`, and negative indexing would incorrectly read the last column rather than representing an absent predecessor.

**A concrete table trace**

Consider `s = "abbaba"`.

When `i = 3` and `j = 0`, both characters are `"a"`. Because `j` is zero, `f[3][0]` becomes one. This represents the repeated one-character substring `"a"`.

When `i = 4` and `j = 1`, both characters are `"b"`. The previous diagonal cell `f[3][0]` is one, so `f[4][1]` becomes two. This represents `"ab"` ending at indices four and one.

If the next preceding characters do not continue to match, another cell's diagonal chain stops at zero. The table therefore records contiguous equality only. It never joins matching characters across a gap, so it finds substrings rather than subsequences.

**Update the global maximum**

After writing a matching cell, the solution runs:

```python
ans = max(ans, f[i][j])
```

Every nonempty repeated substring has two occurrences with distinct end indices. When the loops reach that pair, the cell contains at least the substring's length. Conversely, every positive cell represents equal contiguous substrings ending at two distinct positions. Taking the maximum over all cells therefore yields exactly the longest repeating-substring length.

The update occurs only in the matching branch because mismatching cells are zero and cannot improve a non-negative maximum.

**Why overlapping occurrences are allowed and handled**

The problem requires distinct starting positions, not disjoint occurrences. A repeated substring may overlap itself. For `s = "aaa"`, `"aa"` occurs starting at indices zero and one.

The DP allows this. Cell `f[2][1]` uses `f[1][0]` and becomes two. Nothing in the recurrence requires the two ranges to be disjoint.

This behavior is correct for the stated definition. Adding a restriction such as `f[i][j] <= i - j` would solve a different problem that demands non-overlapping repetitions.

**Why the recurrence is exact**

If `s[i] != s[j]`, equal substrings ending at both indices cannot contain even their final character, so the correct length is zero.

If `s[i] == s[j]`, any equal substrings ending there consist of an equal suffix ending at `i - 1` and `j - 1`, followed by the common current character. The longest such suffix has length `f[i - 1][j - 1]`, so the new longest length is exactly one more. The `j == 0` base case correctly limits it to one.

The loops process increasing `i`, so the previous row is complete before any cell needs it. Thus every cell receives its mathematically defined value, and `ans` receives the maximum of all valid repeated substrings.

**Return only the required length**

The final line returns `ans`. The table does not store the substring text or starting positions because the problem asks only for a length.

A one-character string executes neither loop, leaving `ans` at zero. That is correct because a substring cannot occur at two distinct starting positions in a length-one input.

## Complexity detail

Let `N` be the length of `s`.

The loops process one cell for every pair `j < i`. There are `N(N - 1) / 2` such pairs, and each update is constant time. The exact running time is therefore `O(N^2)`.

The table contains `N^2` integer cells, so the exact auxiliary-space complexity is `O(N^2)`. Only the previous DP row is required by the recurrence, so a carefully ordered rolling-row implementation could reduce space to `O(N)` while retaining `O(N^2)` time. The protected source intentionally stores the full table.

The manifest records `O(N log N)` time and `O(N)` space. Those bounds do not describe this exact DP implementation. They correspond to a more advanced length search, typically binary search combined with rolling hashes, or to a suitably implemented suffix-array technique.

For the binary-search version, the predicate asks whether any substring of length `L` repeats. If length `L` repeats, every shorter length also repeats, making the predicate monotonic. Rolling hashes let all length-`L` windows be checked in `O(N)` expected time, and binary search performs `O(log N)` checks. Hash collisions must be prevented with verification or made negligibly unlikely with robust hashing. Stored window hashes use `O(N)` space.

The exact table is deterministic and conceptually direct, but its honest bounds are quadratic rather than the manifest target.

## Alternatives and edge cases

- **Binary search plus rolling hash for the manifest target:** Check duplicate windows of a candidate length in linear expected time and binary-search the largest successful length. Verify hash matches if deterministic correctness is required.
- **Suffix array and longest-common-prefix array:** Repeated substrings are common prefixes of different suffixes. A suffix array with efficient construction plus an LCP scan can meet `O(N log N)` time and `O(N)` space.
- **Suffix automaton:** Building a suffix automaton and propagating occurrence counts can find the longest state represented at least twice in linear time and space, but it is significantly more advanced.
- **Rolling two DP rows:** Since `f[i][j]` reads only the preceding row, keep two length-`N` rows. This reduces the exact DP space to `O(N)` without changing its `O(N^2)` time.
- **Descending length with a set:** Test every substring length and store sliced substrings. In Python, substring copying can make the worst-case time cubic and space much larger.
- **One character:** There are no two distinct starts, so the loops leave the answer at zero.
- **All characters distinct:** Every comparison fails, every DP cell stays zero, and the function returns zero.
- **All characters equal:** The longest repeated substring has length `N - 1` using starts zero and one. The last relevant diagonal chain reaches that value.
- **Overlapping repetitions:** They are valid and naturally counted, as in two occurrences of `"aa"` inside `"aaa"`.
- **Three or more occurrences:** Only one pair is needed to establish repetition. Considering all endpoint pairs still finds the same maximum length.
- **Equal suffix reaching index zero:** The `j == 0` branch starts the diagonal chain at one and avoids accidental negative indexing.
- **Substring versus subsequence:** Only diagonal predecessor cells extend a match. A character mismatch resets the cell to zero, preserving contiguity.
- **Lowercase alphabet:** The DP compares characters directly and does not depend on alphabet size or special encoding.
- **Input preservation:** Strings are immutable, and the algorithm creates only its separate numeric table.

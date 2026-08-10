## General

**Why ordinary center expansion can repeat quadratic work**

Every palindrome mirrors around a center. An odd-length palindrome has a character at its center; an even-length palindrome has a gap between two characters. Expanding outward from all $2n-1$ possible centers is easy to understand, but a string such as `"aaaa...a"` makes many centers recheck the same character pairs, producing $O(n^2)$ time.

Manacher's algorithm keeps the center-expansion idea but reuses information from a palindrome already known to reach farthest to the right. Symmetry supplies a safe initial radius for many later centers. New comparisons are needed only when a candidate may extend beyond the known boundary, which reduces total work to linear time.

The selected `Solution` class implements Manacher's algorithm. The later `Solution2` class is a quadratic expand-around-center alternative and is not the platform entry point.

**Transform the string so every palindrome has one character center**

Odd and even palindromes otherwise need separate center types. `preProcess` inserts `#` between every pair of original characters and at both ends. It also adds distinct sentinels:

```text
^ # s[0] # s[1] # ... # s[n-1] # $
```

For example:

```text
s = "cbbd"
T = ^ # c # b # b # d # $
```

An odd original palindrome remains centered on an original character. An even original palindrome becomes odd-length in `T`, centered on a `#`. The expansion loop can now treat both cases identically.

The `^` and `$` sentinels are different from each other and, under the digit-and-English-letter input contract, different from every real character. Expansion must encounter a mismatch at a sentinel before an index can leave the list. This removes explicit boundary checks from the inner loop.

For an empty string, `preProcess` returns only `['^', '$']`. The Reference guarantees a non-empty input, but the helper still has a defined representation for the empty case.

**What each radius means**

`P[i]` is the maximum number of transformed positions that match symmetrically around center `i`. More precisely, after it is finalized,

$$
T[i-d] = T[i+d]
$$

for every $1 \le d \le P[i]$, and the next outward pair differs.

Because transformed characters alternate between separators and original characters, the numeric radius `P[i]` also equals the length of the corresponding palindrome in the original string. For the even palindrome `"bb"`, the center is the separator between the two `b` characters and its transformed radius is `2`; the original length is also `2`. For `"bab"`, the transformed radius is `3` and the original length is `3`.

**Track the palindrome with the farthest known right boundary**

The variables `center` and `right` describe the palindrome discovered so far whose rightmost matched transformed index is farthest right:

$$
\texttt{right} = \texttt{center} + P[\texttt{center}].
$$

`right` is the index of the matched boundary, not one past it. The algorithm scans candidate centers `i` from `1` through `len(T) - 2`, excluding the sentinels.

The mirror of `i` across `center` is

$$
i_{mirror} = 2 \cdot \texttt{center} - i.
$$

If `i < right`, then `i` lies inside the known palindrome. Characters around `i` correspond symmetrically to characters around `i_mirror`. The algorithm can reuse the mirror's radius rather than comparing those inner pairs again.

**Why the mirrored radius must be clipped**

The initialization is

```python
P[i] = min(right - i, P[i_mirror])
```

when `i` is inside the right boundary.

Two limits are involved:

- `P[i_mirror]` is how far the mirrored palindrome is known to extend;
- `right - i` is how much room remains before reaching the boundary of the containing palindrome.

If the mirrored palindrome fits entirely inside the containing palindrome, its full radius transfers to `i`. If it crosses the containing palindrome's left boundary, symmetry guarantees matches only up to the corresponding right boundary. Values beyond `right` have not yet been compared, so copying a larger radius would make an unsupported assumption.

When `i >= right`, no reusable contained region exists and `P[i]` starts at zero.

**Expand only from the trusted initial radius**

After initialization, the loop compares the next outward pair:

```python
while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
    P[i] += 1
```

All positions within the current radius are already known to match. The loop begins just outside that radius and increases it one step for every new match. It stops on the first mismatch. Sentinels guarantee safe termination.

If the resulting palindrome extends past the farthest known boundary, the algorithm updates

```python
center, right = i, i + P[i]
```

This new palindrome provides the symmetry information for future centers.

**See the even palindrome in `"cbbd"`**

In

```text
^ # c # b # b # d # $
0 1 2 3 4 5 6 7 8 9 10
```

the gap between the two `b` characters is transformed index `5`.

- The first comparison around `5` is `T[6] == T[4]`, or `b == b`, so the radius becomes `1`.
- The second comparison is `T[7] == T[3]`, or `# == #`, so the radius becomes `2`.
- The next comparison is `T[8] == T[2]`, or `d == c`, so expansion stops.

Thus `P[5] = 2`, representing the original palindrome `"bb"` of length `2`.

**Convert the winning transformed center back to the source string**

After all radii are known, the second loop selects an index `max_i` with the greatest `P[i]`. It updates only on a strict increase, so ties retain the first maximum center encountered from left to right. Any longest palindrome is acceptable.

The leftmost transformed position of the winning palindrome is `max_i - P[max_i]`. Accounting for the leading sentinel and ignoring separators gives the original start formula used by the code:

```python
start = (max_i - 1 - P[max_i]) // 2
```

The original length is `P[max_i]`, so the answer is

```python
s[start:start + P[max_i]]
```

For `"cbbd"`, `max_i = 5` and `P[max_i] = 2`, giving `start = (5 - 1 - 2) // 2 = 1` and the slice `s[1:3] = "bb"`.

**Why symmetry reuse still produces exact radii**

The copied radius never claims more than symmetry proves: it is limited by both the mirror radius and the known right boundary. The subsequent expansion tests every pair beyond that safe region until the first mismatch, so each final `P[i]` is neither too small nor too large.

Every original palindrome corresponds to a center in the transformed list and therefore to one computed radius. Selecting the maximum radius selects a maximum original palindrome length, and the index conversion returns exactly that contiguous substring.

## Complexity detail

Let $n$ be `len(s)` and $N = 2n+3$ be `len(T)` for a non-empty input.

- **Time complexity: $O(n)$.** Preprocessing creates $O(n)$ transformed entries. The outer center loop has $O(N)$ iterations. Mirror initialization avoids rechecking pairs wholly inside the known rightmost palindrome. When expansion succeeds beyond that boundary, `right` advances; it can advance at most $N$ positions over the entire run. Contained mirror cases either require no successful new expansion or lead to boundary growth. The final maximum scan is another $O(N)$ pass. Since $N=O(n)$, total time is $O(n)$.
- **Space complexity: $O(n)$.** The transformed list `T` and radius list `P` each contain $O(n)$ entries. All centers, boundaries, indices, and temporary values use constant additional space. The returned slice has at most $n$ characters.

The later `Solution2` class has $O(n^2)$ time and $O(1)$ auxiliary space, but it is not used when LeetCode instantiates the primary class named `Solution`.

## Alternatives and edge cases

- **Expand around every center:** This is much easier to derive and uses $O(1)$ auxiliary space, but it can perform $O(n)$ work at each of $O(n)$ centers. `Solution2` demonstrates that quadratic alternative.
- **Dynamic programming:** Store whether every interval is palindromic using matching endpoints and a known inner interval. It takes $O(n^2)$ time and $O(n^2)$ space and is simpler than mirror-radius reuse.
- **Check all substrings:** Independent palindrome checks can reach $O(n^3)$ time because both the number of ranges and the check length grow with $n$.
- **Separate odd/even Manacher arrays:** Manacher's algorithm can be written directly on the original string with separate radius definitions for odd and even centers. It avoids the transformed list but introduces two sets of boundary formulas. Separators trade a little memory for one uniform loop.
- **Single character:** Its transformed center obtains radius `1`, and the conversion returns the character.
- **Even-length answer:** A separator acts as the center, as in `"bb"`; no special expansion branch is required.
- **Odd-length answer:** An original character acts as the center, as in `"racecar"`.
- **All characters equal:** Radii become large at many centers, but mirror reuse keeps the total work linear rather than repeating full expansions.
- **Several longest palindromes:** The strict maximum update retains the leftmost transformed center with maximum radius. The contract permits any longest result.
- **Sentinel safety:** `^` and `$` cannot occur under the digit-and-English-letter contract. They differ from each other, so expansion always stops before leaving `T`.
- **Separator safety:** `#` also lies outside the legal input alphabet. Treating it only as a structural separator cannot confuse it with a real character.
- **Empty string robustness:** Although the Reference requires at least one character, `preProcess` returns two sentinels and the remaining logic returns an empty slice.
- **Exact character comparison:** Digits, uppercase letters, and lowercase letters are compared without normalization; palindrome identity is case-sensitive.
- **Input preservation:** `T` and `P` are new lists. The original string is read but never changed.

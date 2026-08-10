## General

**Use globally insufficient characters as mandatory cut points**

Consider one current interval `s[l:r + 1]`. Count every character in that interval. If a character `c` occurs fewer than `k` times in the entire interval, then no valid substring contained inside this interval can include `c`.

The reason is decisive: a smaller substring cannot contain more copies of `c` than the whole interval. If the whole interval supplies fewer than `k`, any candidate containing even one `c` would have a positive frequency below `k`, violating the rule.

Therefore every occurrence of such a character is a barrier. A valid answer must lie completely between consecutive barriers. The exact solution chooses one insufficient character, splits around all of its occurrences, recursively solves every resulting segment, and returns the greatest segment answer.

This is divide and conquer based on an impossibility proof, not an arbitrary midpoint split.

**What one recursive call represents**

`dfs(l, r)` returns the maximum valid-substring length entirely within the inclusive interval from `l` through `r`.

It constructs `Counter(s[l : r + 1])`, obtaining the frequencies for that interval. The slicing notation includes `r` because its upper bound is `r + 1`.

Then it evaluates

```text
split = next((c for c, v in cnt.items() if v < k), '')
```

This picks one character whose interval frequency is below `k`. The empty string is used when no such character exists. Since the real input contains only lowercase letters, `''` cannot be confused with a valid character.

The chosen character need not be the rarest, and it need not appear at the middle. Any character with frequency below `k` has the required barrier property.

**When the entire interval is already valid**

If `split` is empty, every distinct character present in the interval occurs at least `k` times. That is exactly the validity condition for the whole interval.

No contained substring can be longer than the interval itself, so the best answer for this call is immediately `r - l + 1`. There is no reason to split or test smaller substrings.

This is the successful base case of the recursion. The other form of termination occurs when segments become too small or consist only of insufficient characters; repeated splitting then produces no candidate and returns zero.

**Scanning all segments between split characters**

Once `split` is known, `i` starts at `l`. The first inner loop skips any run of barrier characters:

```text
while i <= r and s[i] == split:
    i += 1
```

After skipping, `i` is either beyond the interval or at the first character of a candidate segment.

The second pointer `j` advances until it reaches the next occurrence of `split` or passes `r`:

```text
while j <= r and s[j] != split:
    j += 1
```

Thus `s[i:j]`, equivalently inclusive interval `[i, j - 1]`, is one maximal segment containing no chosen barrier character. The method recursively evaluates `dfs(i, j - 1)`, compares it with `ans`, and sets `i = j` to continue from the barrier just found.

Every possible valid substring is contained in exactly one of these maximal segments, so taking the maximum recursive result loses nothing.

**Why splitting on only one bad character is enough per call**

An interval may contain several characters with frequency below `k`. The method picks only one now. That still preserves correctness because removing the chosen character partitions the search space without discarding any possible answer.

Inside each child segment, frequencies are counted again. Another insufficient character may then be selected and used for the next split. Repeating this process eventually either finds an interval where all present characters meet the threshold or removes every possible region.

Choosing all bad characters at once could reduce recursion, but is not necessary. The one-character-at-a-time proof is simple and the lowercase alphabet bounds how many distinct split characters can appear along one recursion path.

**Tracing `s = "aaabb"`, `k = 3`**

The initial counter is `a: 3`, `b: 2`. Character `b` is insufficient, so no valid substring can include a `b`.

Splitting around `b` leaves segment `"aaa"`. Its recursive counter contains `a: 3`, so there is no split character. The entire segment is valid and contributes length three. The trailing `b` occurrences produce no other nonempty useful segment. The root returns `3`.

**Tracing `s = "ababbc"`, `k = 2`**

The full counts are `a: 2`, `b: 3`, and `c: 1`. Character `c` is a mandatory barrier. The segment before it is `"ababb"`; that segment has `a: 2` and `b: 3`, so it is valid in full and returns length five. The final answer is `5`.

This example shows why frequency must be recomputed for each child. Counts relevant to a candidate are counts inside that candidate, not counts in the original entire string.

**The subtle `if i >= r` condition**

After skipping barrier characters, the exact code breaks when `i >= r`. If `i > r`, no segment remains. If `i == r`, one non-barrier character might remain at the final index, but that one-character segment cannot be valid in this branch.

Reaching the splitting branch means some present character has positive frequency below `k`, which implies `k >= 2`. A segment of length one then cannot contain its only character at least `k` times. Skipping that singleton is therefore safe. When `k == 1`, no present character can have frequency below `k`, so the function returns the whole interval before reaching this code.

**Why the recursive result is exact**

If no split character exists, the current interval is valid and is plainly its own longest contained substring.

Otherwise, let `c` be the chosen split character. Any valid substring must exclude `c`, by the insufficient-frequency argument. It therefore lies wholly within one maximal segment between occurrences of `c`. By induction, the recursive call returns the exact best length within each such segment. The maximum over those calls is consequently the exact best length for the current interval.

Applying this reasoning at the initial interval proves the returned value is the longest valid substring of `s`.

## Complexity detail

Let $n$ be the string length and let $\sigma$ be the number of possible distinct characters. Here $\sigma = 26$ because the input uses lowercase English letters.

At one recursion depth, the processed child intervals are disjoint: they come from splitting parent intervals around barrier characters. The total length counted and scanned across that entire level is at most $n$. Along one root-to-leaf path, every split removes at least one distinct character from all descendants on that path, so depth is at most $\sigma$.

The general bound is therefore $O(\sigma n)$ time. With the fixed 26-letter alphabet, this simplifies to $O(n)$, matching the manifest. Python substring slicing also copies characters, but those copied lengths follow the same disjoint-per-level accounting and remain inside $O(\sigma n)$.

The recursion stack depth is $O(\sigma)$. Counters contain at most $\sigma$ keys. Under the fixed alphabet, both are $O(1)$ auxiliary space. If the alphabet were unbounded, the honest bounds would be $O(\sigma n)$ time and $O(\sigma)$ active recursion/counter state, with a possible $O(n^2)$ time when $\sigma$ grows with $n$.

The slice passed to `Counter` is a temporary string. Its largest size is $O(n)$, so under strict Python allocation accounting, peak temporary auxiliary storage can be $O(n)$ even though the algorithmic fixed-alphabet state is constant. An index-counting implementation that iterates directly from `l` to `r` would avoid that slice and realize the stated $O(1)$ auxiliary bound outside recursion.

## Alternatives and edge cases

- **Sliding window by target distinct count:** For each possible number of distinct letters from one through 26, maintain a window with at most that many distinct characters and track how many meet frequency `k`. This gives deterministic $O(26n)=O(n)$ time and $O(1)$ space without recursion or slicing.

- **Enumerate all substrings:** Expanding every start/end pair and maintaining counts costs $O(n^2)$ time. It is simpler but unnecessary because insufficient characters provide strong cut points.

- **Split on every insufficient character at once:** Identify all characters with interval count below `k` and scan maximal runs containing none of them. This can reduce recursive levels while using the same core proof.

- **`k = 1`:** Every nonempty substring satisfies the condition because each present character occurs at least once. The initial call finds no split and returns `len(s)`.

- **`k > len(s)`:** Every present character is insufficient. Repeated splits eventually leave no valid segment, so the answer is zero even without an explicit length precheck.

- **All characters satisfy the threshold:** The whole string is returned immediately, which is necessarily optimal.

- **All characters are insufficient:** Every occurrence acts as a barrier at some recursion level, and no positive-length interval survives as valid.

- **Repeated barrier characters:** The first inner loop skips an entire run so it does not make empty recursive calls between adjacent barriers.

- **A one-character tail after a barrier:** The exact `i >= r` break skips it safely because the splitting branch implies `k >= 2`.

- **Arbitrary `Counter` iteration choice:** Python chooses the first qualifying key in counter iteration order, but correctness and the fixed-alphabet bound do not depend on which insufficient character is selected.

- **Contiguous substring requirement:** Splitting works because a substring cannot jump over a barrier occurrence. A subsequence problem would require different reasoning.

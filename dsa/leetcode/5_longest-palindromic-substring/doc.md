# Longest Palindromic Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 5 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) |

## Problem Description
### Goal
Given a nonempty string `s`, find a contiguous portion that is a palindrome: its character sequence is unchanged when read from right to left instead of left to right. The chosen characters must occupy one uninterrupted interval of the original string.

Return a palindromic substring whose length is as large as possible. More than one interval may attain that maximum, and returning any one of them is valid. A single character is always a palindrome, so every allowed input has at least one answer.

### Function Contract
**Inputs**

- `s`: `str` with at least one character

**Return value**

A `str` containing a longest palindromic substring of `s`.

### Examples
**Example 1**

- Input: `s = "babad"`
- Output: `"bab"`

**Example 2**

- Input: `s = "cbbd"`
- Output: `"bb"`

**Example 3**

- Input: `s = "a"`
- Output: `"a"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Why ordinary center expansion repeats work**

Every palindrome has a center, so expanding once around each character and once around each gap is a natural solution. Its weakness appears when many neighboring centers belong to the same large palindrome. In a string such as `aaaaaaaa`, each center compares most of the same character pairs again, leading to quadratic work.

**Manacher's algorithm** avoids that repetition. It remembers the palindrome that currently reaches farthest to the right and uses its symmetry to initialize radii for centers inside that known region. Direct comparisons are needed only where symmetry cannot already decide the answer.

**Put odd- and even-length palindromes in one representation**

Insert a separator before, between, and after the original characters. For example:

```text
original:     a b b a
transformed: # a # b # b # a #
```

Now every palindrome has an odd number of transformed positions:

- an original character is the center of an odd-length palindrome;
- a separator is the center of an even-length palindrome.

Distinct left and right sentinels can be placed outside this sequence so expansion stops automatically instead of performing a boundary check on every comparison.

Let `radius[i]` be the number of matching transformed positions on either side of center `i`. The radius also equals the length of the corresponding palindrome in the original string. This is why a radius of `2` at the separator between the two `b` characters in `cbbd` represents the original substring `bb`.

**Reuse the rightmost palindrome through its mirror**

Track `center`, the center of the known palindrome that reaches farthest right, and `right`, its exclusive or inclusive right boundary according to the chosen implementation. For a new center `i` strictly inside this palindrome, its mirror across `center` is:

```text
mirror = 2 * center - i
```

The characters around `mirror` appear in reverse order around `i`. However, that information is guaranteed only inside the known right boundary, so the safe initial radius is:

```text
min(radius[mirror], right - i)
```

The minimum is essential. There are three useful cases:

- If the mirrored palindrome ends before the left boundary of the known palindrome, its entire radius transfers to `i`; it cannot suddenly extend farther on one side without contradicting the exact mirrored radius.
- If it reaches exactly to that boundary, all positions up to `right` are known to match, but characters beyond `right` are unknown. Expansion must resume there.
- If it crosses that boundary, only the clipped portion lies in the symmetric region. Copying the full mirrored radius could claim matches that have never been compared.

After this safe initialization, compare outward normally. If the palindrome at `i` passes `right`, make it the new rightmost palindrome by updating `center` and `right`.

**Why the scan is linear rather than merely faster in practice**

A center may begin with a large radius copied from its mirror, but copied positions cost no character comparisons. The comparisons that successfully move beyond the current right boundary permanently advance that boundary. Since `right` moves only forward across a transformed sequence of linear size, those successful boundary-extending comparisons total $O(n)$.

A center can also perform one final unsuccessful comparison. There are only $O(n)$ centers, so all failed comparisons together are also $O(n)$. This amortized argument is the key reason Manacher's algorithm has a strict linear bound even for highly repetitive strings.

**Recover the substring in original coordinates**

Keep the center with the largest radius. If that transformed center is `best_center` and its radius is `best_length`, then the original start index is:

```text
(best_center - best_length) // 2
```

The division removes the separators that occur before the palindrome. Return `best_length` original characters from that start position. Odd and even lengths require no separate formula because the transformed representation already encoded their parity.

For `cbbd`, the best transformed center is the separator between the two `b` characters, with radius `2`. The formula yields original start index `1`, and the next two characters are `bb`.

**Why every stored radius is exact**

The inserted separators create a one-to-one correspondence: every original palindrome has one transformed center and radius, and removing separators from any transformed palindrome recovers an original one. It therefore suffices to show that the scan computes each transformed radius exactly.

Inside the current rightmost palindrome, reflection across its center guarantees the copied matches, but only up to the nearer of the mirrored radius and the known boundary. Nothing beyond that clipped region is assumed. Direct expansion then tests the first unknown pair and continues until the first mismatch, so it cannot stop before a valid match or extend through an invalid one. A center outside the boundary starts with no assumed matches and reaches the same exact result by expansion.

Updating `center` and `right` after an extension changes only which already-proven palindrome supplies symmetry to later centers. Thus every recorded radius is exact, and selecting the maximum followed by the coordinate conversion returns a longest original palindromic substring.

#### Complexity detail

The transformed sequence contains $2n + 1$ non-sentinel positions. Its construction, the radius array, and the final scan all use $O(n)$ space. Mirror initialization is constant time per center, the right boundary advances at most linearly many times, and each center contributes at most one terminating mismatch, so total time is $O(n)$.

#### Alternatives and edge cases

- Expanding around every character and every gap is much simpler and uses $O(1)$ auxiliary space, but takes $O(n^2)$ time on repetitive inputs.
- Dynamic programming can record whether every interval is palindromic, but requires $O(n^2)$ time and space.
- Enumerating substrings and checking each one can require $O(n^3)$ time.
- A one-character string is already its own answer. Strings whose longest palindrome is even-length are handled by separator centers.
- If several longest palindromes have equal length, returning any one of them satisfies the contract. Update the saved best only on a strictly larger radius if deterministic first-occurrence behavior is desired.

</details>

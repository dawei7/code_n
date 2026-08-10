## General

**Build larger palindromes from smaller inner substrings**

A string is a palindrome when it reads the same from left to right and right to left. For a substring with inclusive endpoints `i` and `j`, two facts are needed:

1. the outer characters match: `s[i] == s[j]`;
2. everything between them, `s[i + 1:j]`, is itself a palindrome.

This gives the recurrence

$$
f[i][j] = (s[i] = s[j]) \land f[i+1][j-1].
$$

Here `f[i][j]` means “the contiguous substring `s[i:j+1]` is a palindrome.” The table remembers answers for inner substrings, allowing an outer substring to be classified in constant time instead of comparing all its character pairs again.

The method is dynamic programming because a state for one interval is derived from a smaller state whose answer has already been stored.

**Why the table starts entirely `True`**

The code creates

```python
f = [[True] * n for _ in range(n)]
```

At first this can look surprising: surely not every substring is a palindrome. Most meaningful entries are overwritten by the nested loops. The initial `True` values serve two base cases through their table positions:

- `f[i][i]` represents a one-character substring, which is always a palindrome;
- `f[i + 1][i]` represents the empty interior of a two-character substring `s[i:i+2]`, and an empty string is considered palindromic.

The second case is stored below the main diagonal, where the left boundary is greater than the right boundary. For adjacent endpoints `j = i + 1`, the recurrence reads `f[i + 1][j - 1] = f[i + 1][i]`. Leaving that entry `True` means two equal adjacent characters, such as `"bb"`, are recognized as a palindrome without a separate length-two branch.

Entries above the diagonal correspond to real substrings of length at least two. Every such entry visited by the loops is explicitly set to `False` before the matching-character test, so the broad initialization does not falsely mark an examined substring.

**Choose an order that computes the inner state first**

The recurrence for `f[i][j]` depends on `f[i + 1][j - 1]`. Therefore the row with the larger start index `i + 1` must already be complete before row `i` is processed.

The outer loop moves `i` backward:

```python
for i in range(n - 2, -1, -1):
```

It begins at `n - 2` because the final one-character state on the diagonal already has its base value. The inner loop moves `j` from `i + 1` to the end:

```python
for j in range(i + 1, n):
```

When the algorithm reaches `(i, j)`, the dependency `(i + 1, j - 1)` lies in the next row, which was processed during an earlier outer-loop iteration, or on/below the diagonal, where the base initialization is correct.

This ordering is essential. Scanning `i` from left to right would ask for states in row `i + 1` before that row had been computed.

**Classify each interval exactly as the recurrence requires**

For every pair with `i < j`, the code first assumes the interval is not palindromic:

```python
f[i][j] = False
```

If the outer characters differ, that answer is final. A palindrome must have matching first and last characters, regardless of what lies inside.

If the characters match, the code copies the inner result:

```python
if s[i] == s[j]:
    f[i][j] = f[i + 1][j - 1]
```

Matching endpoints are necessary but not sufficient. For example, `"abca"` begins and ends with `a`, yet its interior `"bc"` is not a palindrome. Consulting the stored inner state prevents this false positive.

Conversely, if the endpoints match and the interior reads equally in both directions, adding the same character to both sides preserves the mirrored order. The resulting substring must be a palindrome.

**Track bounds without repeatedly slicing strings**

The variables

```python
k, mx = 0, 1
```

describe the best answer found so far:

- `k` is its starting index;
- `mx` is its length.

The non-empty-input guarantee makes the initial one-character answer `s[0:1]` valid. Whenever `f[i][j]` is true, the candidate length is `j - i + 1`. The code updates only when

```python
mx < j - i + 1
```

so a strictly longer palindrome replaces the previous answer. Equal-length palindromes do not replace it, which is allowed because the contract accepts any longest answer. The algorithm stores only integer bounds while scanning; it creates the result substring once at the end with `s[k:k + mx]`.

**Walk through how `"cbbd"` finds its even palindrome**

The single-character diagonal states begin as true, and the best length begins at `1`.

| State | Substring | Endpoint test | Inner state | Result |
|---|---|---|---|---|
| `f[2][3]` | `"bd"` | `b != d` | not needed | `False` |
| `f[1][2]` | `"bb"` | `b == b` | `f[2][1] = True` for the empty interior | `True`; update to start `1`, length `2` |
| `f[1][3]` | `"bbd"` | `b != d` | not needed | `False` |
| `f[0][1]` | `"cb"` | `c != b` | not needed | `False` |
| `f[0][2]` | `"cbb"` | `c != b` | not needed | `False` |
| `f[0][3]` | `"cbbd"` | `c != d` | not needed | `False` |

The final slice is `s[1:3]`, or `"bb"`.

For an odd palindrome such as `"bab"`, matching outer `b` characters consult the one-character inner state for `"a"`. The same recurrence therefore handles both odd and even lengths; only the base state differs between a one-character and an empty interior.

**Why the saved answer is globally longest**

Every possible substring is identified by one pair of inclusive endpoints `(i, j)`. Length-one substrings are covered by the initialized answer and diagonal. The nested loops examine every pair with `i < j`, and the recurrence marks exactly those intervals whose endpoint characters and interior form a palindrome.

Whenever such an interval is longer than the current best, its start and length are saved. Because no substring interval is omitted, a palindrome longer than `mx` cannot remain undiscovered. At termination, `mx` is the maximum palindromic-substring length and `s[k:k + mx]` is one substring attaining it.

## Complexity detail

Let $n$ be `len(s)`.

- **Time complexity of this exact implementation: $O(n^2)$.** The table allocation initializes $n^2$ booleans. The nested loops visit

  $$
  \frac{n(n-1)}{2}
  $$

  endpoint pairs, and each state performs constant-time comparisons, indexing, assignments, and arithmetic. The final slice copies at most $n$ characters, which does not exceed the quadratic table work.
- **Space complexity of this exact implementation: $O(n^2)$.** `f` stores an $n \times n$ Python list of boolean references. The indices and best-answer variables use $O(1)$ additional space, while the returned slice uses $O(n)$ output space.

The branch manifest declares $O(n)$ time and $O(n)$ space, which are the bounds of Manacher's algorithm used by the Competitive variant. They do not describe this dynamic-programming source. This explanation retains the exact quadratic costs so readers are not taught an incorrect analysis for the code they see.

## Alternatives and edge cases

- **Manacher's algorithm:** Transform the string to unify odd and even centers, reuse mirrored palindrome radii, and expand only beyond the farthest known boundary. It achieves $O(n)$ time and $O(n)$ space, matching the manifest, but is substantially more intricate than this DP recurrence.
- **Expand around every center:** Treat each character and each gap as a possible palindrome center. It uses $O(1)$ auxiliary space and $O(n^2)$ worst-case time, avoiding the full table while remaining interview-friendly.
- **Check all substrings independently:** Testing $O(n^2)$ substrings with an $O(n)$ two-pointer palindrome check costs $O(n^3)$ in the worst case and repeats inner comparisons that DP reuses.
- **Store only recent DP rows:** Because `f[i][j]` depends on row `i + 1`, memory can be compressed with careful iteration. However, reconstructing or tracking the answer must remain explicit, and center expansion is often simpler for $O(1)$ auxiliary space.
- **One-character string:** The loops do not run, and the initialized `k = 0`, `mx = 1` returns that character.
- **Two equal characters:** The below-diagonal empty-interior state is `True`, so the pair is recognized and becomes the answer.
- **Two different characters:** Their state stays false, and the valid one-character initial answer is returned.
- **All characters equal:** Every interval is palindromic. The table still visits all $O(n^2)$ states, and the full string eventually becomes the best answer.
- **Several longest answers:** The strict update keeps whichever maximum-length palindrome was found first in this traversal order. For `"babad"`, either `"bab"` or `"aba"` is valid under the contract.
- **Odd and even lengths:** A diagonal `True` state anchors odd palindromes, while a below-diagonal `True` state anchors equal adjacent characters for even palindromes.
- **Contiguous requirement:** Every state uses a complete inclusive interval `s[i:j+1]`; the recurrence never skips interior characters, so it cannot return a subsequence.
- **Digits and letter case:** Characters are compared exactly. Digits participate like letters, and uppercase and lowercase letters are distinct.
- **Input preservation:** The string and table states are read independently; the method never changes `s`.

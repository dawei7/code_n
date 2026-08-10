## General

A split after character index $i$ is balanced when:

$$
\text{score of }s[0..i]
=
\text{score of }s[i+1..n-1].
$$

Instead of recomputing both substring scores for every split, the source begins with the entire score on the right and moves one character at a time from the right total to the left total.

**Converting a character to its score**

For lowercase character `c`, the expression:

`ord(c) - ord("a") + 1`

maps:

- `a` to one;
- `b` to two;
- and `z` to 26.

`ord` returns the character's integer code. Lowercase English letters occupy consecutive code points, so subtracting the code for `a` yields a zero-based alphabet position, and adding one gives the required score.

**Initial left and right totals**

The source initializes:

`l = 0`

because no character has yet moved into the prefix.

It computes:

`r = sum(ord(c) - ord("a") + 1 for c in s)`

so `r` initially equals the score of the complete string.

At this conceptual moment, the boundary lies before the string. That is not a legal split because the left substring is empty, so the method does not compare `l` and `r` yet.

**Moving the boundary**

The loop visits:

`s[:-1]`

which contains every character except the final one. For current character score `x`:

`l += x`

`r -= x`.

The same score is added to the prefix and removed from the suffix. Therefore:

- `l` becomes the score through the current split index;
- `r` becomes the score of every character after it.

If the two totals match, the source immediately returns true.

For `s = "adcb"`, total score is:

$$
1+4+3+2=10.
$$

After moving `a`, the totals are one and nine. After moving `d`, they are five and five, so the split `"ad" | "cb"` succeeds.

**Why the final character is excluded**

Both substrings must be nonempty. If the loop moved the last character to the left, the right score would represent an empty suffix and would not be a legal candidate.

Using `s[:-1]` creates exactly $n-1$ iterations, one for each legal split after indices zero through $n-2$.

The input length is at least two, so this slice contains at least one character and there is at least one candidate split.

**Running-state meaning**

After processing loop character at index `i`:

$$
l=\sum_{j=0}^{i}\operatorname{score}(s[j])
$$

and:

$$
r=\sum_{j=i+1}^{n-1}\operatorname{score}(s[j]).
$$

This follows from the initial complete right sum and moving each visited character exactly once.

Thus `l == r` is equivalent to the contract's equal-substring-score condition for that exact boundary.

**Why early return is safe**

The problem asks whether at least one balanced split exists, not how many exist or which index is earliest. As soon as one equality is found, returning true is conclusive.

If the loop ends without equality, every legal split has been tested once, so returning false is conclusive.

**An equivalent total-score view**

Because `l + r` always equals the total string score, equality is also equivalent to:

$$
2l=\text{total score}.
$$

The source keeps both running values, which mirrors the two substring scores directly. It does not need division, and odd total scores naturally never produce equality.

## Complexity detail

Let $n$ be `len(s)`.

Computing the total score scans all $n$ characters. The boundary loop scans $n-1$ characters and performs constant work for each. Total time is $O(n)$.

The exact source creates `s[:-1]`. Python strings are immutable, and slicing materializes a new string of length $n-1$. Therefore, the exact auxiliary space complexity is $O(n)$, not $O(1)$.

This is a source/manifest mismatch. Iterating by index over `range(n - 1)` would preserve the same logic with constant auxiliary workspace, but it is not the checked-in expression.

The generator used for the initial `sum` is lazy and does not create a score list. The linear allocation comes specifically from the string slice.

## Alternatives and edge cases

- **Recompute both scores at every boundary:** Summing prefix and suffix substrings repeatedly can take $O(n^2)$ time.
- **Prefix-sum array:** It supports constant-time split checks after $O(n)$ preprocessing but uses $O(n)$ storage. Two running totals are simpler.
- **Index-based scan:** Looping over indices zero through $n-2$ avoids `s[:-1]` and achieves the manifest's intended $O(1)$ auxiliary space.
- **Check `2 * l == total`:** This equivalent condition keeps only a prefix and fixed total, also using constant scalar state.
- **Two-character string:** There is one split, and it succeeds exactly when the two character scores match.
- **Odd total score:** Two integer substring scores cannot both equal half an odd total, so no split can succeed.
- **Repeated letters:** Each occurrence contributes separately according to position; equality depends only on summed scores.
- **Early balanced split:** The method returns immediately because existence is all that is requested.
- **Nonempty suffix:** Excluding the last character from the loop prevents testing an illegal empty right substring.
- **Alphabet mapping:** The added one is essential because the contract assigns `a = 1` rather than zero.

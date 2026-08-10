## General

A direct solution could compare every pair of indices, but the distance objective strongly favors the boundaries of the array. An optimal unequal pair can always be replaced, without reducing its distance, by a valid pair touching index zero or index $n-1$.

The exact source therefore compares every word with only:

- `words[0]`, the first word; and
- `words[-1]`, the last word.

This covers all candidate pairs whose left endpoint is zero or whose right endpoint is $n-1$.

**Distances to the first boundary**

At index `i`, if:

`words[i] != words[0]`

then indices zero and `i` form a valid unequal pair. Their inclusive distance is:

$$
i-0+1=i+1.
$$

The source updates `ans` with `i + 1`.

This is why the expression is not merely `i`. The problem defines distance as $j-i+1$, which counts both endpoint positions.

**Distances to the last boundary**

If:

`words[i] != words[-1]`

then indices `i` and $n-1$ form a valid unequal pair. Their distance is:

$$
(n-1)-i+1=n-i.
$$

The source updates `ans` with `n - i`.

The two tests are independent rather than an `if/elif` pair. A middle word may differ from both endpoints, in which case both boundary distances are valid and the larger one should be considered.

**Why checking boundary pairs is sufficient**

First consider the easiest case: `words[0] != words[-1]`. The two endpoints themselves form a valid pair with distance $n$, the largest possible distance in an array of length $n$. The loop discovers it—for example, at `i = 0` the comparison with the last word succeeds and contributes `n - 0 = n`. No other pair can improve on $n$.

Now suppose the endpoint words are equal; call that common word $A$. Take any valid interior pair $i<j$ with `words[i] != words[j]`.

There are two cases.

If `words[i] != A`, then `words[i]` differs from the last boundary word. Pair $(i,n-1)$ is valid, and its distance is:

$$
n-i\ge j-i+1
$$

because $j\le n-1$.

Otherwise, `words[i] = A`. Since the original pair is unequal, `words[j] != A`. Pair $(0,j)$ is valid, and its distance is:

$$
j+1\ge j-i+1
$$

because $i\ge0$.

Thus every valid pair is dominated by an unequal boundary pair that the loop checks. The maximum over those boundary candidates must equal the maximum over all pairs.

**Tracing the second example**

For `words = ["a", "b", "c", "a", "a"]`, both boundary words equal `"a"`.

- At index one, `"b"` differs from the last word, producing distance $5-1=4$ for pair $(1,4)$.
- At index two, `"c"` differs from both boundaries, producing distances three and three.
- The later `"a"` values do not differ from either boundary.

The maximum remains four.

**Why zero is the correct initial value**

The source begins with:

`ans = 0`

Every valid pair of distinct indices has distance at least two, so zero cannot incorrectly defeat a genuine candidate. If all words are equal, neither comparison ever succeeds, `ans` remains zero, and the method returns the required sentinel.

For a one-word array, no two distinct indices exist. Both comparisons involve the same word and fail, so zero is again returned.

**Every source expression matches one legal pair**

Whenever `i + 1` updates the answer, the inequality check proves that pair $(0,i)$ uses unequal words. Whenever `n - i` updates it, pair $(i,n-1)$ is valid. The algorithm never invents a distance without checking the corresponding words.

Combined with the boundary-dominance argument, this shows the final maximum is neither too large nor too small.

## Complexity detail

Let $n$ be the number of words and let $L$ be the maximum word length.

The loop visits each index once and performs at most two string comparisons. A string comparison can take $O(L)$ time, so the generalized bound is $O(nL)$.

The contract limits every word to length at most ten, making $L$ a fixed constant. Under these constraints, the reported time complexity is $O(n)$.

The method stores only `n`, `ans`, the loop index, and references to existing strings. Auxiliary space is $O(1)$.

No input word or array position is modified.

## Alternatives and edge cases

- **Compare every pair:** The straightforward double loop costs $O(n^2L)$ time. Boundary dominance reduces this to one scan.
- **Scan outward from both ends:** One can find the farthest word unequal to each endpoint separately. The exact source combines both searches into one loop.
- **Compare only the first endpoint:** This fails when the best pair uses a word equal to the first endpoint but unequal to the last, as can happen when the endpoint words differ.
- **First and last words differ:** Distance $n$ is immediately attainable and is the absolute maximum.
- **First and last words match:** Any unequal interior pair can be extended to one boundary as shown in the two-case argument.
- **All words equal:** No valid pair exists, both conditions always fail, and zero is returned.
- **One word:** Distinct indices are impossible, so zero is correct.
- **Repeated words:** Equality is based on complete string content, not object identity or frequency.
- **Inclusive distance:** Pair $(i,j)$ contributes $j-i+1$. Omitting the added one would undercount every valid answer.
- **A middle word differs from both boundaries:** Both candidates are evaluated because the source uses two separate `if` statements.

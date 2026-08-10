## General

There can be up to $10^5$ words, so comparing every pair is too slow. The distance objective allows a stronger observation: some maximum-distance unequal pair always uses the first or last array position.

The exact source scans every index `i` and evaluates two possible boundary pairs:

- pair $(0,i)$ when `words[i]` differs from the first word;
- pair $(i,n-1)$ when `words[i]` differs from the last word.

**Candidate using the first word**

If:

`words[i] != words[0]`

then indices zero and `i` are distinct unless `i = 0`, where the inequality naturally fails. Their inclusive distance is:

$$
i-0+1=i+1.
$$

The source updates `ans` with `i + 1`.

The added one is part of the problem's definition. Adjacent indices have distance two, not one.

**Candidate using the last word**

If:

`words[i] != words[-1]`

then pair $(i,n-1)$ is valid and has distance:

$$
(n-1)-i+1=n-i.
$$

The source evaluates `n - i`.

The tests are separate `if` statements. If a middle word differs from both endpoint words, both distances are legitimate and both should compete for the maximum.

**Why endpoint comparisons cover all optimal pairs**

If `words[0] != words[n-1]`, the endpoints themselves form an unequal pair with distance $n$, the largest any pair can have. The scan finds this value, so the result is immediate.

Now suppose the endpoint words are equal to a common value $A$. Consider any valid pair $i<j$ with `words[i] != words[j]`.

If `words[i] != A`, pair $(i,n-1)$ is valid. Its distance satisfies:

$$
n-i\ge j-i+1
$$

because $j\le n-1$.

Otherwise `words[i] = A`. The original pair is unequal, so `words[j] != A`. Pair $(0,j)$ is valid, and:

$$
j+1\ge j-i+1.
$$

Thus every valid interior pair has an unequal boundary pair at least as far apart. Taking the maximum over all boundary pairs is sufficient.

**Why every computed value is attainable**

The source does not update `ans` from distance alone. It first checks that the corresponding two boundary words differ.

- `i + 1` always represents actual valid pair $(0,i)$.
- `n - i` always represents actual valid pair $(i,n-1)$.

Therefore, the method cannot return a distance belonging only to equal words.

Combining attainability with boundary dominance establishes that the returned maximum is exact.

**Example with matching endpoints**

For `["a", "b", "c", "a", "a"]`, the endpoints both contain `"a"`.

At index one, `"b"` differs from the last word and produces:

$$
5-1=4.
$$

At index two, `"c"` differs from both boundaries, but each associated distance is only three. No later candidate exceeds four.

**No-valid-pair behavior**

`ans` begins at zero. If every word is equal, neither inequality ever succeeds and zero is returned as required.

If the array contains one word, the only comparisons are that word with itself. No pair of distinct indices exists, and the result also remains zero.

**The scan covers both boundary families completely**

As `i` moves from zero through $n-1$, the first condition considers every coordinate pair of the form $(0,i)$. The second condition considers every pair of the form $(i,n-1)$. Those are exactly the two boundary families used in the dominance argument.

The method does not need to remember which indices produced `ans` because the requested output is only a distance. If a later valid boundary pair is farther, `max` replaces the old value; if it is shorter or tied, the best distance remains unchanged.

When the endpoint words differ, distance $n$ is discovered and no larger answer is mathematically possible. The source still completes the scan rather than returning early. This performs a little unnecessary constant work per remaining index but leaves the $O(n)$ bound unchanged and keeps one uniform loop for every input.

The inequality checks also enforce distinctness automatically at the two degenerate boundary positions. At `i = 0`, the first comparison is a word against itself and fails. At `i = n - 1`, the second comparison likewise fails. Only the cross-endpoint test can yield distance $n$, and it does so only when those endpoint words truly differ.

## Complexity detail

Let $n$ be `len(words)` and $L$ be the maximum word length.

The loop performs at most two string comparisons per index. A comparison can examine up to $L$ characters, giving generalized time $O(nL)$.

The contract bounds $L$ by ten, so it is a fixed constant and the reported complexity is $O(n)$.

The source stores only scalar values and references to the existing endpoint strings. Auxiliary space is $O(1)$.

The input array and its strings are not modified.

## Alternatives and edge cases

- **Check all pairs:** A double loop takes $O(n^2L)$ time and is infeasible for $n=10^5$.
- **Scan separately from each endpoint:** Two scans are equivalent. The source performs both comparisons inside one loop.
- **Compare only against `words[0]`:** This can miss a farther valid pair that is best expressed using the last endpoint.
- **Different endpoint words:** The answer is immediately the full length $n$, though the source discovers it during its ordinary scan.
- **Equal endpoint words:** Any unequal pair contains or can be extended toward a word differing from the common endpoint value.
- **All words equal:** No comparison succeeds, so zero is returned.
- **One word:** Distinct indices do not exist, and zero is correct.
- **Adjacent unequal words:** Their distance is two because both endpoints are counted.
- **Repeated non-endpoint words:** Only content equality matters; frequency and object identity are irrelevant.
- **Middle word differs from both endpoints:** Both boundary distances are considered independently.

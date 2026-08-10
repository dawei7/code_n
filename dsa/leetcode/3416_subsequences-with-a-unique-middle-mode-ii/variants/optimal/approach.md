## General

**Fix the middle index and choose two positions on each side.** A length-$5$ subsequence whose middle element is `nums[index]` must choose exactly two earlier indices and two later indices. Let the middle value be $x$, let $L$ be the number of positions on the left, and let $R$ be the number on the right. There are

$$
\binom L2\binom R2
$$

total ways to choose those four surrounding positions. The source counts all of them and subtracts precisely the choices in which $x$ is not the unique mode.

Let $l_v$ and $r_v$ be the frequencies of value $v$ on the left and right of the middle. In particular, write $a=l_x$ and $b=r_x$. The `left` and `right` counters maintain these frequencies while the middle index moves.

**Classify invalid choices by how many extra copies of the middle value are selected.** The middle itself already contributes one $x$.

If no surrounding position contains $x$, then $x$ appears once. If all four other values are distinct, every value ties at frequency one; if any repeats, that other value beats $x$. Either way, $x$ is not a unique mode. The number of these invalid choices is

$$
\binom{L-a}{2}\binom{R-b}{2},
$$

which is `choose_two(left_other) * choose_two(right_other)`.

If at least two surrounding positions contain $x$, then $x$ appears at least three times. At most two non-$x$ positions remain, so no other value can tie its frequency. Every such choice is automatically valid.

The only complicated case is exactly one extra $x$. Then $x$ appears twice and is the unique mode unless some non-$x$ value also appears at least twice among the other three selected positions. The source counts these ties separately depending on which side supplies the extra $x$.

**Extra \(x\) chosen on the left.** There are $a$ choices for that occurrence. The remaining selections are one non-$x$ left position and two non-$x$ right positions. A repeated non-$x$ value arises in one of two disjoint ways:

1. the two right values are equal; or
2. the right values differ, and the left value equals one of them.

Define

$$
P_R=\sum_{v\ne x}\binom{r_v}{2}
$$

and

$$
C=\sum_{v\ne x}l_vr_v.
$$

The first case has $(L-a)P_R$ choices. For the second, fix the matched value $v$: choose its left occurrence in $l_v$ ways, one matching right occurrence in $r_v$ ways, and the other right position from the $(R-b)-r_v$ non-$x$ positions with a different value. Summing gives

$$
\sum_{v\ne x}l_vr_v((R-b)-r_v)
=(R-b)C-\sum_{v\ne x}l_vr_v^2.
$$

Multiplying the sum of these cases by $a$ produces the source's first long invalid term.

**Extra \(x\) chosen on the right.** This is symmetric. There are $b$ choices for that $x$, leaving two non-$x$ left positions and one non-$x$ right position. Invalid selections either have an equal left pair or have different left values with the right value matching one of them:

$$
b\left((R-b)P_L+(L-a)C-\sum_{v\ne x}l_v^2r_v\right),
$$

where $P_L=\sum_{v\ne x}\binom{l_v}{2}$.

Subtracting the no-extra-$x$ case and these two exactly-one-$x$ tie cases from the total leaves precisely the subsequences where the middle value is the unique mode.

**Maintain all required sums in constant time.** Iterating over every distinct $v$ for every middle would be quadratic. The source instead maintains five global aggregates:

$$
\begin{aligned}
\texttt{left\_pairs} &= \sum_v\binom{l_v}{2},\\
\texttt{right\_pairs} &= \sum_v\binom{r_v}{2},\\
\texttt{sum\_left\_right} &= \sum_v l_vr_v,\\
\texttt{sum\_left\_right\_squared} &= \sum_v l_vr_v^2,\\
\texttt{sum\_left\_squared\_right} &= \sum_v l_v^2r_v.
\end{aligned}
$$

For the current middle $x$, subtracting its contribution from each aggregate yields the corresponding sum over $v\ne x$, such as `other_cross` and `other_right_pairs`.

At the start, the left side is empty and `right` contains all values. Before evaluating an index, the current occurrence is removed from the right. If its old right count is $b+1$, then $\binom{b+1}{2}-\binom b2=b$, explaining `right_pairs -= right_middle`. The cross sum decreases by $a$. The $l_vr_v^2$ aggregate changes by $a(b^2-(b+1)^2)$, and the $l_v^2r_v$ aggregate decreases by $a^2$. These are exactly the four source updates before counting.

After counting, the current occurrence moves onto the left, changing $a$ to $a+1$. The left-pair sum increases by $a$. The cross sum increases by $b$, the $l_vr_v^2$ sum by $b^2$, and the $l_v^2r_v$ sum by

$$
((a+1)^2-a^2)b=(2a+1)b.
$$

Those identities explain every maintenance statement in the code.

**Why the count is exact.** Every selection of two left and two right positions falls into exactly one of the zero, one, or at-least-two extra-$x$ categories. The zero category is wholly invalid; the at-least-two category is wholly valid; and the one category is invalid exactly when its three non-$x$ values contain a duplicate. The two disjoint duplicate patterns count each such triple once. Therefore, `total - invalid` is exactly the valid count for this middle. Summing over middle indices counts each length-$5$ index subsequence once, at its unique third index.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Building the initial counter and initial right-pair sum takes $O(n)$ expected time. Each middle index performs a constant number of expected-$O(1)$ counter accesses and integer arithmetic operations; it never loops over distinct values. Total expected time is $O(n)$.

The two counters contain at most $O(n)$ distinct values, so auxiliary space is $O(n)$. All aggregate sums are scalar Python integers. The answer is reduced modulo $10^9+7$ after each middle contribution, while the maintained combinatorial aggregates remain exact.

## Alternatives and edge cases

- **Enumerate five indices:** Directly checking every length-$5$ subsequence costs $O(n^5)$ and is impossible for $n=10^5$.
- **Loop over distinct values per middle:** The same formulas can be computed from counters by summing all values each time, but this degrades to $O(n^2)$ when values are mostly distinct.
- **Count valid patterns directly:** Valid cases can also be divided by the number of extra middle values, but the exactly-one case remains intricate. Total-minus-invalid produces compact disjoint formulas.
- **All values equal:** Every choice of five indices is valid. The subtraction terms become zero, yielding $\binom n5$ across all middle positions, as in the first example.
- **All values distinct:** The middle appears once and ties every other value, so every selection is included in the no-extra-$x$ invalid term and the result is zero.
- **Mode ties:** Appearing twice is insufficient if another value also appears twice. The duplicate-triple formulas exist specifically to remove those ties.
- **Negative and large values:** Counter keys can be any integers; the algorithm depends on equality and frequency, not numeric magnitude.
- **Too few positions on one side:** `choose_two(0)` and `choose_two(1)` are zero, so edge middle indices contribute nothing without separate branches.
- **Nonnegative subtraction:** The combinatorial derivation guarantees `total - invalid` counts real selections. Applying modulo also safely normalizes the accumulated answer.
- **Current occurrence placement:** The middle must be removed from `right` before counting and added to `left` afterward. Reversing either step would allow the same index to be selected as both middle and side element.

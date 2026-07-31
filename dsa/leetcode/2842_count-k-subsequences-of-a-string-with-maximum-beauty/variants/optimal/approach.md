## General

**Reduce subsequences to character choices.** Every valid subsequence uses each selected character exactly once. Its beauty therefore depends only on which $k$ distinct characters are selected, not on which occurrence of each character supplies the subsequence. If a chosen character $c$ occurs $f(c)$ times, however, there are $f(c)$ choices for its selected index. Once one index has been chosen for each character, their positions determine exactly one subsequence order; there is no extra permutation factor.

**Find the only maximum-beauty frequency profile.** Count the frequencies of the at most $26$ lowercase letters and sort the positive counts in descending order. If fewer than $k$ counts exist, no valid subsequence exists. Otherwise, a maximum-beauty selection must use the $k$ largest frequencies: replacing any selected frequency with a larger unselected one would strictly increase the beauty.

The only ambiguity occurs at the $k$th frequency. Let $x$ be this cutoff, let $h$ be the number of characters with frequency greater than $x$, and let $t$ be the number with frequency exactly $x$. All $h$ higher-frequency characters are forced, and the selection needs another $r=k-h$ characters from the tied group. There are $\binom{t}{r}$ ways to choose their identities.

For every chosen set of identities, the forced characters contribute the product of their frequencies and the tied characters contribute $x^r$. Thus the answer is

$$
\left(\prod_{f(c)>x} f(c)\right)x^r\binom{t}{r}\pmod{10^9+7}.
$$

This counts every maximum-beauty index subsequence exactly once: its selected character set appears in one combination, and its selected occurrence of each character appears in one factor of the corresponding frequency.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and let $A=26$ be the fixed lowercase alphabet size. Counting the string takes $O(n)$ time; sorting at most $A$ counts takes $O(A\log A)$ time. Since $A$ is constant, the total time is $O(n)$.

The counter and sorted frequency list each hold at most $A$ entries, so the auxiliary space is $O(1)$ with respect to $n$.

## Alternatives and edge cases

- **Enumerate k-subsequences:** Generating index combinations directly is exponential or combinatorial in $n$ and repeats the same character-set reasoning many times.
- **Dynamic programming by position and character set:** A state over selected letters can count subsequences, but it introduces unnecessary exponential dependence on the alphabet when only global frequencies matter.
- **Fewer than k distinct characters:** The uniqueness rule makes a valid k-subsequence impossible, so return `0` before accessing the cutoff.
- **Partial cutoff tie:** Only the required number of tied characters is selected; omitting the factor $\binom{t}{r}$ undercounts different character sets with the same maximum beauty.
- **Index identity:** Selecting different occurrences of the same chosen character creates different subsequences, which is why each character contributes its frequency as a multiplicative factor.
- **No factorial:** Chosen indices have one inherited left-to-right order, so the selected characters must not be permuted again.
- **Modulo arithmetic:** Products and powers are reduced modulo $10^9+7$ to keep large counts bounded.

## General

**Beauty depends only on which character identities are chosen.** A valid length-`k` subsequence uses `k` distinct characters. If character `c` is included, its contribution to beauty is the global frequency `f(c)`, regardless of which occurrence of `c` supplies the subsequence.

Therefore, maximum beauty is obtained by choosing `k` character identities with the largest global frequencies.

**First check whether a valid subsequence exists.** `Counter(s)` records one frequency per distinct lowercase character. If there are fewer than `k` keys, it is impossible to choose `k` unique characters, so the method returns zero.

**Sort frequencies and identify the cutoff.** `vs = sorted(f.values(), reverse=True)` orders character frequencies from largest to smallest. The frequency at index `k - 1`, stored in `val`, is the cutoff frequency of an optimal identity set.

Every character with frequency strictly greater than `val` must be selected. Excluding one of them in favor of a lower-frequency character would reduce beauty.

Characters with frequency below `val` cannot be selected while maximum beauty is maintained.

Among all characters whose frequency equals `val`, enough are selected to fill the remaining slots. These tied identities create combinatorial alternatives with equal maximum beauty.

**Count how many characters are tied at the cutoff.** `x = vs.count(val)` is the total number of distinct characters having frequency `val`. This includes tied characters appearing both before and after the cutoff position in the sorted list.

**Multiply choices for mandatory higher-frequency characters.** `ans` starts at one. The loop scans frequencies in descending order and stops when it reaches `val`. For every frequency `v > val`:

- One character with that frequency is mandatory.
- There are `v` choices of occurrence index for that character.
- `k` is decremented because one required character slot has been filled.
- `ans` is multiplied by `v` modulo $10^9+7$.

After this loop, the mutated `k` is no longer the original subsequence length. It is the number $r$ of cutoff-frequency character identities still needed.

**Choose identities and occurrences at the cutoff.** There are `comb(x, k)` ways to choose which $r$ of the $x$ tied characters participate.

For each selected cutoff character, any of its `val` occurrences can supply the subsequence. Independent occurrence choice gives `val^r` possibilities, computed by `pow(val, k, mod)`.

The final multiplication is therefore

$$
\left(\prod_{f(c)>\texttt{val}} f(c)\right)
\binom{x}{r}\texttt{val}^{\,r}
\pmod{10^9+7}.
$$

**Why choosing occurrences counts subsequences correctly.** Once one occurrence index has been selected for each chosen character identity, sorting those indices yields exactly one subsequence in original string order. Different occurrence choices produce different index sets, which the statement counts as different subsequences even if the resulting character string happens to be identical.

No additional factorial for ordering is needed. Subsequence order is forced by the selected indices; characters cannot be arbitrarily permuted after occurrence positions are chosen.

**Why only the cutoff group creates identity choices.** All frequencies above the cutoff are mandatory, and all below are excluded. Any substitution between unequal frequencies changes the beauty sum. Only equal-frequency characters can replace one another without changing beauty.

**A simple tied example.** Suppose frequencies are three, two, two, and one with original `k = 2`. Frequency three is mandatory and contributes three occurrence choices. One of the two frequency-two characters is needed, giving two identity choices and two occurrence choices. The count is $3\cdot2\cdot2=12$.

**Fixed alphabet implications.** The input contains only lowercase English letters, so there are at most 26 Counter entries. Sorting, counting the cutoff, and computing the combination operate on a constant-sized collection. The scan of `s` dominates runtime.

## Complexity detail

Let $n=\lvert s\rvert$ and let $\sigma\le26$ be the number of distinct characters. Building the Counter takes $O(n)$ time. Sorting frequencies takes $O(\sigma\log\sigma)$, which is $O(1)$ for the fixed alphabet. The remaining loop and count are $O(\sigma)$.

Total time is $O(n)$. Python's `comb` operates on values at most 26, and modular exponentiation uses an exponent at most 26, so both are constant-time under this contract.

The Counter and frequency list contain at most 26 items, making auxiliary space $O(1)$ with respect to $n$. The returned integer is constant-size modulo the fixed modulus.

For an unbounded alphabet, the more general bounds would be $O(n+\sigma\log\sigma)$ time and $O(\sigma)$ space.

## Alternatives and edge cases

- **Frequency buckets:** Since each frequency is at most $n$, group how many characters have each frequency and scan downward. This avoids sorting but uses $O(n)$ buckets unless a sparse map is used.
- **Select top `k` with a heap:** It can find the cutoff without fully sorting, but the alphabet has only 26 characters, so sorting is simpler.
- **Fewer than `k` distinct characters:** No valid unique-character subsequence exists, and zero is returned immediately.
- **`k = 1`:** Choose any character with maximum frequency and any one of its occurrences; the formula counts all such index choices.
- **All frequencies equal:** No character is mandatory above the cutoff; choose any `k` identities and one occurrence of each.
- **No tie at cutoff:** `x = k_remaining = 1` for that group in the relevant sense, so the combination factor is one.
- **Repeated subsequence text:** Different selected indices still count separately, and frequency multiplication captures them.
- **Modulo timing:** Identity and occurrence counts are derived in ordinary combinatorics, then multiplied modulo the required prime.
- **Mutating `k` locally:** The parameter is intentionally reused as remaining slots; no later step needs its original value.
- **Subsequence ordering:** It is determined by index order, so no permutation factor should be introduced.
- **Lower-frequency characters:** Including any one would strictly lower beauty and is never counted.

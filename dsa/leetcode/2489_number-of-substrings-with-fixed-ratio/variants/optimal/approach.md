## General

**Convert a ratio into an equality**

Suppose a substring contains $z$ zeros and $o$ ones. The required ratio is

$$
z:o=\texttt{num1}:\texttt{num2}.
$$

Cross-multiplication avoids division:

$$
z\cdot\texttt{num2}
=
o\cdot\texttt{num1}.
$$

Rearranging gives a zero-valued weighted balance,

$$
o\cdot\texttt{num1}
-
z\cdot\texttt{num2}
=0.
$$

The method assigns each encountered one a contribution of `num1` and each zero a contribution of `-num2`. A substring has the desired ratio exactly when the sum of its contributions is zero.

**Use prefix scores to describe every substring**

After scanning a prefix of `s`, the code has counts `n0` and `n1`. Its score is

`x = n1*num1 - n0*num2`.

Consider two prefix boundaries, an earlier one with score $X_a$ and a later one with score $X_b$. The substring between them has weighted balance $X_b-X_a$, because all contributions before the earlier boundary cancel.

That substring has the fixed ratio exactly when its balance is zero, which is equivalent to $X_b=X_a$. The problem has therefore become: count pairs of prefix boundaries with equal scores.

**The empty prefix is a real boundary**

Before reading any characters, both digit counts are zero and the prefix score is zero. The counter starts as `Counter({0:1})` to record this empty prefix.

This initialization is essential for substrings beginning at index zero. If the current prefix itself has the target ratio, its score is zero and `cnt[0]` contributes the empty boundary as its starting point.

For example, with ratio $1:2$, prefix `"011"` has one zero and two ones. Its score is $2\cdot1-1\cdot2=0$, so it matches the empty prefix and is counted.

**Count before inserting the current boundary**

For each character, the solution updates `n0` and `n1`, computes the new score `x`, and adds `cnt[x]` to `ans`. Every earlier boundary with that score gives one distinct non-empty substring ending at the current position.

Only after counting does it execute `cnt[x] += 1`. This order prevents the current boundary from pairing with itself, which would represent an empty substring. It also makes the newly seen boundary available as the start for later substrings.

If the same score has appeared three times before, there are three possible earlier boundaries and hence three different substrings ending here. A set would lose this multiplicity, which is why a frequency map is required.

**Why the character counters are exact**

The expressions `c=='0'` and `c=='1'` produce Boolean values. In Python, `True` acts like integer one and `False` like zero. Because every character is guaranteed to be binary, exactly one of `n0` and `n1` increases on each iteration.

The code could update `x` directly by adding `num1` for a one and subtracting `num2` for a zero. Keeping explicit counts instead makes the ratio derivation visible and produces the same score.


Take any ratio substring. Its start and end determine two prefix boundaries. The substring's cross-multiplied balance is zero, so those boundaries have equal scores. When the later boundary is processed, the earlier one is already recorded and contributes one to the answer.

Conversely, every contribution from `cnt[x]` chooses an earlier boundary with the same score as the current one. Their difference has zero weighted balance, which rearranges to the required zero-to-one ratio. Since the earlier boundary is strictly earlier, the substring is non-empty.

Each substring has a unique pair of boundaries, so it is counted exactly once.

**Why coprimality is not used explicitly**

The contract says `num1` and `num2` are coprime, so they express the ratio in lowest terms. The cross-multiplication test remains correct even without explicitly computing a greatest common divisor. A valid substring may contain any positive multiple of those base counts, such as two zeros and four ones for ratio $1:2$.

A non-empty binary substring cannot satisfy the positive ratio with zero occurrences of one digit, because both ratio parts are at least one. The weighted equality naturally rejects such a substring.

## Complexity detail

Let $n=\lvert s\rvert$. The loop processes each character once. Counter lookup and update take expected $O(1)$ time, so total expected time is $O(n)$.

There can be $O(n)$ distinct prefix scores, each stored with a frequency, giving $O(n)$ auxiliary space.

The number of substrings can reach $n(n+1)/2$, which is larger than a 32-bit signed integer for $n=10^5$. Python integers grow as needed.

## Alternatives and edge cases

- **Direct running score:** Update one balance variable instead of storing `n0` and `n1`. It uses the same map and proof.
- **Enumerate all substrings:** Maintaining counts for every start still costs $O(n^2)$ time.
- **Normalize every substring with gcd:** It repeats expensive work and is unnecessary because cross-multiplication tests the ratio exactly.
- **Substring beginning at zero:** The preloaded empty-prefix score counts it.
- **Non-empty requirement:** Looking up before inserting the current score prevents pairing a boundary with itself.
- **Many equal scores:** Every earlier occurrence must contribute, so use frequencies rather than a set.
- **All zeros or all ones:** No non-empty substring can meet a ratio with both positive parts, and the answer remains zero.
- **Ratio multiples:** Counts such as $2\cdot\texttt{num1}$ and $2\cdot\texttt{num2}$ are valid.
- **Large answer:** Use an integer type capable of holding a quadratic count.
- **Coprime inputs:** No reduction step is required inside the algorithm.

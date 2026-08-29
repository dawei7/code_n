## General

**The two character choices can be optimized independently.** The desired value is

$$
\operatorname{freq}(a_1)-\operatorname{freq}(a_2),
$$

where the first frequency is odd and the second is even. To maximize a subtraction, choose the largest allowed first term and the smallest allowed second term. Therefore, the answer is

$$
\max(\text{positive odd frequencies})
-
\min(\text{positive even frequencies}).
$$

The source first builds `Counter(s)`. This dictionary contains one entry for each character that actually appears, with its positive frequency.

It initializes `a = 0` as the largest odd frequency seen so far and `b = inf` as the smallest even frequency seen so far. For every counter value `v`:

- if `v % 2` is nonzero, `v` is odd and may increase `a`;
- otherwise, `v` is even and may decrease `b`.

The constraints guarantee at least one appearing character with an odd frequency and at least one with an even frequency. Consequently, `a` and `b` are both replaced by real frequencies before `a - b` is returned.

For `"aaaaabbc"`, the frequencies are $5$ for `a`, $2$ for `b`, and $1$ for `c`. The largest odd frequency is $5$, the smallest even frequency is $2$, and the difference is $3$.

**Absent letters are not candidates.** A lowercase letter not present in `s` has mathematical count zero, which is even. However, the task asks for frequencies of characters in the string, and the guarantee about an even-frequency character refers to an appearing character. `Counter(s).values()` deliberately excludes absent letters, so zero cannot be chosen as `freq(a2)`. Including all 26 letters with zero counts would incorrectly make the smallest even frequency zero for almost every input.

**Why maximum odd and minimum even always form a valid pair.** The parity classes are disjoint, so the same character cannot supply both terms. Any character attaining the largest odd frequency can be used as $a_1$, and any character attaining the smallest positive even frequency can be used as $a_2$. There is no adjacency, ordering, or distinct-position restriction connecting their choices.

For any other valid pair with frequencies $o$ and $e$,

$$
o\le a
\quad\text{and}\quad
e\ge b.
$$

Subtracting these inequalities gives $o-e\le a-b$. Thus the source's pair achieves a difference at least as large as every alternative.

**The maximum difference may be negative.** For example, the largest odd count could be $1$ while the smallest even count is $2$, giving $-1$. The source does not clamp the result to zero, because the task requires choosing one character from each parity class. The least negative valid difference is still the maximum.

Only frequencies matter, not which characters attain them. Ties require no special handling because the method returns the numeric difference rather than the character names.
After processing any prefix of `cnt.values()`, `a` is the greatest odd value in that processed set and `b` is the smallest even value. The update rules preserve those meanings. At the end they are the global extrema, and the independent-choice argument proves their difference is optimal.

The Counter's insertion order is irrelevant. Maxima and minima are commutative, so any traversal order produces the same result.

The variable names `a` and `b` are compact, but their roles are asymmetric: `a` monotonically increases through odd candidates, whereas `b` monotonically decreases through even candidates. Neither stores a character, only the frequency needed by the objective.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and let $\Sigma$ be the lowercase alphabet. Building the counter takes $O(n)$ time. Scanning its at most $26$ values takes $O(\lvert\Sigma\rvert)$, which is constant. Total time is $O(n)$.

The counter stores at most $26$ entries. Because the alphabet size is fixed, auxiliary space is $O(1)$ with respect to $n$. More generally, it is $O(\lvert\Sigma\rvert)$.

## Alternatives and edge cases

- **Try every character pair:** At most $26^2$ checks are still constant, but independently selecting the two extrema is simpler and proves optimality directly.
- **Count into a 26-slot array:** This avoids a dictionary and has the same asymptotic bounds, but zero entries must be skipped so absent letters are not treated as even-frequency candidates.
- **Use the largest even frequency:** That would make the subtraction smaller. The even term must be minimized.
- **Use the smallest odd frequency:** That also moves the objective in the wrong direction. The odd term must be maximized.
- **Absent characters:** Their zero counts are excluded; only positive frequencies stored by `Counter` participate.
- **Negative result:** It is valid and must not be replaced by zero.
- **Several tied characters:** Any tied character realizes the same numeric optimum, and the output does not request their identities.
- **Guarantee dependency:** Without an odd or even appearing frequency, the sentinels would remain invalid. The implementation relies on the explicit input guarantee.
- **Single scan after counting:** Frequencies do not change, so no repeated passes over the original string are needed.
- **Lowercase-only alphabet:** The constant-space claim uses the fixed 26-character domain.

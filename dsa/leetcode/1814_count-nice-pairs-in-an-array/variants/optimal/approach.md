## General

**Rearrange the pair equation into one per-number signature**

A pair $(i,j)$ is nice when

$$
\texttt{nums}[i]+\operatorname{rev}(\texttt{nums}[j])
=
\texttt{nums}[j]+\operatorname{rev}(\texttt{nums}[i]).
$$

Move each number's own reverse to the same side:

$$
\texttt{nums}[i]-\operatorname{rev}(\texttt{nums}[i])
=
\texttt{nums}[j]-\operatorname{rev}(\texttt{nums}[j]).
$$

Define the signature

$$
f(x)=x-\operatorname{rev}(x).
$$

Then a pair is nice exactly when both values have the same signature. The original two-index equation has become an equality-group counting problem.

**Reverse a nonnegative integer numerically**

Helper `rev(x)` starts `y = 0`. While `x` is nonzero:

1. `x % 10` extracts its final digit;
2. `y = y * 10 + digit` appends that digit to the reversed value;
3. `x //= 10` removes the processed digit.

For 120, the steps build 0, then 2, then 21. The leading zero that would appear in textual `"021"` contributes no numerical value, so returning 21 matches the definition.

For input zero, the loop runs zero times and returns zero.

**Count how many numbers share each signature**

The generator `x - rev(x) for x in nums` computes one signature per array position. `Counter` maps every signature to its occurrence count.

Signatures may be negative. For example, a number whose reverse is larger produces a negative difference. Hash-map keys handle positive, zero, and negative integers uniformly.

Only signature equality matters; two different original values can and often do share one key.

**Convert a group size into index-pair count**

If one signature appears $v$ times, any two distinct positions in that group form a nice pair. The number of unordered index pairs is

$$
\binom{v}{2}=\frac{v(v-1)}{2}.
$$

The solution sums this expression over every Counter value. Groups are disjoint, so no pair is counted twice.

Modulo $10^9+7$ is applied after the full sum. Python integers can hold the exact intermediate count, so reducing after every group is unnecessary.

**Following the first example**

For 42, the reverse is 24 and the signature is 18. For 97, the reverse is 79 and the signature is also 18. Their group size two contributes one pair.

For 11 and 1, both signatures are zero because each equals its reverse. That group also contributes one pair.

No other signature group has size at least two, so the total is two.

**Why Counter aggregation is equivalent to streaming**

One could scan left to right and, for each signature, add how many equal signatures have appeared earlier. The final Counter formula gives the same result in aggregate: a group of size $v$ contributes `0 + 1 + ... + (v - 1)`, which equals $v(v-1)/2$.

The exact source chooses the shorter two-phase Counter formulation.

**Why the result is correct**

Algebra proves that nice-pair status is equivalent to signature equality. Counter partitions all indices into exactly those equality classes.

Within a class, every two indices form a nice pair; across different classes, none do. Summing the combination count for each class therefore counts every valid $i<j$ pair once and no invalid pair.

## Complexity detail

Let $n$ be the array length and let

$$
T=\sum_{x\in\texttt{nums}}\max(1,\text{number of decimal digits of }x).
$$

Reversing all values costs $O(T)$ time. Counter construction is expected $O(n)$, and summing at most $n$ Counter values is $O(n)$. Exact total expected time is $O(T+n)=O(T)$.

Because each input has at most ten decimal digits under the $10^9$ bound, $T=O(n)$, so time is linear. The manifest's `O(D)` can be read with $D$ as total processed digits; treating fixed-width integer operations as constant also gives $O(n)$.

The Counter can store $n$ distinct signatures, using $O(n)$ auxiliary space, matching the manifest.

## Alternatives and edge cases

- **Streaming hash count:** Add the previous frequency before incrementing each signature. It avoids a separate final combination pass but has the same bounds.
- **Check every pair:** Direct equation testing costs $O(n^2)$ and is too slow.
- **Sort signatures:** Equal runs can be counted after $O(n\log n)$ sorting, slower than expected-linear hashing.
- **String reversal:** Converting to text is valid but numeric reversal makes dropped trailing zeros explicit.
- **Input zero:** Its reverse and signature are both zero.
- **Trailing zeros:** They disappear from the reversed numerical value, as required.
- **Palindromic number:** Its signature is zero and it pairs nicely with every other zero-signature value.
- **Negative signature:** It is a normal Counter key and needs no special handling.
- **All signatures distinct:** Every group size is one and contributes zero.
- **All signatures equal:** The answer before modulo is $n(n-1)/2$.
- **Duplicate input values:** They necessarily share a signature and their distinct indices form pairs.
- **Modulo timing:** Applying it once at the end is safe in Python.
- **Index order:** Each unordered combination corresponds to exactly one ordered condition $i<j$.
- **Input preservation:** The helper consumes only its local copy of each integer; `nums` is unchanged.

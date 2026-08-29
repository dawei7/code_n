## General

The score at index $i$ needs only one fact about the suffix: how many even values and how many odd values remain to the right.

The exact source first counts both parity classes in the entire array. It then scans from left to right, removes the current value from those totals, and reads the count of the opposite class. After removal, the counters represent exactly the strict suffix.

**Encoding parity as zero or one**

For an integer $x$:

$$
x\mathbin{\&}1
=
\begin{cases}
0,&x\text{ is even},\\
1,&x\text{ is odd}.
\end{cases}
$$

The two-element list `cnt` uses that bit directly as an index:

- `cnt[0]` is the number of even values;
- `cnt[1]` is the number of odd values.

The first loop visits every `x` and increments `cnt[x & 1]`. At its end, the list describes the whole array.

**Converting whole-array counts into suffix counts**

At the beginning of forward iteration $i$, the counters still include `nums[i]` and every value to its right, while earlier values have already been removed.

The source first executes

```text
cnt[x & 1] -= 1
```

After this decrement, `cnt` contains exactly the values at indices $j>i$:

$$
\texttt{cnt}[0]
=
\#\{j>i:\texttt{nums}[j]\text{ is even}\},
$$

$$
\texttt{cnt}[1]
=
\#\{j>i:\texttt{nums}[j]\text{ is odd}\}.
$$

This order matters. Reading the opposite count first would not change the numerical answer for the current value—because the current value belongs to its own parity rather than the opposite one—but decrementing first establishes the clean strict-suffix invariant and makes the reasoning direct.

**Selecting the opposite count**

XOR with one flips a parity bit:

$$
0\mathbin{\hat{}}1=1,
\qquad
1\mathbin{\hat{}}1=0.
$$

The source reads

```text
cnt[x & 1 ^ 1]
```

Python evaluates `&` before `^`, so this is

```text
cnt[(x & 1) ^ 1]
```

For a current even value, the expression selects `cnt[1]`, the number of odd suffix values. For a current odd value, it selects `cnt[0]`, the number of even suffix values.

Every one of those suffix values has opposite parity, and no same-parity value is included. That count is exactly `ans[i]`.

**A loop invariant**

Immediately after decrementing at index $i$, `cnt` records parity frequencies in subarray `nums[i + 1..n - 1]`.

This is true at $i=0$ because the counters began with the whole array and the source removed `nums[0]`. If it holds after index $i$, then the next iteration begins with counts for `nums[i+1..]`; removing `nums[i+1]` leaves `nums[i+2..]`. Thus it remains true throughout the scan.

The selected opposite-parity entry therefore gives the exact score at every index.

**Example**

For `nums = [1,2,3,4]`, total counts begin as two evens and two odds.

- At index 0, remove odd 1. The suffix has two evens and one odd, so the opposite count is 2.
- At index 1, remove even 2. The suffix has one even and one odd, so the opposite count for an even current value is 1.
- At index 2, remove odd 3. The suffix contains one even, so the score is 1.
- At index 3, remove even 4. Both counts are zero, so the score is 0.

The answer is `[2,1,1,0]`.

**Why values themselves do not matter**

Unlike the related problem that also asks for smaller values, this score has no magnitude comparison. Once parity is known, every opposite-parity suffix element qualifies regardless of whether its value is larger, smaller, or equal in magnitude.

The two counters therefore contain all information required. No sorting, ordered multiset, coordinate compression, or range tree is necessary.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The source makes one pass to count total parity frequencies and one pass to produce scores. Each pass performs constant work per element.

Total time is

$$
O(N).
$$

The `cnt` list always contains exactly two integers, so working auxiliary space is

$$
O(1).
$$

The returned `ans` array has $N$ entries and requires $O(N)$ output space. The manifest's $O(1)$ space refers to auxiliary working state rather than required output.

The manifest summary says the algorithm scans from right to left while counting values already seen. That is an equally valid design, but it is not what the checked-in source does. The source uses whole-array counts followed by a left-to-right decrementing scan.

The input array is not modified.

## Alternatives and edge cases

- **Right-to-left scan:** Start both counts at zero, answer from the opposite count, then add the current value. This matches the manifest summary and has the same bounds.
- **Quadratic pair checking:** Testing every $i,j$ pair costs $O(N^2)$ and stores no useful reusable suffix summary.
- **Suffix parity arrays:** Precomputing even and odd counts for every suffix works in $O(N)$ time but uses $O(N)$ extra storage instead of two mutable totals.
- **Single element:** Removing it leaves both counters zero, so its score is zero.
- **All values even:** The odd counter is always zero, and every score is zero.
- **All values odd:** The even counter is always zero, and every score is zero.
- **Alternating parity:** Scores decrease according to how many opposite-class positions remain, and the counters track them exactly.
- **Repeated values:** Magnitude and distinctness are irrelevant; each index contributes one occurrence to its parity count.
- **Last index:** Its decrement empties the represented suffix, so its answer is always zero.
- **Expression precedence:** The source relies on `&` binding before `^`; explicit parentheses would improve readability without changing behavior.
- **Positive-value constraint:** The low-bit parity test also works for zero and Python negative integers, though only positive values are required.
- **Manifest/source traversal difference:** Both directions are linear, but the explanation follows the actual left-to-right decrement strategy.

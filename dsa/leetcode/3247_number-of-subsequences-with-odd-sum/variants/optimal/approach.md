## General

**The all-even case**

If every array value is even, every possible subsequence sum is even. The answer is then zero, so first scan for at least one odd element.

**Pair subsequences by toggling one odd index**

Suppose an odd element exists, and fix one particular odd index $p$. Consider all $2^n$ index subsets, including the empty subset. Pair each subset with the subset obtained by toggling whether $p$ is selected.

The two subsets in a pair differ by exactly one odd value, so their sums have opposite parity. Consequently, every pair contains one even-sum subset and one odd-sum subset. The toggle is its own inverse, so no subset is omitted or placed in two pairs. Exactly half of all subsets therefore have odd sum:

$$
\frac{2^n}{2}=2^{n-1}.
$$

The empty subset belongs to the even half, so counting all odd subsets already matches the required nonempty subsequences. Compute $2^{n-1}$ with modular exponentiation.

## Complexity detail

Finding whether any odd value exists takes $O(n)$ time. Modular exponentiation takes $O(\log n)$ time, which is dominated by the scan, so total time is $O(n)$. Only constant-sized counters and the modulus are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Parity dynamic programming:** Tracking current even- and odd-sum subsequence counts also takes $O(n)$ time, but the toggle bijection reduces the state to one existence check.
- **Track counts by subsequence length:** This is correct but performs $O(n^2)$ work for information the answer does not request.
- **Enumerate index subsets:** Direct enumeration takes $O(2^n)$ time and is infeasible at the maximum length.
- A single odd element produces one valid subsequence.
- A single even element produces zero valid subsequences.
- When any odd value exists, the answer depends only on $n$, not on how many values are odd.
- Equal values at different indices remain distinct subsequence choices.
- Large values matter only through parity.
- The modulo must be applied to the power rather than constructing the full exponential integer.

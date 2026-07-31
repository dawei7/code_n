## General

**Use the final value as the state**

Let $D(x)$ be the decimal digit sum of $x$, and let `ways[x]` count valid prefixes whose last value is exactly $x$. For the first requested digit sum, `ways[x]` is `1` when $D(x)$ matches and `0` otherwise: every matching value creates exactly one length-one array.

Suppose `ways` is correct through position $i-1$. A prefix ending at value $y$ may be extended with $x$ exactly when $y\le x$, because that is the complete non-decreasing condition at the new boundary. If $D(x)$ matches the next request, the transition is therefore

$$
\texttt{next[x]}=\sum_{0\le y\le x}\texttt{ways[y]}.
$$

If the digit sum does not match, `next[x]` remains zero.

**Turn every transition into one prefix scan**

Evaluating that sum separately for every $x$ would repeat nearly the same work. Scan the permitted values from `0` through `5000` while maintaining the running sum of `ways[0]` through `ways[x]`. Whenever the current value has the required digit sum, copy that running total into `next[x]`. Reduce the running total modulo $10^9+7$, then replace the previous row after the scan.

The initialization counts every valid one-element prefix exactly once. Inductively, assume `ways[y]` counts exactly the valid prefixes ending at $y$. The prefix total used for `next[x]` includes all and only prefixes whose final value can legally precede $x$; appending $x$ is a one-to-one extension, and the digit-sum check admits exactly the required values. Thus the next row counts every valid prefix once. After the final position, summing all ending states gives exactly the number of complete valid arrays.

## Complexity detail

Let $n=\lvert\texttt{digitSum}\rvert$ and $U=5001$, the size of the permitted value universe. Precomputing all decimal digit sums takes $O(U)$ time. Each of the $n$ positions scans the universe once, so the total time is $O(nU)$. Two arrays of $U$ counts plus the digit-sum table use $O(U)$ auxiliary space.

The benchmark defines size as $n$ and holds the four possible digit-sum-`1` values fixed. Its tiers contain `4`, `12`, and `32` positions. Both the accepted dense prefix DP and an independent sparse two-pointer DP scale linearly in $n$. A correct depth-first enumeration of every non-decreasing assignment visits a polynomially growing tree of partial arrays and should fail only the scaling verdict.

## Alternatives and edge cases

- **Sum every predecessor separately:** Computing each transition by looping over every $y\le x$ is $O(nU^2)$ and repeats prefix sums that one running total provides.
- **Enumerate valid arrays:** Trying every compatible value sequence counts the right objects but visits a rapidly growing search tree; even digit sum `1` permits four choices at every position.
- **Sparse candidate lists:** Store only values matching the current and previous requested sums, then merge the sorted lists while accumulating predecessor counts. This is also within $O(nU)$ and can reduce constants, but the dense scan is simpler and has a small fixed universe.
- **Digit sum zero:** Only the value `0` qualifies, and any later requested zero is impossible after a positive chosen value.
- **Unattainable requested sum:** The largest digit sum in `0..5000` is `31`, achieved by `4999`; any larger request immediately makes the answer zero.
- **Upper endpoint:** The value `5000` is legal and has digit sum `5`, so it must not be lost by scanning only four-digit values below the limit.
- **Equal adjacent values:** Non-decreasing permits equality, so a transition includes the predecessor state at the same value rather than only smaller values.

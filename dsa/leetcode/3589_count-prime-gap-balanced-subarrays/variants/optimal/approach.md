## General

First classify every value up to $V=\max(\texttt{nums})$ with the Sieve of Eratosthenes. Extract the positions and values of the prime occurrences, preserving their array order. Nonprime values do not affect a prime minimum or maximum, so a subarray is characterized by the consecutive block of prime occurrences it contains plus the nonprime positions by which its two ends can be extended.

Suppose prime occurrence $i$ is the leftmost prime in a subarray. If the preceding prime is at position $p_{i-1}$ and this prime is at $p_i$, then the subarray's left endpoint has

$$
p_i-p_{i-1}
$$

choices, using $p_{-1}=-1$. Similarly, if occurrence $j$ is the rightmost prime, its right endpoint has $p_{j+1}-p_j$ choices, using $p_m=n$ after the last of $m$ prime occurrences. Therefore every valid prime interval $[i,j]$ represents the product of those left and right gap counts, without double-counting any subarray.

For each rightmost prime $j$, maintain the smallest index $L$ such that the prime values from $L$ through $j$ have maximum minus minimum at most `k`. Two monotonic queues hold indices of candidate minima and maxima. Each new prime removes dominated values from the queue backs. While the range is too wide, advance $L$ and discard an outgoing index when it reaches a queue front. Every prime enters and leaves each queue at most once.

All leftmost primes $i$ from $L$ through $j-1$ then form valid intervals with at least two primes. A prefix sum of the left-gap counts obtains their combined number of left endpoints in $O(1)$:

$$
\sum_{i=L}^{j-1}(p_i-p_{i-1}).
$$

Multiply that sum by the right-gap count for $j$ and add it to the answer. The monotonic-window condition is sufficient because removing primes from the left cannot enlarge the maximum-minus-minimum range, so the valid left indices form one contiguous suffix.

## Complexity detail

Let $n$ be the array length and $V=\max(\texttt{nums})$. The sieve costs $O(V \log\log V)$ time. Extracting primes, forming prefix sums, and sliding the window cost $O(n)$ time because every queue operation is amortized constant time. Total time is $O(V \log\log V+n)$.

The sieve uses $O(V)$ space. Prime positions, prime values, prefix sums, and monotonic queues use $O(n)$ space in the worst case, for $O(V+n)$ auxiliary space overall.

## Alternatives and edge cases

- **Sparse table plus binary search:** Range-minimum and range-maximum queries over prime values can find each farthest valid partner, but preprocessing and searches add logarithmic machinery that the monotonic sliding window avoids.
- **Enumerating all subarrays:** Updating prime extrema for every start and end is $O(n^2)$ and cannot handle the maximum input length.
- **Fewer than two prime occurrences:** No subarray qualifies, even if `k` is very large.
- **Repeated equal primes:** Occurrences at different indices count separately, and a window containing them has prime gap zero.
- **Composite boundary runs:** Nonprimes before the leftmost prime and after the rightmost prime create multiple distinct subarrays and must be included through the gap weights.
- **Zero tolerance:** When `k = 0`, only windows whose prime values are all equal are valid.
- **Input preservation requirement:** The native source stores `(nums, k)` in the requested local variable `zelmoricad` midway through the function.

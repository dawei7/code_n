## General

**Take the largest Fibonacci number that fits**

The optimal strategy repeatedly subtracts the largest Fibonacci number not exceeding the remaining target. This is the Fibonacci version of a greedy decomposition. The special structure of consecutive Fibonacci numbers makes the strategy optimal even though a largest-coin rule does not work for every arbitrary coin system.

The implementation does not build a list of Fibonacci numbers. It first generates one consecutive pair just beyond the target, then reverses the recurrence to walk downward.

**Generate the first Fibonacci number larger than the original target**

The variables start as:

```python
a = b = 1
```

At every iteration of the first loop:

```python
a, b = b, a + b
```

the pair advances from two consecutive Fibonacci numbers to the next consecutive pair. Python evaluates both right-hand expressions from the old values before assigning either new value, so the recurrence is not corrupted.

The loop continues while `b <= k`. When it stops, `b` is the first generated Fibonacci number strictly greater than the original target and `a` is the preceding Fibonacci number. Starting one value too high is convenient because the descending loop can use one uniform check for every candidate.

For `k = 7`, the pair advances through `(1, 2)`, `(2, 3)`, `(3, 5)`, and `(5, 8)`. It stops with `a = 5` and `b = 8`.

**Reverse the recurrence without a stored sequence**

If `a` and `b` are consecutive Fibonacci values, the forward relation is:

$$
b = a + \text{previous}.
$$

Therefore, the previous value is $b-a$. The assignment

```python
a, b = b - a, a
```

moves the pair backward. From `(5, 8)` it produces `(3, 5)`, then `(2, 3)`, then `(1, 2)`.

In the descending loop, `b` is the candidate currently being considered. If it fits:

```python
if k >= b:
    k -= b
    ans += 1
```

the algorithm uses that Fibonacci number once and reduces the remaining target. Regardless of whether it fits, the reverse assignment then proceeds to the next smaller Fibonacci value.

**Why no candidate needs to be used repeatedly**

Suppose the current candidate is $F_i$. Because every larger candidate was already considered and rejected or subtracted, the current remainder is below $F_{i+1}$. If $F_i$ is chosen, the new remainder satisfies:

$$
\text{remainder} < F_{i+1} - F_i = F_{i-1}.
$$

So the remainder is too small not only for another copy of $F_i$, but also for the immediately preceding Fibonacci number $F_{i-1}$. This is why one downward visit per value is sufficient even though the problem permits repeated use.

For `k = 7`, 8 is skipped, 5 is selected, and the remainder becomes 2. The next candidate 3 is too large, then 2 is selected and the remainder becomes zero. `ans` is two.

**Why the greedy decomposition exists**

The descending process can always finish because 1 is a Fibonacci number. If a positive remainder survives all larger candidates, the final candidate one can reduce it. More strongly, the remainder-shrinking property produces a sum of distinct, nonconsecutive Fibonacci numbers. This is the canonical Fibonacci representation often called Zeckendorf's representation.

**Why the number of terms is minimal**

The canonical representation is not just valid; it uses no more terms than any representation with repetitions. One way to understand this is through normalization.

If a representation contains consecutive Fibonacci numbers, they can be replaced by their next Fibonacci number:

$$
F_i + F_{i+1} = F_{i+2}.
$$

That preserves the sum and reduces the number of terms by one. Repeated equal terms can also be rewritten through Fibonacci identities into terms with larger indices without increasing the number of terms; continuing these exchanges eventually either creates consecutive terms that combine or reaches a representation with distinct, nonconsecutive indices.

The unique fully normalized representation is exactly the one produced by repeatedly taking the largest value that fits. Since the normalization process never increases the term count, the greedy representation cannot use more terms than an alternative representation. Therefore, `ans` is minimal.

There is also a local capacity intuition. Once $F_i$ is the largest value not exceeding the remainder, refusing it forces the same amount to be assembled from smaller pieces. No smaller Fibonacci number is larger than $F_{i-1}$, and the greedy remainder after taking $F_i$ falls below $F_{i-1}$. Choosing the largest term handles as much of the target as possible without creating a future penalty.

**Termination details**

The second loop is `while k`, so it runs until the remaining target is exactly zero. On the iteration that subtracts the final needed value, the code still performs one reverse-pair update before the condition is checked again. That harmless update does not alter `ans` or the zero remainder.

The two initial Fibonacci ones do not cause an error. Near the bottom of the sequence, the pair can become `(1, 1)`. One candidate one is sufficient because the greedy representation never needs duplicate ones; after subtraction, the remainder is zero.

## Complexity detail

Fibonacci numbers grow exponentially with their index. The number of Fibonacci values not exceeding $k$ is therefore $O(\log k)$. The first loop advances through that many values, and the second loop walks back through at most the same number. Each iteration performs constant-time arithmetic, so total time is $O(\log k)$.

The exact code stores only `a`, `b`, `ans`, and the changing remainder `k`. Its auxiliary space is $O(1)$. The manifest's $O(\log k)$ space is a valid loose upper bound, but it would be tight for an alternative that stores the generated sequence in a list; this implementation specifically avoids that list by reversing the recurrence.

## Alternatives and edge cases

- **Store all Fibonacci numbers:** Generate a list through $k$, then traverse it backward greedily. It has the same $O(\log k)$ time but uses $O(\log k)$ space and is simpler to visualize.
- **Repeated binary search:** After each subtraction, binary-search a stored Fibonacci list for the next largest fitting value. It works but adds machinery when a single descending pass already visits candidates in order.
- **Dynamic programming over all totals:** A coin-change DP can find a minimum count, but $k$ can be $10^9$, making $O(k)$ time and space impractical.
- **Breadth-first search of sums:** Exploring every reachable sum by number of terms also grows with $k$ and ignores the Fibonacci structure.
- **Arbitrary coin-system intuition:** Greedy is not universally optimal for coin change. Its correctness here depends on Fibonacci normalization and should not be generalized without proof.
- **`k = 1`:** Generation moves just beyond one, the descending scan selects one, and the answer is one.
- **`k` is Fibonacci:** All larger values are skipped, that value is subtracted once, and the result is one.
- **Remainder skips an adjacent Fibonacci:** After selecting $F_i$, the remainder is below $F_{i-1}$, so the next candidate cannot be selected.
- **Duplicate Fibonacci one:** Although the mathematical sequence begins with two ones, they represent the same usable value. The greedy sum never requires taking both copies.
- **Large target:** Only logarithmically many Fibonacci values are generated for `k <= 10^9`.

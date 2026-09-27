# Guided Example: Number of Subarrays With GCD Equal to K

## 1. The representative instance

We work the official instance `nums = [9, 3, 1, 2, 6, 3]` with `k = 3`: how many of its subarrays have greatest common divisor exactly $3$?

A subarray is a contiguous block, so an array of length six has $6 + 5 + 4 + 3 + 2 + 1 = 21$ subarrays. Grouping them by length shows where the answer comes from.

| Subarray length | Subarrays of that length | With gcd exactly $3$ | Which ones |
|:---:|:---:|:---:|:---|
| 1 | 6 | 2 | `[3]` at index 1 and `[3]` at index 5 |
| 2 | 5 | 2 | `[9, 3]` at indices 0-1 and `[6, 3]` at indices 4-5 |
| 3 | 4 | 0 | the first three contain the value $1$ at index 2; the last is gcd(2, 6, 3) = 1 |
| 4 | 3 | 0 | every one of them contains index 2 |
| 5 | 2 | 0 | every one of them contains index 2 |
| 6 | 1 | 0 | the whole array contains index 2 |

Four subarrays qualify, so the answer for this instance is $4$.

The interesting part is not the enumeration but the fact that the gcd of a growing block changes in a highly constrained way, which is what lets a scan stop early instead of examining all 21 blocks.

## 2. The running gcd and its divisor chain

Fix the left end $i$ and let $G(i, j) = \gcd(\texttt{nums}[i..j])$. Extending the block by one element gives

$$
G(i, j+1) = \gcd\bigl(G(i, j), \texttt{nums}[j+1]\bigr),
$$

and the right-hand side always divides $G(i, j)$. Two consequences drive the whole method.

**The chain never increases.** Every later value divides the current one, so it can only stay where it is or drop to a proper divisor. A block whose gcd already equals $k$ can therefore keep equal to $k$ — as long as each new element is a multiple of $k$ — but it can also fall below.

**A value that does not admit $k$ as a divisor is a dead end.** If $k$ does not divide the current running value, then no extension can produce gcd exactly $k$, because every future value divides the current one. That is the early exit: the scan abandons this left end instead of walking to the end of the array.

The drop is also fast. Each strict decrease moves to a proper divisor, so the value at least halves, which bounds the number of distinct values in any chain by $\lfloor \log_2 V \rfloor + 1$ where $V$ is the largest array value. With values up to $10^9$ that is at most about thirty distinct values per left end.

| Left end $i$ | Running gcd as the right end advances | Distinct values | Why the scan ends here |
|:---:|:---|:---:|:---|
| 0 | 9, 3, 1, 1, 1, 1 | 9, 3, 1 | the value $1$ reached at $j = 2$ does not admit $3$ |
| 1 | 3, 1, 1, 1, 1 | 3, 1 | the value $1$ reached at $j = 2$ does not admit $3$ |
| 2 | 1, 1, 1, 1 | 1 | the very first value already fails |
| 3 | 2, 2, 1 | 2, 1 | the value $2$ does not admit $3$ |
| 4 | 6, 3 | 6, 3 | $6$ admits $3$, so the chain must continue; it lands on the target |
| 5 | 3 | 3 | a single element, which is the target |

## 3. Step-by-step execution of the official instance

For each left end the scan carries one accumulator: the gcd of everything from that left end through the current right end. It counts the accumulator whenever it equals $k$, and abandons the left end as soon as the accumulator stops admitting $k$.

| Left end $i$ | Right end $j$ | `nums[j]` | Running gcd after including $j$ | Equals $k$? | Does $k$ divide it? | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | 9 | 9 | no | yes | extend |
| 0 | 1 | 3 | 3 | yes, count 1 | yes | extend |
| 0 | 2 | 1 | 1 | no | no | abandon this left end |
| 1 | 1 | 3 | 3 | yes, count 2 | yes | extend |
| 1 | 2 | 1 | 1 | no | no | abandon this left end |
| 2 | 2 | 1 | 1 | no | no | abandon immediately |
| 3 | 3 | 2 | 2 | no | no | abandon immediately |
| 4 | 4 | 6 | 6 | no | yes | extend |
| 4 | 5 | 3 | 3 | yes, count 3 | yes | right end reached the end of the array |
| 5 | 5 | 3 | 3 | yes, count 4 | yes | right end reached the end of the array |

The count reaches $4$, matching the enumeration in section 1. Two rows deserve attention. At left end $3$ the accumulator is $2$ and the scan stops after a single step, because $2$ cannot grow into a multiple of $3$. At left end $4$ the accumulator is $6$, which is *not* the target, yet the scan must continue: $6$ is a multiple of $3$, and $\gcd(6, 3) = 3$. Confusing those two situations is the most common way to break this method.

The trace performs ten gcd evaluations in place of the $21$ blocks the enumeration would inspect.

## 4. Invariant and correctness of the early exit

**Invariant.** At the top of every inner iteration, the accumulator equals $\gcd(\texttt{nums}[i..j])$ for the current left end $i$ and right end $j$. It is established at $j = i$, where the accumulator is `nums[i]` itself, and preserved by the update rule, which is exactly the defining recurrence of the running gcd.

**Soundness.** A subarray is counted only when the accumulator equals $k$, and the invariant says the accumulator is that subarray's gcd. Every counted block therefore has gcd exactly $k$, so the count never exceeds the truth.

**Completeness.** Suppose some block `nums[i..j*]` has gcd exactly $k$. Consider the inner loop for left end $i$. Moving from a shorter prefix to a longer one can only divide the value further, so for every $j \le j^{*}$ the value $\gcd(\texttt{nums}[i..j])$ is a multiple of $\gcd(\texttt{nums}[i..j^{*}]) = k$. In other words $k$ divides every accumulator this left end sees up to $j^{*}$, so the early exit cannot fire before $j^{*}$. The loop reaches $j^{*}$, finds the accumulator equal to $k$, and counts that block. No qualifying block is skipped.

The pruning test is therefore exactly the right one, and its two outcomes are worth separating:

| Running value $g$ | Target $k = 3$ | Does $k$ divide $g$? | Can a longer block from this left end reach $3$? |
|:---:|:---:|:---:|:---|
| 9 | 3 | yes | yes: gcd(9, 3) = 3 |
| 6 | 3 | yes | yes: gcd(6, 3) = 3, even though $6$ is not the target |
| 3 | 3 | yes | yes: it is the target already, and multiples of $3$ keep it there |
| 2 | 3 | no | no: every later value divides $2$, and $2$ is not a multiple of $3$ |
| 1 | 3 | no | no: the same argument with $1$ |

A useful corollary follows from the same divisibility fact: if a block has gcd exactly $k$, then every element of it is a multiple of $k$, and in particular its first element is. A scan may therefore skip any left end whose first value is not a multiple of $k$ — a free filter, though it changes nothing in the worst case where the whole array consists of multiples of $k$.

## 5. Boundary and degenerate instances

The package's authored cases probe the situations where a naive reading of the rule goes wrong.

| Case | `nums` | `k` | Answer | Why |
|:---|:---|:---:|:---:|:---|
| `sample-1` | `[9, 3, 1, 2, 6, 3]` | 3 | 4 | the instance traced in section 3 |
| `sample-2` | `[4]` | 7 | 0 | the single element is not the target, and there is nothing to extend |
| `trial-all-ones` | `[1, 1, 1]` | 1 | 6 | every block of ones has gcd $1$, and there are $3 \cdot 4 / 2 = 6$ blocks |
| `trial-multiples` | `[3, 6, 9]` | 3 | 4 | `[3]`, `[3, 6]`, `[6, 9]` and `[3, 6, 9]` qualify; the singletons `[6]` and `[9]` do not |
| `trial-reset-by-nonmultiple` | `[6, 3, 10, 15]` | 3 | 2 | `[3]` and `[6, 3]` qualify; appending $10$ drops the gcd to $1$ and ends the left end $0$ scan |
| `trial-gcd-emerges` | `[8, 12, 18]` | 2 | 1 | only the whole array: gcd(8, 12) = 4 and gcd(12, 18) = 6, but gcd(8, 12, 18) = 2 |
| `trial-large-values` | `[1000000000, 500000000]` | 500000000 | 2 | the singleton `[500000000]`, and the pair whose gcd is exactly $500000000$ |
| `trial-no-match` | `[2, 4, 6]` | 5 | 0 | no gcd of these values can be $5$, because the first element is not a multiple of $5$ |

`trial-gcd-emerges` is the case that defeats an "inspect every pair" shortcut: the target appears only at full length. `trial-reset-by-nonmultiple` shows the opposite event, where a single element that is not a multiple of $k$ truncates every block that spans it. And `trial-all-ones` is the quadratic worst case in miniature, since with $k = 1$ the early exit never fires.

## 6. Alternative methods and what they cost

| Method | Time | Auxiliary space | What it costs you |
|:---|:---|:---|:---|
| Enumerate all subarrays, compute each gcd from scratch | $\Theta(n^3)$ gcd evaluations | $O(1)$ | correct but cubic; nested prefixes are re-reduced repeatedly |
| Running gcd per left end, as traced here | $\Theta(n^2)$ gcd evaluations in the worst case | $O(1)$ | one accumulator and a counter; the inner scan can still reach the end of the array |
| Running gcd per left end, skipping equal-value runs | $\Theta(n \log V)$ gcd evaluations | $O(\log V)$ for the current chain boundaries | needs the positions where the chain changes value, which the plain loop never records |
| Restrict the left ends to multiples of $k$ | same worst case, usually much less work | $O(1)$ | valid by the corollary in section 4, but useless when every element is a multiple of $k$ |
| Prefix-gcd table or sparse table | $\Theta(n \log n)$ construction, $O(\log n)$ per query | $O(n \log n)$ | answers arbitrary range-gcd queries, far more machinery than a counting pass needs |

The second and third rows are the same idea at two levels of care. The plain loop is preferred when the array is short, because the chain boundaries cost more to maintain than the gcd evaluations they save; the grouped version is preferred when values are large and the inner scans are long.

## 7. Complexity: time and auxiliary space

For left end $i$ the inner loop performs at most $n - i$ gcd evaluations, so the whole pass performs at most

$$
\sum_{i=0}^{n-1} (n - i) = \frac{n(n+1)}{2}
$$

evaluations, which is $\Theta(n^2)$ gcd operations in the worst case. Each evaluation costs $O(\log V)$ bit operations for the Euclidean algorithm — at most about thirty division steps for values up to $10^9$ — so the bit-level bound is $O(n^2 \log V)$.

The quadratic worst case is attained, not merely an upper bound: on `nums = [1, 1, ..., 1]` with $k = 1$ the accumulator equals the target at every step, the early exit never fires, and the pass really does evaluate $n(n+1)/2$ pairs. `trial-all-ones` is that shape at $n = 3$.

Auxiliary space is constant. The scan keeps one accumulator, one counter for the answer, and two loop indices; nothing scales with $n$. That is what distinguishes it from the grouped variant, which keeps the current chain's value-change boundaries and therefore $O(\log V)$ storage — at most about thirty entries, bounded by the divisor-chain argument in section 2 rather than by the array length.

The two bounds together explain the design: the early exit is what keeps the common case far below the quadratic ceiling, the divisor-chain bound is what makes a grouping variant worth writing when values are large, and the constant-space property is what makes the plain loop the right default for this problem.
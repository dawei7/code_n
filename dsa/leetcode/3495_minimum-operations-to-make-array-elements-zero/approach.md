## General

**Measure how many times each individual number must be selected.** One selection replaces $x$ by $\lfloor x/4\rfloor$. Repeating this removes one base-four digit per selection. Positive values fall into bands:

- $1$ through $3$ need one selection;
- $4$ through $15$ need two;
- $16$ through $63$ need three;
- in general, $4^{d-1}$ through $4^d-1$ need $d$ selections.

Call this required count the number's workload. An operation processes two array elements at once, so the interval problem becomes scheduling all individual workloads into pair operations.

**Build a prefix sum of workloads by power-of-four bands.** Helper `f(x)` returns the total workload of all integers from one through $x$.

It starts `p = 1` and depth `i = 1`. At one loop iteration, current band is

$$
[p,4p-1].
$$

The part lying at or below $x$ contains

`min(p * 4 - 1, x) - p + 1`

integers. Each needs `i` selections, so their contribution is `cnt * i`. Multiplying `p` by four and incrementing `i` advances to the next band.

For query interval $[l,r]$, total individual workload is

`s = f(r) - f(l - 1)`.

This prefix difference counts every required divide-by-four step for every integer in the array exactly once.

**Two lower bounds determine the number of pair operations.** Since one operation can perform at most two individual selections, at least

$$
\left\lceil\frac{s}{2}\right\rceil
$$

operations are necessary. The source computes this as `(s + 1) // 2`.

There is another constraint: one array element can be selected at most once in a single operation because the operation chooses two elements. If the largest workload is `mx`, that element alone needs `mx` different operations. Therefore, at least `mx` operations are necessary.

Workload is nondecreasing with numeric value, so the maximum in $[l,r]$ belongs to $r$. The expression

`mx = f(r) - f(r - 1)`

extracts exactly the individual workload of $r$ from the prefix function.

The answer for the query is

`max((s + 1) // 2, mx)`.

**Why these lower bounds are jointly attainable.** Think of each number as a stack containing one unit job per required selection. In each round, take at most one job from each of two different stacks. If no stack holds more than the proposed number of rounds and the total jobs do not exceed twice that number, the jobs can be distributed across those round slots without putting two jobs from the same stack in one round.

Here the proposed number is

$$
T=\max\left(\left\lceil s/2\right\rceil,mx\right).
$$

It provides $2T$ total slots and at least one slot in each of $T$ rounds for the largest stack. Pairing jobs from currently largest remaining stacks realizes the schedule. If only one nonzero element remains in a round, it may be paired with an element already equal to zero; selecting zero leaves it zero and is legal. Thus no extra bound is needed.

For interval `[2,4]`, workloads are $1,1,2$. Total $s=4$, maximum $mx=2$, and both bounds give two operations. For `[2,6]`, workloads are $1,1,2,2,2$, so $s=8$, $mx=2$, and four pair operations are necessary and sufficient.

**Why simulating changed numeric values is unnecessary.** The number of times an element must be selected depends only on its initial power-of-four band. Each selection advances it deterministically one level toward zero. The choice of pairing affects only how efficiently workloads share operations, not their individual sizes.

**Complete correctness argument.** The band prefix function computes every element's exact required selections. Any valid operation schedule must respect both capacity of two selections per operation and one selection per element per operation, giving the two lower bounds. The workload scheduling argument constructs a schedule using their maximum. Therefore, each query contribution is minimal, and summing those independent contributions gives the returned result.

## Complexity detail

For an argument $x$, `f(x)` visits powers $1,4,16,\ldots$ through $x$, so it costs $O(\log_4 x)=O(\log x)$ time and $O(1)$ space.

The source calls `f` three times per query: at $r$, $l-1$, and $r-1$. With $q$ queries and maximum endpoint $R$, total time is $O(q\log R)$ and auxiliary space is $O(1)$, matching the manifest.

The returned sum can be large across $10^5$ intervals, so fixed-width implementations should use 64-bit integers. Python handles arbitrary-size totals.

## Alternatives and edge cases

- **Materialize every integer in every interval:** Endpoints reach $10^9$, so range enumeration is impossible.
- **Simulate division operations:** Workload bands determine selection counts directly; simulation repeats predictable steps.
- **Use only \(\lceil s/2\rceil\):** One very large element cannot receive two selections in one operation, so its individual workload is a second lower bound.
- **Use only the maximum workload:** Many moderate workloads may require more than twice that number of total slots.
- **Binary-length bands:** Dividing by four removes two binary bits, so binary bands work too; power-of-four bands express the source more directly.
- **Endpoint \(r\):** Workload is monotone, making `f(r)-f(r-1)` the interval maximum.
- **Odd total workload:** The final operation uses one useful selection and can pair it with a zero element.
- **Several maximum-workload values:** They can be paired with each other across rounds and remain covered by the same two bounds.
- **Band boundary \(4^d\):** It needs one more selection than $4^d-1$, which the loop's next band handles exactly.
- **Inclusive interval:** Prefix subtraction `f(r)-f(l-1)` includes both endpoints.
- **At least two elements:** The constraint `l < r` ensures a second array element exists for every pair operation, even after it becomes zero.
- **Repeated helper calls:** They change only a constant factor; precomputing band endpoints could share small work but is unnecessary.

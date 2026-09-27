# Guided Example: Number of Distinct Averages

## 1. The repeated extraction process and the instance we trace

The official instance is `nums = [4, 1, 4, 0, 3, 5]`, and the expected answer is $2$. The
description prescribes a strictly sequential process: while the array is not empty, remove
one occurrence of the current minimum, remove one occurrence of the current maximum,
record their average $(a + b)/2$, and repeat. The quantity we must return is not the
sequence of averages but how many *different* values appear in it.

Two facts about this process shape everything that follows.

1. The process is driven entirely by order statistics of the current **multiset**: at each
   step the two removed values are the smallest and largest values still present.
2. When several copies of the minimum or maximum exist, the description explicitly allows
   removing any of them. Values are interchangeable, so the *multiset* remaining after a
   step depends only on the multiset before it, never on which physical copy was chosen.

Together these facts say the process is a deterministic function of the input multiset,
and that the order in which the input is given is irrelevant.

## 2. Sorting converts the process into symmetric pairing

Sort the array once into non-decreasing order and write it as
$s_1 \le s_2 \le \dots \le s_n$. At the first step the minimum is $s_1$ and the maximum is
$s_n$. After both are removed, the smallest remaining value is the old $s_2$ and the
largest is the old $s_{n-1}$: deleting the current extremes simply uncovers the next layer
of the sorted order. Repeating the argument shows that step $k + 1$, counting steps from
$0$, always removes the pair

$$
\bigl(s_{k+1},\; s_{n-k}\bigr), \qquad k = 0, 1, \dots, \tfrac{n}{2} - 1 .
$$

So instead of simulating the removals, we can read the pairs directly off the sorted
array: the $i$-th smallest element is paired with the $i$-th largest. For the traced
instance the sorted array is $[0, 1, 3, 4, 4, 5]$, and the three pairs are fixed.

| Pair index $i$ | `nums[i]` (from the small end) | Partner (same distance from the large end) | Sum | Average | Tie in value with an earlier pair? | Distinct averages so far |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `0` | `5` | $5$ | $2.5$ | no | 1 |
| 1 | `1` | `4` | $5$ | $2.5$ | yes, sum $5$ seen at pair $0$ | 1 |
| 2 | `3` | `4` | $7$ | $3.5$ | no | 2 |

## 3. Step-by-step trace of the official instance

The table below follows the literal wording of the process, showing the remaining multiset
at every stage. It is the same information as the sorted-pair table, read in the order the
process actually consumes it.

| Step | Multiset before the step | Minimum removed | Maximum removed | Sum | Average | Multiset after the step |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| 1 | $\{0, 1, 3, 4, 4, 5\}$ | `0` | `5` | $5$ | $2.5$ | $\{1, 3, 4, 4\}$ |
| 2 | $\{1, 3, 4, 4\}$ | `1` | `4` | $5$ | $2.5$ | $\{3, 4\}$ |
| 3 | $\{3, 4\}$ | `3` | `4` | $7$ | $3.5$ | $\emptyset$ |

The recorded averages are $2.5$, $2.5$, $3.5$, of which only two values are distinct,
which matches the expected output $2$. Note where the two `4`s went: one was removed at
step 2 as the maximum and the other at step 3 as the maximum again. Because the two copies
are interchangeable, the process would produce exactly the same average multiset if the
other copy had been taken first — the pair *values* are what matter, not the indices.

## 4. Counting distinct sums instead of distinct averages

Every average is a sum divided by the same constant $2$. For two sums $u$ and $v$,

$$
\frac{u}{2} = \frac{v}{2} \iff u = v ,
$$

so the number of distinct averages equals the number of distinct sums. That observation
removes the division completely: the arithmetic can stay in the integers, which avoids
producing fractional values and sidesteps any question about comparing them. The
instances below show that the sums and the averages always differ by exactly that halving
and that the distinct counts agree even when the averages are half-integers.

| Instance | Sorted form | Pair sums in process order | Pair averages | Distinct averages |
|:---|:---|:---|:---|:---:|
| `[4, 1, 4, 0, 3, 5]` | `[0, 1, 3, 4, 4, 5]` | $5, 5, 7$ | $2.5, 2.5, 3.5$ | 2 |
| `[1, 100]` | `[1, 100]` | $101$ | $50.5$ | 1 |
| `[0, 2, 3, 7]` | `[0, 2, 3, 7]` | $7, 5$ | $3.5, 2.5$ | 2 |
| `[0, 1, 2, 3, 9, 20]` | `[0, 1, 2, 3, 9, 20]` | $20, 11, 5$ | $10, 5.5, 2.5$ | 3 |
| `[1, 2, 3, 4]` | `[1, 2, 3, 4]` | $5, 5$ | $2.5, 2.5$ | 1 |
| `[1, 1, 0, 0]` | `[0, 0, 1, 1]` | $1, 1$ | $0.5, 0.5$ | 1 |
| `[5, 5, 5, 5, 5, 5]` | `[5, 5, 5, 5, 5, 5]` | $10, 10, 10$ | $5, 5, 5$ | 1 |
| `[0, 0, 50, 75, 100, 100]` | `[0, 0, 50, 75, 100, 100]` | $100, 100, 125$ | $50, 50, 62.5$ | 2 |

The `[1, 2, 3, 4]` row is the cleanest illustration of the mechanism: the array is not
constant, yet every symmetric pair has the sum $5$, so only one average is ever produced.
Distinctness of the *inputs* says nothing about distinctness of the *averages*.

## 5. Why the symmetric pairing is correct

The invariant that justifies reading pairs off the sorted array is:

> After $k$ completed steps, the values still present are exactly
> $s_{k+1}, s_{k+2}, \dots, s_{n-k}$ — the original sorted array with its $k$ smallest and
> $k$ largest entries removed.

The base case $k = 0$ is the sorted array itself. For the inductive step, suppose the
remaining multiset is $s_{k+1}, \dots, s_{n-k}$. Its minimum is $s_{k+1}$ and its maximum
is $s_{n-k}$, so step $k+1$ removes those two values and leaves
$s_{k+2}, \dots, s_{n-1-k}$, which is exactly the claimed form for $k + 1$. The invariant
therefore holds for every step, and it also proves that the pairing never depends on
tie-breaking: even when $s_{k+1} = s_{k+2}$ or $s_{n-k-1} = s_{n-k}$, the multiset of
remaining values is unchanged.

Correctness of the final count follows immediately. A run of the process consumes pairs
$0, 1, \dots, \tfrac{n}{2} - 1$ of the sorted array, and the invariant shows no other pair
can ever be consumed. The set of averages produced is therefore exactly
$\{\, (s_{i+1} + s_{n-i}) / 2 \,\}$, and the number of distinct elements of that set is
what the problem asks for. Since halving is injective on the integers, counting distinct
sums $s_{i+1} + s_{n-i}$ gives the same number.

## 6. Boundary and trap analysis

| Situation | Instance | Trap | What actually happens | Outcome |
|:---|:---|:---|:---|:---|
| Single element (below the stated lower bound of $2$, but present in the package cases) | `[4]` | assume at least one average always exists | no pair is ever formed, so no average is recorded | `0` |
| Exactly two elements | `[1, 100]` | expect a large count because the values are far apart | one step, one average $50.5$ | `1` |
| Duplicates at both extremes | `[1, 1, 0, 0]` | think the two `0`s and two `1`s give two different pairs | the pairs are $(0,1)$ and $(0,1)$; the sum $1$ repeats | `1` |
| All values equal | `[5, 5, 5, 5, 5, 5]` | expect many distinct averages | every pair sums to $10$ | `1` |
| Non-constant but symmetric | `[1, 2, 3, 4]` | expect at least two averages because the values differ | every extreme pair sums to $5$ | `1` |
| All pair sums different | `[0, 1, 2, 3, 9, 20]` | expect the third pair to repeat the second's average | sums are $20, 11, 5$; three distinct averages | `3` |
| Half-integer averages | `[0, 2, 3, 7]` | assume averages must be integers to be counted | the values $2.5$ and $3.5$ are perfectly legal averages | `2` |
| Boundary values $0$ and $100$ | `[0, 0, 50, 75, 100, 100]` | treat a repeated extreme value as a new average | the extreme pair contributes the same sum twice; only $125$ is new | `2` |

The general lesson from the middle rows is that the answer is a property of the *pair
sums*, not of the input values. Two arrays with completely different elements can yield
the same count, and an array with many distinct elements can yield the smallest possible
count.

## 7. Alternatives and why the sorted pairing is preferred

| Approach | Idea | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Literal simulation with repeated scans | re-scan the array for the minimum and maximum on every step and delete them | $O(n^{2})$ time, $O(n)$ space | correct, but it recomputes order statistics that sorting settles once; needlessly slow on repeated values |
| Two-heap or balanced-tree simulation | keep the elements in structures that expose the current minimum and maximum | $O(n \log n)$ time, $O(n)$ space | correct and online, but far more machinery than the pairing needs, since no element is ever inserted after the start |
| Enumerate every tie-breaking choice | branch on which equal minimum or maximum is removed and collect all outcomes | exponential in the number of ties | produces exactly the same multiset of averages in every branch; the branching can never change the count |
| Sort once, pair the extremes, collect the sums | sort, walk $i$ from the small end and $n - 1 - i$ from the large end, count distinct sums in a hash set | $O(n \log n)$ time, $O(n)$ space | the method used here: one sort, $\tfrac{n}{2}$ additions, and no division at all |
| Sort once, collect average values as fractions | keep the averages as exact rationals and deduplicate them | $O(n \log n)$ time, $O(n)$ space | stores twice as much per average and compares two integers per element; the direct sum comparison is strictly simpler |

## 8. Complexity: time and auxiliary space

Let $n$ be the length of `nums`, with $n$ even in the official domain and
$2 \le n \le 100$.

**Time.** Sorting the array dominates: $O(n \log n)$ comparisons. After that, the pairing
walk performs exactly $\lfloor n/2 \rfloor$ iterations, each doing one addition and one
expected $O(1)$ hash-set insertion or lookup, for $O(n)$ expected additional work. The
total is $O(n \log n)$ time. At the constraint maximum this is a few hundred comparisons,
so the bound is comfortable by a wide margin. Deriving the pairing from the sorted order
is what removes the quadratic re-scanning of the literal simulation; the sort is paid once
and then every step's extremes are already known.

**Auxiliary space.** The deduplication set holds at most $\lfloor n/2 \rfloor$ sums, so
$O(n)$ integers. The sort is performed on the input sequence itself and, for a typical
comparison sort implementation, needs up to $O(n)$ temporary storage in the worst case
(and $O(\log n)$ stack space for the recursive descent). No other structure is allocated —
in particular, nothing proportional to the number of *pairs of pairs* is ever built, which
is what keeps the method linear in memory rather than quadratic.
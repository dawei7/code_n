# Guided Example: Count the Number of K-Free Subsets

## 1. The instance and the required count

Counting subsets under a forbidden-difference rule is a counting problem over an independence structure, and the whole difficulty is discovering that the structure is far simpler than it first appears. The instance below is the statement's second example, and it is chosen because it contains a genuine conflict, two isolated values, and therefore the full shape of the answer.

$$
\text{nums} = [2,\ 3,\ 5,\ 8], \qquad k = 5 .
$$

The required outcome is the count $12$.

A k-Free subset may contain no two elements whose absolute difference equals $k$; here that forbidden difference is $5$. Among the four values, the pair $3$ and $8$ is the only pair that differs by exactly $5$, so every subset except those containing both $3$ and $8$ is admissible. There are $2^{4} = 16$ subsets in total and exactly $2^{2} = 4$ of them contain both $3$ and $8$ — the two values may each independently be accompanied by either, neither, or both of $2$ and $5$ — so a first estimate is $16 - 4 = 12$, which agrees with the expected count. The rest of this lesson explains why that subtraction is not the general method, and what replaces it.

## 2. Where a conflict can possibly live

The key observation is a divisibility fact. If two values $a$ and $b$ differ by exactly $k$, then

$$
\lvert a - b \rvert = k \;\Longrightarrow\; k \mid (a - b) \;\Longrightarrow\; a \equiv b \pmod{k}.
$$

Two values can therefore only conflict when they leave the **same remainder** on division by $k$. Values in different remainder classes are automatically compatible with each other, no matter how close their magnitudes are. Sorting the instance and recording remainder classes makes the structure visible immediately.

| Value after sorting | Remainder $x \bmod 5$ | Class it joins | Class contents so far |
|---|---|---|---|
| 2 | 2 | remainder 2 | `[2]` |
| 3 | 3 | remainder 3 | `[3]` |
| 5 | 0 | remainder 0 | `[5]` |
| 8 | 3 | remainder 3 | `[3,8]` |

The classes are `[5]`, `[2]` and `[3,8]`. The value $2$ differs from $5$ by $3$ and from $3$ by $1$, both different from $k$, and that is guaranteed in advance: $2 \equiv 2$ while $5 \equiv 0$ and $3 \equiv 3$, so no value outside the remainder-2 class can ever differ from $2$ by a multiple of $5$.

```mermaid
accTitle: Conflict graph of the traced instance
accDescr: The values 3 and 8 form the only forbidden pair because they differ by k equals 5 and share remainder 3, while the values 2 and 5 are isolated because their remainders differ from every other value's remainder.
graph LR
    B["3, remainder 3"] -->|"difference exactly 5"| D["8, remainder 3"]
    A["2, remainder 2, isolated"]
    C["5, remainder 0, isolated"]
```

## 3. Inside one remainder class, conflicts are local

Now consider a single class with its values in ascending order: $x_1 < x_2 < \dots < x_m$. Every difference $x_j - x_i$ with $j > i$ is a positive multiple of $k$. It follows that two values conflict only when they are neighbours in this order, and only when that neighbouring gap is exactly $k$:

- if $x_{i+1} - x_i = k$, the pair $(x_i, x_{i+1})$ is forbidden;
- if $x_{i+1} - x_i > k$, then it is at least $2k$, and every later gap is positive, so no pair straddling this gap can differ by exactly $k$. The class splits at that gap into **independent components**.

So each class is a disjoint union of chains, and each value has at most two potential partners: $x - k$ and $x + k$. Applied to the instance:

| Class | Sorted values | Consecutive gaps | Gap equals $k$? | Components |
|---|---|---|---|---|
| remainder 0 | `[5]` | none | — | one singleton |
| remainder 2 | `[2]` | none | — | one singleton |
| remainder 3 | `[3,8]` | 5 | yes | one chain of length 2 |

A longer chain shows the same rule with a break in the middle. For the authored instance `[11,1,9,3]` with $k = 2$, every value is odd, so all four share one remainder class; after sorting, the gaps are $2$, $6$ and $2$. The middle gap exceeds $k$, which cuts the class into the two components `[1,3]` and `[9,11]` — whose counts, as the next section shows, multiply to the expected $9$.

## 4. Counting the admissible selections of one chain

Let $f(i)$ be the number of admissible selections from the first $i$ values of a component, in ascending order, including the empty selection. The first two values are determined: $f(0) = 1$, since the empty selection is always admissible, and $f(1) = 2$, since a single value may be taken or left. For $i \ge 2$ the recurrence depends on the gap before the $i$-th value.

| Case | Reasoning about the $i$-th value | Recurrence |
|---|---|---|
| its predecessor is exactly $k$ below it | leaving the $i$-th value out leaves all $f(i-1)$ selections free; taking it forbids taking its predecessor, leaving $f(i-2)$ selections | $f(i) = f(i-1) + f(i-2)$ |
| its predecessor is more than $k$ below it | taking the $i$-th value conflicts with no earlier value at all, so every earlier selection extends in both ways | $f(i) = 2\,f(i-1)$ |

The first case is the familiar non-adjacent-selection recurrence, and it produces Fibonacci numbers rather than powers of two. A chain of three values makes the difference unmistakable; take the authored instance `[1,4,7]` with $k = 3$, whose expected count is $5$.

| $i$ | Value | Gap to predecessor | Recurrence applied | $f(i)$ |
|---|---|---|---|---|
| 0 | none | — | empty selection only | 1 |
| 1 | 1 | — | base case, take or leave | 2 |
| 2 | 4 | 3, equal to $k$ | $f(2) = f(1) + f(0) = 2 + 1$ | 3 |
| 3 | 7 | 3, equal to $k$ | $f(3) = f(2) + f(1) = 3 + 2$ | 5 |

The three admissible selections counted by $f(2)$ are the empty set, `{1}` and `{4}`; from them, $f(3) = 5$ adds the empty-set-plus-$7$ and `{1,7}` extensions while refusing to extend `{4}` with $7$. The three rejected subsets out of the $8$ total are `{4,7}`, `{1,4}` and `{1,4,7}`. Note that this is *not* a simple subtraction of conflicting pairs from $2^{3}$: the pair `{1,7}` is compatible even though both endpoints are adjacent to the middle value, which is why the chain recurrence cannot be replaced by counting forbidden pairs.

## 5. Combining the classes: the product rule

Classes are mutually compatible, so a k-Free subset is exactly an independent choice of one admissible selection per class. Different classes share no elements, so the choices cannot interact, and the total count is the product of the per-class counts.

| Remainder class | Sorted values | Count for that class | Running product |
|---|---|---|---|
| 0 | `[5]` | 2 | 2 |
| 2 | `[2]` | 2 | 4 |
| 3 | `[3,8]` | 3, since $f = 1 + 2$ for a conflicting pair | 12 |

The final running product is $12$, matching the required outcome. Enumerating by class also explains the expected list of admissible subsets: the class `[3,8]` contributes a choice of "neither, only 3, or only 8", the class `[2]` a choice of "neither or 2", and the class `[5]` a choice of "neither or 5", so the $3 \times 2 \times 2 = 12$ combinations are the twelve subsets the statement lists. The combination that selects both $3$ and $8$ is absent, and every combination that selects at most one of them appears.

The independence argument also covers the extremes. With `[1000,1]` and $k = 999$, both values leave remainder $1$, the single gap is exactly $k$, and the count is $1 + 2 = 3$. With the fifty values $1$ through $50$ and $k = 1000$, every value leaves a different remainder, so there are fifty singleton classes and the count is $2^{50} = 1125899906842624$, the largest answer the constraints allow.

## 6. Invariant and correctness of the class decomposition

**Invariant I — remainder separation.** For any two values $a, b$ of `nums`, if $a \equiv b \pmod{k}$ fails, then $\lvert a - b \rvert \ne k$. This follows from the divisibility implication of section 2 and holds for every pair, so no forbidden pair ever spans two classes.

**Invariant II — local conflicts.** Within one class sorted ascending, two values conflict if and only if they are consecutive and their gap is exactly $k$. Consecutive gaps are positive multiples of $k$; a gap larger than $k$ is at least $2k$, and every pair straddling it differs by more than $k$, so only the exact-$k$ gaps create edges. Each class is therefore a disjoint union of paths, which is precisely the structure for which the recurrence of section 4 is defined.

**Correctness of the recurrence.** For the $i$-th value of a component, partition the admissible selections of the first $i$ values by whether they contain that value. Those that exclude it are exactly the admissible selections of the first $i - 1$ values, of which there are $f(i-1)$. Those that include it must exclude every earlier value that conflicts with it; by Invariant II that is only the predecessor when the gap equals $k$, so the remaining choices are exactly the admissible selections of the first $i - 2$ values, of which there are $f(i-2)$; when the gap is larger, no earlier value conflicts and each of the $f(i-1)$ selections extends. The two branches are disjoint and exhaustive, so the recurrences count every admissible selection exactly once. The bases $f(0) = 1$ and $f(1) = 2$ are immediate.

**Correctness of the product.** Map each k-Free subset to the tuple of its intersections with the classes. Each intersection is an admissible selection within its class, by Invariant I and the definition of admissibility; distinct subsets give distinct tuples, because a subset is the union of its intersections; and every tuple of admissible selections assembles into a k-Free subset, because no conflict crosses a class boundary and none exists inside an admissible selection. The map is therefore a bijection between k-Free subsets and tuples of per-class admissible selections, and the number of tuples is the product of the per-class counts. The empty subset corresponds to the all-empty tuple and is counted exactly once, as required.

## 7. Traps this instance exposes

| Trap | The tempting but wrong move | What this instance reveals |
|---|---|---|
| Global pair subtraction | subtract the number of forbidden pairs, or of subsets containing one, from $2^{n}$ | forbidden pairs overlap: the chain `[1,4,7]` has two forbidden pairs but only three bad subsets out of eight, and `{1,7}` is compatible |
| Cross-class conflict | compare every pair of values by magnitude alone | only equal remainders can conflict, which is why $2$ and $5$ never interact even at $k = 3$ |
| Ignoring breaks in a class | treat one remainder class as a single chain | a gap larger than $k$ splits the class, as `[1,3,9,11]` splits into `[1,3]` and `[9,11]` for a count of $3 \times 3 = 9$ |
| Order of processing | group values without sorting them first | adjacency is defined by the sorted order; `[11,1,9,3]` must be sorted before its gaps mean anything |
| Chain recurrence | use $2^{m}$ for a component of $m$ values | a three-value chain counts $5$, not $8$, because selecting the middle value forbids both neighbours |
| Summing instead of multiplying | add the per-class counts | independent classes compose multiplicatively: $2 \times 3 \times 2 = 12$, whereas summing gives $7$ |
| Forgetting the empty subset | count only non-empty selections | every base case starts from $f(0) = 1$, and the expected counts $5$, $12$ and $2$ for a single value all include the empty subset |
| Assuming small answers | treat the count as if it fits a small range | fifty singleton classes give $2^{50}$, so the accumulator must be an exact integer rather than a bounded machine word |

The last row is a consequence of the constraints rather than of the conflict rule: with $n \le 50$ the answer can reach $2^{50}$, and the multiplication must stay exact while it grows.

## 8. Complexity of the decomposition and the recurrence

Let $n = \text{nums.length}$ with $1 \le n \le 50$ as the statement guarantees.

**Time.** Sorting the values costs $O(n \log n)$ and is the dominant term. The single pass that assigns each value to its remainder class costs $O(n)$. Scanning each class in sorted order to detect exact-$k$ gaps costs one comparison per value, so $O(n)$ overall, and filling the recurrence table costs one constant-time step per value. The total is therefore

$$
O(n \log n)
$$

arithmetic operations, plus the cost of the $O(n)$ multiplications whose operands grow to as much as $2^{50}$; with exact integer arithmetic those multiplications are not constant-time in the strict bit model, but they remain negligible under these constraints.

**Auxiliary space.** The grouping structure holds all $n$ values once, and the recurrence table holds one entry per value of the class currently being processed, so the storage is $O(n)$. No subset is ever materialised: the chain recurrence replaces enumeration of all $2^{n}$ subsets, which for $n = 50$ would be about $10^{15}$ candidates, by a linear scan whose largest intermediate value is the answer itself.

**Why the structure matters.** On a general graph, counting independent sets is intractable in the worst case. Here the forbidden-difference rule forces the conflict graph to be a disjoint union of paths — one path per run of consecutive multiples of $k$ inside a remainder class — and path counting is exactly the two-term recurrence above. Recognising that structure is what turns an exponential enumeration into a sort, a grouping pass, and a product.

# Guided Example: Median of Two Sorted Arrays

We will solve

- **First sorted array:** $A=[1,3,8,12,15]$
- **Second sorted array:** $B=[2,4,6,9,10,11]$
- **Combined length:** $11$

The combined collection has odd cardinality, so its median is the value of rank $6$ in one-based indexing. We will identify that rank without merging the arrays.

## 1. Turn the median into a partition problem

A median boundary divides the combined sorted multiset into a lower part and an upper part. For $11$ values, the lower part must contain

$$
h=\left\lfloor\frac{11+1}{2}\right\rfloor=6
$$

values. Because the total is odd, the lower part owns the median itself.

Choose a cut after $i$ values of $A$. The cut in $B$ is then not independent: it must be after

$$
j=h-i=6-i
$$

values. Every candidate is therefore determined by a single integer $i$.

> **Balanced-size condition:** $i+j=6$.

> **Sorted-boundary condition:** every value left of the cuts must be no greater than every value right of the cuts.

Since each individual array is sorted already, only the four values adjacent to the cuts can violate the second condition.

## 2. Name the four boundary values

For cuts $i$ and $j$, define

| Boundary | Meaning |
|---|---|
| $A_L$ | largest selected value from $A$ |
| $A_R$ | smallest unselected value from $A$ |
| $B_L$ | largest selected value from $B$ |
| $B_R$ | smallest unselected value from $B$ |

A balanced cut is globally sorted exactly when both cross-array inequalities hold:

$$
A_L\le B_R
\qquad\text{and}\qquad
B_L\le A_R.
$$

The first compares the left boundary of $A$ with the right boundary of $B$; the second performs the symmetric check. Internal elements need no further tests because sorted order places them farther from the boundary in the safe direction.

## 3. First candidate: the cut in A is too far left

Binary search starts among the $6$ possible cuts of the shorter array $A$, from $i=0$ through $i=5$. The first midpoint is $i=2$, so $j=4$.

| Array | Left of cut | Cut | Right of cut |
|---|---|:---:|---|
| $A$ | $1,3$ | $\mid$ | $8,12,15$ |
| $B$ | $2,4,6,9$ | $\mid$ | $10,11$ |

The adjacent boundaries are

| $A_L$ | $A_R$ | $B_L$ | $B_R$ |
|---:|---:|---:|---:|
| 3 | 8 | 9 | 10 |

Now evaluate the two necessary inequalities:

| Test | Evaluation | Verdict |
|---|---:|---|
| $A_L\le B_R$ | $3\le10$ | true |
| $B_L\le A_R$ | $9\le8$ | false |

The value $9$ has been placed in the lower half while the smaller value $8$ remains in the upper half. The cut in $A$ is therefore **too far left**: it contributes too few values from $A$.

Increasing $i$ moves $A_R$ to a value no smaller than before and simultaneously decreases $j$, moving $B_L$ to a value no larger than before. Both changes repair the failed inequality monotonically. Consequently every cut $i\le2$ can be discarded.

The remaining search interval is $3\le i\le5$.

## 4. Second candidate: the cut in A is too far right

The next midpoint is $i=4$, which forces $j=2$.

| Array | Left of cut | Cut | Right of cut |
|---|---|:---:|---|
| $A$ | $1,3,8,12$ | $\mid$ | $15$ |
| $B$ | $2,4$ | $\mid$ | $6,9,10,11$ |

| $A_L$ | $A_R$ | $B_L$ | $B_R$ |
|---:|---:|---:|---:|
| 12 | 15 | 4 | 6 |

| Test | Evaluation | Verdict |
|---|---:|---|
| $A_L\le B_R$ | $12\le6$ | false |
| $B_L\le A_R$ | $4\le15$ | true |

Now $12$ lies in the lower half while $6$ lies in the upper half. The cut in $A$ is **too far right**: it contributes too many values from $A$.

Decreasing $i$ moves $A_L$ to a value no larger than before. At the same time, $j$ increases and moves $B_R$ to a value no smaller than before. Thus every cut $i\ge4$ can be discarded.

Only $i=3$ remains.

## 5. Third candidate: certify the balanced partition

Set $i=3$ and $j=3$.

| Array | Left of cut | Cut | Right of cut |
|---|---|:---:|---|
| $A$ | $1,3,8$ | $\mid$ | $12,15$ |
| $B$ | $2,4,6$ | $\mid$ | $9,10,11$ |

| $A_L$ | $A_R$ | $B_L$ | $B_R$ |
|---:|---:|---:|---:|
| 8 | 12 | 6 | 9 |

| Test | Evaluation | Verdict |
|---|---:|---|
| $A_L\le B_R$ | $8\le9$ | true |
| $B_L\le A_R$ | $6\le12$ | true |

Both conditions hold. Exactly six values lie on the left, and no left value exceeds any right value:

| Combined lower half | Combined upper half |
|---|---|
| $1,2,3,4,6,\mathbf{8}$ | $9,10,11,12,15$ |

The lower half contains the extra element, so its maximum is the median:

$$
\operatorname{median}=\max(A_L,B_L)=\max(8,6)=8.
$$

## Search geometry at a glance

| Candidate cut $i$ | Forced cut $j=6-i$ | Failed relation | Geometric meaning | Next action |
|---:|---:|---|---|---|
| 2 | 4 | $B_L>A_R$ | $A$ contributes too few lower-half values | move $i$ right |
| 4 | 2 | $A_L>B_R$ | $A$ contributes too many lower-half values | move $i$ left |
| 3 | 3 | none | partition is balanced and ordered | read median |

This is a binary search over **cut positions**, not over possible median values.

## Why the reasoning is correct

The equation $i+j=6$ establishes the correct cardinality of the lower half. Sorted order inside $A$ and $B$ already guarantees that each array's left segment is no greater than its own right segment. The two cross inequalities supply the only missing comparisons between arrays. When both hold, every lower-half value is no greater than every upper-half value, so the boundary has the correct combined rank.

The failed inequalities are monotone in opposite directions. If $B_L>A_R$, moving the cut in $A$ farther left can only make $A_R$ no larger and $B_L$ no smaller, so it cannot help. If $A_L>B_R$, moving the cut in $A$ farther right can only make $A_L$ no smaller and $B_R$ no larger, so it cannot help. Each failure therefore eliminates an entire half-interval of cut positions.

## Boundary conventions and traps

- **Search the shorter array:** this gives $O(\log(\min(m,n)))$ time and ensures the complementary cut stays within the longer array.
- **Use cut positions, not element indices:** an array of length $m$ has $m+1$ legal cuts, including cuts before its first and after its last element.
- **Preserve the total left size:** changing $i$ must change $j$ in the opposite direction so that $i+j=h$ remains true.
- **Use non-strict inequalities:** duplicate values may legally appear on both sides of the partition.
- **Handle empty partition sides:** a missing left boundary behaves as $-\infty$ and a missing right boundary as $+\infty$.
- **Distinguish odd and even totals:** for an even total, the median is

$$
\frac{\max(A_L,B_L)+\min(A_R,B_R)}{2}.
$$

- **Do not merge first:** merging reveals the full combined order but spends $O(m+n)$ time, which discards the logarithmic advantage supplied by the sorted inputs.

## Cost of the method

There are $m+1$ candidate cuts in the shorter array, and binary search halves that set after every invalid partition. The running time is $O(\log(\min(m,n)))$. Only cut indices and four boundary values are retained, so the auxiliary space is $O(1)$.


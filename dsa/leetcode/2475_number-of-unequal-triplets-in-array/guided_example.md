# Guided Example: Number of Unequal Triplets in Array

## 1. What is being counted, and why index order is not the hard part

We are given a 0-indexed array of positive integers `nums` and must count the
triplets of indices $(i, j, k)$ with

$$
0 \le i < j < k < n, \qquad \text{nums}[i] \neq \text{nums}[j],\quad
\text{nums}[i] \neq \text{nums}[k],\quad \text{nums}[j] \neq \text{nums}[k].
$$

The index constraint and the value constraint pull in opposite directions, and
separating them is the whole lesson. The index condition only says that the three
chosen positions are three *different* positions: for any 3-element set of
indices there is exactly one way to name its members in increasing order as
$(i, j, k)$. So the ordered condition $i < j < k$ is not a filter on top of
"pick three positions" — it is a canonical naming of the pick. Counting valid
triplets is therefore the same as counting **3-element index subsets whose values
are pairwise distinct**.

That reformulation matters because the value condition ignores positions
entirely. Two positions holding the same number can never both appear in a valid
triplet, while positions holding different numbers can always appear together,
whatever their distance. The only structure that survives is the multiset of
values — equivalently, the frequency of each distinct value.

## 2. The representative instance and its index set

The official instance is

| index $i$ | 0 | 1 | 2 | 3 | 4 |
|:---|:---:|:---:|:---:|:---:|:---:|
| `nums[i]` | 4 | 4 | 2 | 4 | 3 |

with the required outcome `3`. The value `4` occupies three positions, so the
array is not a set of values in disguise; the multiplicities are the entire
difficulty of the instance.

An index-subset view enumerates all $\binom{5}{3} = 10$ candidate subsets, which
is small enough to check by hand and shows exactly where the three survivors come
from.

| index subset $\{i,j,k\}$ | values $(\text{nums}[i], \text{nums}[j], \text{nums}[k])$ | pairwise distinct? |
|:---|:---|:---|
| $\{0,1,2\}$ | (4, 4, 2) | no — the two `4`s collide |
| $\{0,1,3\}$ | (4, 4, 4) | no |
| $\{0,1,4\}$ | (4, 4, 3) | no |
| $\{0,2,3\}$ | (4, 2, 4) | no |
| $\{0,2,4\}$ | (4, 2, 3) | yes |
| $\{0,3,4\}$ | (4, 4, 3) | no |
| $\{1,2,3\}$ | (4, 2, 4) | no |
| $\{1,2,4\}$ | (4, 2, 3) | yes |
| $\{1,3,4\}$ | (4, 4, 3) | no |
| $\{2,3,4\}$ | (2, 4, 3) | yes |

Three subsets survive, matching the official answer. The surviving subsets are
$\{0,2,4\}$, $\{1,2,4\}$, and $\{2,3,4\}$, which is exactly the official list of
triplets $(0,2,4)$, $(1,2,4)$, $(2,3,4)$ once each subset is written in
increasing index order. The `4` at index 3 is never useful in this instance: it
can only ever be the third copy of a value that already appears elsewhere.

## 3. Collapsing the array to value frequencies

Since only multiplicities matter, the array is compressed into one row per
distinct value.

| value $v$ | positions holding $v$ | frequency $c_v$ |
|:---:|:---|:---:|
| 2 | 2 | 1 |
| 3 | 4 | 1 |
| 4 | 0, 1, 3 | 3 |

The total is $\sum_v c_v = 5 = n$. A valid triplet must draw its three positions
from three *different* values, so the count is a sum over the 3-element subsets
of distinct values:

$$
\text{answer} = \sum_{\{a,b,d\}} c_a\, c_b\, c_d ,
$$

where the sum runs over all unordered triples of distinct stored values, and
$a, b, d$ denote them. For the instance there is only one such value triple,
$\{2, 3, 4\}$, and its product is

$$
c_2 \cdot c_3 \cdot c_4 = 1 \cdot 1 \cdot 3 = 3 .
$$

The whole difficulty has been moved into a combinatorial identity: choosing one
position from each of three distinct value groups produces an index set with
pairwise distinct values, and every such index set arises exactly once from that
choice. No ordering work is required, because the index order $i < j < k$ is
recovered from the set.

## 4. Accumulating the triple products without enumerating triples of values

Enumerating every triple of distinct values costs $\Theta(d^3)$ for $d$ distinct
values, which is wasteful. Three running accumulators compute the same sum in one
pass if each group is folded in with its own frequency $c$:

- $s_1 = \sum c$ — total positions folded so far,
- $s_2 = \sum_{\{a,b\}} c_a c_b$ — pairs of positions with distinct values seen so far,
- $s_3 = \sum_{\{a,b,d\}} c_a c_b c_d$ — the answer so far.

A new group of size $c$ creates one new triple product with every pair already
counted in $s_2$, and one new pair product with every single position already
counted in $s_1$. Updating from the highest accumulator downward keeps the new
group from pairing with itself:

$$
s_3 \mathrel{+}= s_2 \cdot c, \qquad
s_2 \mathrel{+}= s_1 \cdot c, \qquad
s_1 \mathrel{+}= c .
$$

Processing the instance's groups in ascending value order gives a complete,
readable trace.

| Step | group folded in | $c$ | $s_1$ after | $s_2$ after | $s_3$ after |
|:---:|:---:|:---:|:---:|:---:|:---:|
| start | — | — | 0 | 0 | 0 |
| 1 | value 2 | 1 | 1 | $0 + 0 \cdot 1 = 0$ | $0 + 0 \cdot 1 = 0$ |
| 2 | value 3 | 1 | 2 | $0 + 1 \cdot 1 = 1$ | $0 + 0 \cdot 1 = 0$ |
| 3 | value 4 | 3 | 5 | $1 + 2 \cdot 3 = 7$ | $0 + 1 \cdot 3 = 3$ |

The final accumulator $s_3 = 3$ is the answer. Two details in the table carry the
whole method. First, the row for value 3 adds a pair but no triple, because only
two value groups have been seen — no third distinct value exists yet. Second, the
row for value 4 multiplies the *previous* $s_2 = 1$ by $c = 3$, which is precisely
the single value triple $\{2,3,4\}$ weighted by the three positions holding `4`.

The same accumulator on the authored four-group instance `[1,2,2,3,3,3,4,4,4,4]`
shows the sum building across several value triples at once:

| Step | group folded in | $c$ | $s_1$ | $s_2$ | $s_3$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| start | — | — | 0 | 0 | 0 |
| 1 | value 1 | 1 | 1 | 0 | 0 |
| 2 | value 2 | 2 | 3 | $0 + 1 \cdot 2 = 2$ | 0 |
| 3 | value 3 | 3 | 6 | $2 + 3 \cdot 3 = 11$ | $0 + 2 \cdot 3 = 6$ |
| 4 | value 4 | 4 | 10 | $11 + 6 \cdot 4 = 35$ | $6 + 11 \cdot 4 = 50$ |

The final $s_3 = 50$ equals $1\cdot2\cdot3 + 1\cdot2\cdot4 + 1\cdot3\cdot4 +
2\cdot3\cdot4 = 6 + 8 + 12 + 24$, the four value triples of that instance, and it
matches the authored expectation.

## 5. The invariant and why the accumulation is correct

The accumulators maintain a precise invariant after any prefix of the value
groups has been folded in: $s_t$ equals the elementary symmetric polynomial of
degree $t$ over the frequencies of the prefix, that is, the sum of products of
$t$ distinct group frequencies from the prefix. Taking $s_0 = 1$ as a basis, the
invariant is

$$
s_t = \sum_{\{v_1 < \dots < v_t\} \subseteq \text{prefix}} c_{v_1} \cdots c_{v_t}.
$$

Folding a new group with frequency $c$ must extend the invariant from degree $t-1$
to degree $t$. Every degree-$t$ product over the enlarged prefix either avoids
the new group — already counted in the old $s_t$ — or uses it exactly once, in
which case its remaining $t-1$ factors form a degree-$(t-1)$ product over the old
prefix, contributing $s_{t-1} \cdot c$. Hence $s_t \leftarrow s_t + s_{t-1} c$,
which for $t = 3$ and $t = 2$ is exactly the update used above. Since the
invariant is true before the first group ($s_1 = s_2 = s_3 = 0$ over an empty
prefix) and is preserved by each fold, it holds after all groups, and $s_3$ is by
section 3 the number of valid triplets.

Two consequences follow. The result cannot depend on the order in which groups
are folded, because a symmetric polynomial is invariant under permutation of its
arguments — the descending update order only prevents a group from pairing with
itself. And the count is correct even though no index was ever compared with
another: the bijection between valid index triplets and index subsets carrying
three distinct values is what lets positions be discarded, while the frequencies
preserve exactly the number of ways each value can supply a position.

## 6. Boundary conditions and the traps they expose

| Instance | Situation | What the method computes | Verdict |
|:---|:---|:---|:---|
| `[1,2,3]` | three distinct values, minimum length | one value triple with $1 \cdot 1 \cdot 1$ | 1 |
| `[1,2,1,2,1]` | only two distinct values | $s_3$ never receives a second value group | 0 |
| `[1,1,1,1,1]` | one distinct value, all positions collide | one huge group, no value triple | 0 |
| `[9,7,5,3,1]` | all values distinct | every 3-subset qualifies, $\binom{5}{3}$ | 10 |
| `[1,1,2,2,3,3]` | three groups of equal size | $2 \cdot 2 \cdot 2$ | 8 |
| `[1,2,3,1,2,3,4]` | duplicates interleaved, not adjacent | four value triples, products $8,4,4,4$ | 20 |
| `[4]`, `[4,4]` | fewer than three positions | no 3-subset exists at all | 0 |

The interleaved instance is the one that punishes a positional solution: the two
copies of each of `1`, `2`, and `3` are separated by other values, so a scan that
compared neighbours would see an alternating pattern and misjudge the group
structure. The frequency view is blind to that arrangement, which is exactly why
it is the right representation. The two-element and one-element instances are
boundary cases that the accumulator handles without a special branch: folding a
single group leaves $s_3 = 0$, and a group larger than the remaining positions
contributes only the products that actually exist.

## 7. Alternative formulations

| Formulation | How it counts | Cost | Where it breaks down |
|:---|:---|:---|:---|
| Enumerate all index triples | test the three pairwise inequalities for every $i < j < k$ | $\Theta(n^3)$ | correct but wasteful; it re-tests the same value equality many times |
| Sort, then multiply three group segments | for each pair of group boundaries, multiply left, middle, and right segment lengths | $O(n^2)$ after an $O(n \log n)$ sort | needs both boundaries maintained and is easy to double count or to skip the last group |
| Frequency map plus all value triples | build the counts, then multiply over every triple of distinct values | $O(n)$ expected build plus $\Theta(d^3)$ | collapses when many values appear, even if each appears once |
| Incremental symmetric accumulation (used here) | fold each group once, maintaining $s_1, s_2, s_3$ | $O(n)$ expected with a hash map, $O(d)$ after | none for this problem; the only trap is updating the accumulators in the wrong direction |

The sorted variant is the closest competitor in spirit: sorting makes equal values
adjacent, so segment lengths are read directly from boundaries. But it still pays
a nested loop over boundary pairs, while the accumulator replaces that loop with
three multiplications per group. That is why the accumulator is preferable: it
turns a sum of products into a running state.

## 8. Complexity of the method

Let $n = \texttt{nums.length}$ and let $d$ be the number of distinct values, so
$d \le \min(n, 1000)$ under the stated value range.

- **Time:** grouping the array into frequencies costs $\Theta(n)$ with a hash
  map, or $O(n \log n)$ if the values are sorted first. Folding the $d$ groups
  through the three accumulators costs $\Theta(d)$, a constant number of
  arithmetic operations per group. The total is $O(n)$ expected with hashing, and
  $O(n \log n)$ in the sorted formulation. The cubic enumeration of index
  triples, by contrast, is $\Theta(n^3)$: for $n = 100$ that is on the order of
  $10^6$ iterations with three comparisons each, versus a few hundred hash
  operations for the accumulator.
- **Auxiliary space:** the frequency map holds $d$ counters, so $O(d)$ auxiliary
  space, and the accumulators add only three integers. The sorted formulation
  needs $O(d)$ extra beyond its in-place sort of the input. In both cases the
  working memory is bounded by the number of distinct values, not by the number
  of triplets, which is at most $\binom{n}{3}$.

The last point is the practical lesson of the instance: the output can be cubic
in size while the computation stays linear in the input, because the triple
products are accumulated arithmetically instead of being enumerated.

# Guided Example: Bitwise OR of All Subsequence Sums

The task is to OR together the sums of every subsequence of `nums` and return
the resulting integer. Since a subsequence is any selection of indices in their
original relative order, and addition does not care about order, the answer
depends only on which **multiset** of values a selection produces. The order of
`nums` is therefore irrelevant, and the only question that matters is:

> for each bit position $i$, does at least one subsequence have a sum whose
> $i$-th bit is 1?

OR is a bitwise disjunction, so the answer is determined position by position,
and the positions do not interact. That decomposition is what turns an
exponentially large family of $2^{n}$ subsequences into a linear scan over bit
counts.

## 1. The representative instance

Use the first official example, `nums = [2,1,0,3]`. Write each value in binary to
see which positions it can supply directly.

| Index | Value | Binary | Bits set |
|:---:|:---:|:---:|:---|
| 0 | 2 | 010 | 1 |
| 1 | 1 | 001 | 0 |
| 2 | 0 | 000 | none |
| 3 | 3 | 011 | 0 and 1 |

Reading the table column-wise gives the **direct supply** of each position: two
elements have bit 0 set (the values 1 and 3), two elements have bit 1 set (the
values 2 and 3), and no element has bit 2 or above set. The value 0 has no bit
set at all, which will matter later.

## 2. Which sums are actually reachable

There are $2^{4} = 16$ subsequences, but only seven distinct sums, because the
element 0 adds nothing and because different selections can collide.

| Sum | Binary | One witnessing subsequence | Bits contributed |
|:---:|:---:|:---|:---|
| 0 | 000 | the empty subsequence | none |
| 1 | 001 | the values 1 | 0 |
| 2 | 010 | the value 2 | 1 |
| 3 | 011 | the value 3, or the values 2 and 1 | 0, 1 |
| 4 | 100 | the values 1 and 3 | 2 |
| 5 | 101 | the values 2 and 3 | 0, 2 |
| 6 | 110 | the values 2, 1 and 3 | 1, 2 |

The OR of these seven values is $0 \lor 1 \lor 2 \lor 3 \lor 4 \lor 5 \lor 6 = 7$,
whose binary form is 111: bits 0, 1 and 2 are all present, and no higher bit is.
The required output is therefore $7$, and the interesting part of the lesson is
explaining why those three bits — and only those three — are present.

| Bit position $i$ | Is bit $i$ set in the OR? | Smallest witness sum | Crafted from |
|:---:|:---:|:---:|:---|
| 0 | yes | 1 | the single value 1 |
| 1 | yes | 2 | the single value 2 |
| 2 | yes | 4 | two values, 1 and 3 |
| 3 | no | none exists | every sum is at most 6 |
| 4 | no | none exists | every sum is at most 6 |

## 3. Two ways a bit can be supplied

Look at how bit 2 is produced in this instance. No element has bit 2 set, so no
singleton can supply it. It appears because two elements both have bit 1 set,
and their contributions add as

$$
2 \cdot 2^{1} = 2^{2},
$$

so the pair 1 and 3 carries exactly one unit into position 2. This is the general
mechanism, and it has exactly two forms:

- **Direct supply.** An element with bit $i$ set contributes one unit at
  position $i$ by itself, and taking that element as a singleton subsequence
  makes bit $i$ of the sum equal to 1.
- **Fusion.** Units at lower positions pair up and carry upward. Two units at
  position $i-1$ fuse into one unit at position $i$; in general, $2^{s}$ units at
  position $i-s$ carry up $s$ positions to place one unit at position $i$.

Because every element value is non-negative and the empty subsequence is allowed
to contribute 0, the OR only ever gains bits; a bit is present if **any** legal
selection places a unit there. This is why the algorithm can count supplies
without ever choosing a subsequence explicitly.

## 4. Counting units: the recurrence and its closed form

Let $d_i$ be the number of elements of `nums` whose bit $i$ is set; Section 1
computed $d_0 = 2$, $d_1 = 2$, $d_2 = 0$ for the traced instance. Let $c_i$ be
the number of units available at position $i$ once fusions are accounted for.
Scanning positions upward from 0, every pair of units at position $i$ becomes one
unit at position $i+1$, so

$$
c_0 = d_0, \qquad c_i = d_i + \left\lfloor \frac{c_{i-1}}{2} \right\rfloor .
$$

The floor is essential: units fuse only in whole pairs, and the odd unit left
behind at position $i-1$ is exactly what keeps bit $i-1$ set. Expanding the
recurrence with the identity
$\lfloor \lfloor x/a \rfloor / b \rfloor = \lfloor x/(ab) \rfloor$ gives the
closed form

$$
c_i = \sum_{s \ge 0} \left\lfloor \frac{d_{i-s}}{2^{s}} \right\rfloor ,
$$

which says the same thing locally: a bit $i$ can be assembled if and only if
**some** level $i-s$ holds at least $2^{s}$ elements with that bit set. Bit $i$
is present in the answer exactly when $c_i \ge 1$.

| Level $i$ | $d_i$ (elements with bit $i$) | Carry-in $\lfloor c_{i-1}/2 \rfloor$ | $c_i$ | Bit $i$ emitted? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 2 (values 1 and 3) | 0 | 2 | yes |
| 1 | 2 (values 2 and 3) | 1 | 3 | yes |
| 2 | 0 | 1 | 1 | yes |
| 3 | 0 | 0 | 0 | no |
| 4 | 0 | 0 | 0 | no |

The closed form can be read off the same data, and it agrees bit for bit.

| Bit $i$ | Candidate $s = 0$ | Candidate $s = 1$ | Candidate $s = 2$ | Any level adequate? |
|:---:|:---|:---|:---|:---:|
| 0 | $d_0 = 2 \ge 1$ | — | — | yes |
| 1 | $d_1 = 2 \ge 1$ | $d_0 = 2 \ge 2$ | — | yes |
| 2 | $d_2 = 0 < 1$ | $d_1 = 2 \ge 2$ | $d_0 = 2 < 4$ | yes, through $s = 1$ |
| 3 | $d_3 = 0 < 1$ | $d_2 = 0 < 2$ | $d_1 = 2 < 4$ | no |
| 4 | $d_4 = 0 < 1$ | $d_3 = 0 < 2$ | $d_2 = 0 < 4$ | no |

## 5. Correctness: why the recurrence decides every bit

**No bit is invented.** Every bit that appears in some subsequence sum is
accounted for by a unit at that position. Units at position $i$ can only come
from two sources: elements with bit $i$ set, of which there are $d_i$, or carries
out of position $i-1$. A carry out of position $i-1$ consumes two units there and
produces one at position $i$, so the number of units reaching position $i$ is at
most $d_i + \lfloor c_{i-1}/2 \rfloor = c_i$. If $c_i = 0$, then $d_i = 0$ and
$c_{i-1} \le 1$: nothing sits at position $i$, and the only possible source of a
carry into it is a single unpaired unit at position $i-1$, which cannot carry.
Inducting upward, a zero count at position $i$ means no selection of elements can
place a unit there, so bit $i$ is absent from every subsequence sum and therefore
absent from the OR. In the trace this rules out bits 3 and above, and it also
rules out bit 2 for a set such as `nums = [8,1,1]`, where $d_2 = 0$ and
$c_1 = 1$ is a single unpaired unit that cannot reach position 2.

**No achievable bit is missed.** If $c_i \ge 1$ then some fusion schedule
produces a unit at position $i$. Take the minimal schedule the recurrence
describes: either one element with bit $i$ set, which is itself a subsequence
whose sum has bit $i$ equal to 1, or a group of $2^{s}$ disjoint elements with
bit $i-s$ set whose contributions fuse upward. Every fusion consumes units in
whole pairs, so inside such a group the accumulation at position $i$ is an odd
number of units, and an odd count at a position is precisely what makes that bit
of the binary sum equal to 1. The group is a legal subsequence, so bit $i$
appears in the OR. The floor in the recurrence is exactly this odd-unit
bookkeeping: it discards the completed pairs and keeps the survivor.

**The two directions agree.** For each position, "the recurrence reports a
positive count" and "some subsequence sum has that bit set" are equivalent, so
summing the surviving positions with weights $2^{i}$ reproduces the OR exactly.
The traced instance is small enough to certify by complete enumeration: the
sixteen subsequences produce the seven sums
$0,1,2,3,4,5,6$, whose OR is $7 = 111$, and Section 4 predicts precisely bits
0, 1 and 2.

## 6. Traps the instance exposes

| Situation | Naive expectation | What actually happens |
|:---|:---|:---|
| Duplicate large values, `nums = [4,4]` | the answer is the OR of the elements, so 4 | two 4s add to 8, whose bit 3 no element has, so the answer is 12 |
| A value 0 in the array | it contributes its own bits | it has no bits; it only multiplies the number of subsequences that share an existing sum |
| A high element beside several small ones, `nums = [8,1,1]` | the two 1s must create bit 1 and cannot go further, yet bit 2 seems reachable from 8 | the answer is $11 = 1011$: bit 2 is absent because two units at position 0 carry only to position 1 |
| Repeated ones, `nums = [1,1,1,1]` | only bit 0 is present | four units at position 0 fuse to one unit at position 2, so bits 0, 1 and 2 appear and the answer is 7 |
| A single element, `nums = [7]` | there could be sums beyond the element itself | the only subsequences are empty and the element, giving $0 \lor 7 = 7$ |
| Order of `nums` | the order of a subsequence matters | only the multiset of selected values matters for a sum, so the answer is order-independent |
| Value bound | sums might need bits far above 30 | with $n \le 10^{5}$ and values up to $10^{9}$, a sum never exceeds $10^{14} < 2^{47}$, so counting levels a little above 47 is already more than enough |

The authored checks follow exactly these rules. An array of three zeros yields
$0$, because every subsequence sum is 0. The pair `[2,2]` yields 6, since the
reachable sums are $0, 2, 4$. The pair `[1,3]` yields 7. And the pair of maximum
values `[1000000000,1000000000]` yields $2143280640$, which is the OR of the two
elements and their sum, a value whose highest bit comes from the carry rather
than from either element alone.

## 7. Complexity: time and auxiliary space

Let $n$ be the length of `nums` and let $B$ be the number of bit levels counted.
The values satisfy `nums[i]` $\le 10^{9} < 2^{30}$, so a count is needed for
about 30 levels; because the OR is taken over sums that can reach $n \cdot 10^{9}
\le 10^{14} < 2^{47}$, counting up to a few levels beyond 47 is safe, and $B = 64$
is a comfortable fixed bound.

**Time.** Reading the elements once costs $O(n)$, and inspecting the bit pattern
of each value costs $O(\log \text{max value}) \subseteq O(30)$ per element. The
carry scan then makes one pass over the $B$ levels, each step performing a halving
and a comparison, so it costs $O(B)$. The total is
$O(n \cdot 30 + B)$, which is $O(n)$ for the stated value bound; the level count
is a constant and does not grow with the input size.

**Auxiliary space.** The only working storage is the count vector $c$ of length
$B$, so the auxiliary space is $O(B) = O(1)$ with respect to $n$ — 64 counters,
independent of whether the array holds one element or $10^{5}$. No subset, sum,
or intermediate subsequence is ever materialised.

| Strategy | Time | Auxiliary space | Trade-off |
|:---|:---:|:---:|:---|
| Count element bits, then carry levels upward | $O(n \log V + B)$ | $O(B)$ | the intended method; one pass and a 64-slot vector |
| Enumerate all $2^{n}$ subsequences and OR their sums | $O(2^{n})$ | $O(1)$ | exact by definition and usable only for tiny $n$; hopeless at $n = 10^{5}$ |
| Sort the values and simulate the largest achievable sum greedily | $O(n \log n)$ | $O(n)$ | tempting but wrong: bits come from parities of carries, not from the maximum sum |
| Dynamic programming over reachable sums | $O(n \cdot \sum \text{nums}[i])$ | $O(\sum \text{nums}[i])$ | correct in principle, but the sum can reach $10^{14}$, far beyond any feasible table |
| Track only the total sum and its highest bit | $O(n)$ | $O(1)$ | fails immediately on duplicates such as `[4,4]`, where the interesting bit is created by a carry no single value implies |

The bit-counting method wins because the question is asked one bit at a time:
eligibility for each position is a local accounting of supplies and carries, and
the answer is assembled from those independent verdicts.

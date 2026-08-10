## General

**Translate two distinct halves into a frequency limit.** Each output part must contain distinct elements. Therefore one particular value can appear at most once in `nums1` and at most once in `nums2`. Across both parts, any value may appear at most twice.

This gives an immediate necessary condition:

$$
\max_v \operatorname{count}(v)\le2.
$$

If some value appears three or more times, placing all occurrences into only two parts forces at least one part to receive two copies, violating distinctness.

**Why the same condition is sufficient.** Suppose every value appears once or twice. For each value appearing twice, put one copy in each part. For each value appearing once, assign it to whichever part currently needs an element.

It remains to justify that the two parts can reach equal size $N/2$. Let $d$ be the number of duplicated values and $u$ the number of singleton values. The total length is

$$
N=2d+u.
$$

Because $N$ is even, $u$ is even. After distributing duplicate copies, each part has $d$ elements. Split the $u$ singleton values evenly, $u/2$ to each part. Both then have

$$
d+\frac{u}{2}=\frac{N}{2}
$$

elements, and no part contains a duplicate. Thus the maximum-frequency condition is also sufficient.

**The exact one-line implementation.** `Counter(nums)` computes all frequencies. `max(...values())` finds the largest, and the method returns whether it is less than 3:

`max(Counter(nums).values()) < 3`.

Since the input length is at least one—and in fact positive even length—the counter is nonempty, so `max` is safe.

**A trace.** For `[1,1,2,2,3,4]`, maximum frequency is two. Put one 1 and one 2 in each part, then distribute singleton 3 to the first and 4 to the second. Valid parts are `[1,2,3]` and `[1,2,4]`.

For `[1,1,1,1]`, maximum frequency is four. Four copies cannot be placed into two distinct-element parts, so false is returned.

**Why the algorithm need not construct the split.** The contract asks only whether a split exists. The frequency proof establishes existence whenever the predicate is true. Building concrete arrays would use extra memory and introduce assignment bookkeeping without changing the Boolean answer.

**A pigeonhole proof for impossibility.** If a value has at least three copies, those copies are three objects placed into two boxes. By the pigeonhole principle, one box receives at least two. Since each box represents one output array, that array would not be distinct. No arrangement of other values can fix this.

**No hidden capacity conflict.** It may seem that singleton assignments could overfill one side. They are freely assignable and occur in an even count, so choosing exactly half for each side always balances the sizes. Duplicate values already contribute equally to both.

## Complexity detail

Let $N$ be input length and $U$ the number of distinct values. Building the counter takes $O(N)$ expected time, and finding its maximum takes $O(U)$. Total expected time is $O(N)$.

The counter stores $O(U)$ entries. Since values are constrained to 1 through 100, $U\le100$ and the space is bounded independently of $N$; under the fixed value domain, auxiliary space is $O(1)$. Without that bound, the honest parameterized space would be $O(U)$.

The input list is not modified. The returned Boolean uses constant result space.

## Alternatives and edge cases

- **Construct both parts greedily:** It can work but requires balancing logic that the frequency proof makes unnecessary.
- **Sort and detect triples:** Three equal consecutive values after sorting imply impossibility. That costs $O(N\log N)$ time and may mutate or copy input.
- **Fixed 101-entry frequency array:** It exploits the value bound and has deterministic constant space, equivalent to the counter approach.
- **Every value distinct:** Maximum frequency is one; because length is even, divide the values arbitrarily into equal halves.
- **Every value appears twice:** Put one occurrence of each value in each part; sizes automatically match.
- **Exactly one value appears three times:** The answer is already false regardless of all other values.
- **Length two:** Any two values are splittable into one-element parts, even if equal, because each individual part is distinct.
- **Even-length guarantee:** It is essential for equal-sized halves and for singleton count parity in the sufficiency proof.
- **Bounded values:** This is why the manifest can call the counter storage constant space.
- **Input preservation:** Counting reads elements without reordering or changing them.
- **Why there is no separate half-capacity test:** Once duplicate values contribute one element to each half, every remaining value is a unique singleton and may go to either side. Even singleton count guarantees an exact equal split, so frequency at most two already contains the size argument.
- **Counter maximum versus checking all counts:** `max < 3` is logically equivalent to `all(count <= 2)`. The maximum form is concise because the counter cannot be empty under the input guarantee.
- **Copies remain distinguishable by position:** Two equal occurrences may be placed in different arrays even though their values match. The requirement is distinctness within each part, not across the union.

## General

**Different values never interact.** Each operation removes either two equal elements or three equal elements. Copies of one value cannot help remove copies of another. Therefore the array can be reduced independently by frequency, and the minimum total number of operations is the sum of the minimum operations for each distinct value.

The source begins with `Counter(nums)`. For every frequency `c`, it solves the small arithmetic problem: represent `c` as a sum of twos and threes while using as few summands as possible.

**Why frequency one is impossible.** Neither allowed operation removes a single item. If any value occurs exactly once, no operation can delete that copy, regardless of what happens to other values. The function immediately returns `-1`. Conversely, every frequency at least two can be formed from twos and threes, so one is the only impossible positive frequency.

**A lower bound on the number of operations.** One operation removes at most three copies. Removing `c` copies therefore needs at least

$$
\left\lceil\frac c3\right\rceil
$$

operations. If that lower bound is always achievable for `c\ge2`, it is optimal.

Consider `c` modulo three.

If `c = 3q`, use `q` triples. This takes exactly $c/3=\lceil c/3\rceil$ operations.

If `c = 3q + 2`, use `q` triples and one pair. That takes `q + 1 = ceil(c/3)` operations.

If `c = 3q + 1` and `c\ge2`, the smallest such frequency is four, so $q\ge1$. Using only as many triples as possible would leave one copy, which is invalid. Replace one triple plus that leftover one, a total of four copies, by two pairs. The construction uses `q - 1` triples and two pairs, totaling `q + 1 = ceil(c/3)` operations.

Thus every frequency except one achieves the lower bound.

**How the source computes the ceiling.** For a positive integer `c`,

`(c + 2) // 3`

equals $\lceil c/3\rceil$. Integer division `//` rounds downward, and adding two before division performs ceiling division by three. The code adds this value to `ans` for every frequency after ruling out `c == 1`.

**Why local minima add to a global minimum.** Operations on one value neither consume nor create copies of another value. Any full solution must spend at least the local lower bound for each frequency, so it must use at least their sum. The constructions above achieve each local bound independently; concatenating those operations empties the whole array using exactly that sum. Hence the sum is globally minimal.

For frequency four, the formula gives `(4 + 2) // 3 = 2`, corresponding to two pairs. For frequency seven, it gives three operations: one triple and two pairs. For frequency eight, it also gives three: two triples and one pair.

**A complete frequency-table trace.** Consider `nums = [2,3,3,2,2,4,2,3,4]`. Its frequencies are four copies of `2`, three copies of `3`, and two copies of `4`. The four twos need two pair operations. The three threes need one triple operation. The two fours need one pair operation. Adding these independent minima gives `2 + 1 + 1 = 4` operations. The physical indices shown in the statement may shift after deletions, but that never affects the calculation: an operation asks only for equal values, not adjacent positions.

Now contrast a frequency table containing counts `3, 2, 1`. The first two groups could be removed in one triple and one pair, yet the singleton group can never be touched. Returning `-1` immediately is therefore stronger than merely adding costs for the removable groups; one impossible value makes the entire array impossible.

**Why no mixed-value trick can improve the ceiling bound.** The two operation types demand that every element chosen in one operation have the same value. As a result, an operation can be assigned to exactly one counter bucket. If a full execution used fewer operations than the sum of the bucket ceilings, at least one bucket would receive fewer than its own $\lceil c/3\rceil$ operations. Those operations could remove at most three items each and could not empty that bucket. This contradiction makes the additive lower bound formal.

**Why “always take a triple” needs qualification.** Triples are most efficient, but blindly taking triples until fewer than three remain fails for frequencies congruent to one modulo three. For four, taking one triple leaves one impossible copy. The ceiling formula is correct because its proof includes the required replacement of one triple by two pairs.

## Complexity detail

Let $n$ be the array length and $u$ its number of distinct values. Building the counter takes expected $O(n)$ time. Iterating through its $u$ frequencies takes $O(u)$, which is at most $O(n)$. Total expected time is $O(n)$.

The counter stores $u$ keys and counts, so auxiliary space is $O(u)$ and becomes $O(n)$ in the worst case. The manifest's tighter `O(u)` notation accurately describes the exact source. Hash-table operations are expected or amortized constant time in the usual model.

## Alternatives and edge cases

- **Dynamic programming per frequency:** A coin-change-style table using removals of two and three works, but the modulo proof gives a constant-time formula for each count.
- **Greedy triples without remainder handling:** It fails whenever `c % 3 == 1` because it leaves one copy. Convert one would-be triple plus that singleton into two pairs.
- **Any singleton frequency:** Return `-1` immediately; operations on other values cannot rescue it.
- **Frequency two:** One pair is both feasible and optimal.
- **Frequency three:** One triple is both feasible and optimal.
- **Frequency four:** It must be two pairs, illustrating why simple triple-first removal is unsafe.
- **Many distinct values:** Their operation counts add independently; order of executing operations is irrelevant.
- **Input mutation:** The counter-based method does not delete from or reorder `nums`.

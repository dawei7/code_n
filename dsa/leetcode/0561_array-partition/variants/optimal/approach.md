## General

Each pair contributes only its smaller element. To maximize the sum, large values should not be wasted as the larger partner of much smaller values when two nearby large values could form a pair whose minimum is also large.

The optimal strategy is:

1. sort all values in ascending order;
2. pair adjacent values;
3. sum the first value of each pair.

After sorting:

`x[0] <= x[1] <= x[2] <= x[3] <= ...`,

the pairs are `(x[0], x[1])`, `(x[2], x[3])`, and so forth. Their minima are exactly the even-indexed elements, which `nums[::2]` selects.

**Why the smallest value should pair with the next-smallest.** The globally smallest remaining value must be the minimum of whichever pair contains it; no partner can make its contribution larger.

If it is paired with some later large value, the next-smallest value must pair elsewhere and may consume another valuable large partner. Pairing the two smallest together sacrifices only the second-smallest as a non-contributing maximum and leaves every larger value available for later pairs.

This argument can be repeated after removing the first pair, proving adjacent pairing inductively.

**Exchange argument.** Consider sorted values `a <= b <= c <= d` where a pairing crosses or separates nearby ranks, such as `(a,c)` and `(b,d)`. Its minimum sum is `a+b`. Pairing adjacent values `(a,b)` and `(c,d)` gives `a+c`, which is at least `a+b` because `c >= b`.

Likewise, pairing `(a,d)` and `(b,c)` gives `a+b` and cannot beat adjacency. Replacing nonadjacent structure with adjacent pairs never decreases the score.

For `[1,4,3,2]`, sorting yields `[1,2,3,4]`. Adjacent pairs contribute one and three, totaling four.

For `[6,2,6,5,1,2]`, sorting yields `[1,2,2,5,6,6]`. Even indices contribute one, two, and six, totaling nine.

**Why only even indices are added.** In each adjacent sorted pair `(nums[2q], nums[2q+1])`, the first is no greater than the second and is therefore the minimum. Every input element belongs to exactly one such pair.

The code sorts `nums` in place. This changes the caller-provided list order, which does not affect the returned numeric result but is an observable implementation detail.

Negative values do not change the proof. For sorted pair `(-5,-2)`, the minimum is minus five; grouping adjacent negatives still prevents a relatively large value from being wasted beside an even smaller one.

Duplicates are also natural. Equal adjacent values make either copy the minimum, and slicing chooses one representative occurrence per pair.

**Why the result is globally optimal.** Starting with the smallest remaining element, adjacent pairing is never worse than pairing it with a farther element. Removing that pair leaves the same problem on the remaining sorted suffix. Induction covers all `n` pairs, so no other complete pairing has a larger sum of minima.

The implementation does not need to construct tuple objects for pairs because the sorted positions already encode them.

Another useful viewpoint is to count which values become “discarded” as the larger member of a pair. Exactly half the elements do not contribute. The optimal arrangement discards indices one, three, five, and so on after sorting, because each discarded value is the smallest possible shield for the contributing value immediately before it. Discarding a much larger value next to a small minimum leaves a medium value that must later suppress some other potentially larger minimum.

For sorted `[-4, -3, 5, 100]`, adjacent pairing contributes `-4 + 5 = 1`. Pairing `-4` with `100` and `-3` with `5` contributes `-4 + -3 = -7`. The example makes clear that the argument is about order, not positivity.

## Complexity detail

Let $N$ be the number of integers, equal to twice the problem's pair count. Python sorting takes $O(N\log N)$ time. Slicing `nums[::2]` and summing take $O(N)$ additional time, so sorting dominates.

The slice creates a new list containing $N/2$ integers, using $O(N)$ extra space. Python's sort also has implementation-dependent temporary storage; the manifest's $O(n)$ space safely covers the exact method.

If the sum were written as a generator over even indices, the explicit slice allocation could be avoided, though sort storage would remain implementation-dependent.

The numeric result may be negative when sufficiently many input values are negative. Maximization still means choosing the least harmful pairing; the method does not assume the optimum is nonnegative.

## Alternatives and edge cases

- **Counting sort:** The bounded value range allows linear time in input size plus range, at the cost of a frequency array.
- **Enumerate pairings:** The number of pairings grows combinatorially and is unnecessary.
- **Pair smallest with largest:** It wastes large values as non-contributing partners and is generally suboptimal.
- **One pair:** Sorting and choosing index zero returns the smaller of the two values.
- **All values equal:** Every pairing has the same result; adjacency remains valid.
- **Negative values:** Ascending adjacency still maximizes the minima sum.
- **Duplicate values:** They remain separate occurrences and pair normally.
- **In-place sort:** The original order is not preserved.
- **Even-length guarantee:** Every sorted element belongs to a complete adjacent pair.
- **Slice semantics:** `[::2]` selects indices zero, two, four, and so on.
- **Large pair count:** Sorting, not pairing construction, is the dominant cost.

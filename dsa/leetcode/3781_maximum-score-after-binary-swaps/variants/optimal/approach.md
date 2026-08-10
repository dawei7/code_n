## General

**Describe reachable one positions as deadlines**

Legal swaps change `"01"` to `"10"`, so a one may move left across zeros but never right across a zero. Ones also cannot pass one another.

List the original one positions in increasing order as

$$
p_1<p_2<\cdots<p_m.
$$

If their final positions are $q_1<q_2<\cdots<q_m$, reachability requires

$$
q_k\le p_k
$$

for every $k$. The $k$th one must be assigned a distinct score position no later than its original position. Conversely, any increasing positions satisfying these inequalities can be reached by moving the ones from left to right into those earlier-or-equal places.

Thus each original one position is a deadline: when scan index `p_k` is reached, one unused position from prefix `0..p_k` must be selected.

**Store all currently available score values**

The source scans `nums` and `s` together from left to right. At every index, it pushes `-x` into `pq`.

Python provides a min-heap. Negating scores makes the most valuable available score the smallest stored negative number. Popping it and subtracting it from `ans` adds the original positive value.

The heap contains score positions already encountered but not yet assigned to a one. A position may be selected at most once because popping removes it.

**Satisfy a deadline whenever an original one appears**

When current character `c` is `"1"`, another original one deadline has arrived. The source immediately pops the largest score among all unassigned positions in the current prefix.

After processing any prefix ending at index `i`:

- the number of selected positions equals the number of original ones in `s[0..i]`;
- every selected position lies inside that prefix;
- `pq` contains all other prefix positions.

The heap can never be empty at a one: the current position was pushed before the conditional pop, and previous pops cannot outnumber previous ones.

**Why taking the current maximum is optimal**

At deadline `p_k`, some position from the available prefix must be assigned to the $k$th one. Suppose an optimal assignment uses available score `y` now while a larger available score `x` is not selected.

If `x` is never selected later, replace `y` with `x` and improve the score.

If `x` is selected for a later one, swap their assignments. Position `x` was already available by deadline `p_k`, so it is legal for the current one. Position `y` was also available now and therefore remains no later than the later deadline. Feasibility is preserved, and total score is unchanged.

Repeated exchanges make an optimal assignment agree with every greedy heap pop. Therefore selecting the largest available score at each one deadline is globally optimal.

**Trace the first example**

For `nums=[2,1,5,2,3]` and `s="01010"`:

- index zero pushes 2; there is no deadline;
- index one pushes 1 and encounters a one, so it selects 2;
- index two pushes 5;
- index three pushes 2 and encounters the second one, so it selects 5;
- index four pushes 3 but has no new one.

The selected positions have values 2 and 5, for score seven. They correspond to final one positions zero and two, reachable by moving each original one left once.

**Why unused heap entries are harmless**

The total number of ones never changes, so exactly $m$ positions must contribute. The source pops exactly once for each original `"1"` and ignores every leftover heap value at the end.

Those leftover positions receive zeros in the final string. Even a large late score cannot be selected if too few one deadlines remain or if selecting it would require an earlier one to move right.

For an all-zero string, no pop occurs and the answer remains zero. For an all-one string, each pushed value is immediately popped, so every original position contributes.

## Complexity detail

Each of the $N$ positions is pushed once. Each original one causes one pop, for at most $N$ pops. Heap operations cost $O(\log N)$, yielding $O(N\log N)$ total time.

The heap can contain $O(N)$ unassigned values, so auxiliary space is $O(N)$. The method stores only the accumulated numeric score beyond that heap and does not mutate either input.

## Alternatives and edge cases

- **Simulate adjacent swaps:** Exploring or performing swaps directly can be quadratic and hides the assignment structure.
- **Choose the globally largest values:** A large value to the right of an early one's deadline may be unreachable for that one.
- **Min-cost matching:** The nested prefix constraints form a special deadline problem that the heap solves greedily.
- **Process from right to left:** A dual formulation is possible, but the source treats original ones as left-to-right deadlines.
- **Push after handling a one:** That would incorrectly exclude the one's current position from its legal choices; the source pushes first.
- **All zeros:** No score position is selected and the answer is zero.
- **All ones:** No one can change its relative occupancy; all values are selected.
- **One at index zero:** Its only available position is zero, so that value is popped immediately.
- **Late one:** It may choose any still-unused position in its entire prefix.
- **Duplicate score values:** Heap occurrences remain separate and can be selected for different ones.
- **Positive scores:** The algorithm still respects reachability; positivity means using all fixed ones is naturally required.
- **Ones never cross:** Sorted deadline-to-position matching preserves their order.
- **Input preservation:** The heap stores negated values without changing `nums` or `s`.

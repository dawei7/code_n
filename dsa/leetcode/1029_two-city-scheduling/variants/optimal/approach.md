## General

**Compare the extra cost of choosing city A**

Every person must go to exactly one city, and exactly half must go to each. Looking only at the cheaper ticket for each person can violate that quota. The useful quantity is not either ticket price alone, but the relative change caused by assigning that person to city A instead of city B.

For costs `[a, b]`, define

$$
\Delta = a-b.
$$

If `\Delta` is negative, city A is cheaper by `-\Delta`. If it is positive, city A is more expensive by `\Delta`. A smaller difference means that choosing A is more favorable relative to choosing B.

The code sorts `costs` by `x[0] - x[1]` in ascending order. It then sends the first half to A and the second half to B.

**Derive the rule from a baseline**

Imagine initially sending everyone to city B. The baseline total is

$$
\sum_i b_i.
$$

Moving person `i` from B to A changes that total by `a_i - b_i = \Delta_i`. The quota requires moving exactly `n` of the `2n` people to A. Therefore, the final total is

$$
\sum_i b_i + \sum_{i\ \text{chosen for A}} \Delta_i.
$$

The baseline is fixed regardless of the assignment. Minimizing total cost is therefore exactly the same as choosing `n` differences with the smallest possible sum. Those are the first `n` entries after sorting differences ascending.

This derivation explains why sorting by `a` alone, `b` alone, or the cheaper absolute ticket is not sufficient. The quota decision depends on the cost of switching between cities for the same person.

**An exchange proof**

Suppose an assignment sends person `p` to A and person `q` to B, but `\Delta_p > \Delta_q`. Swap their destinations. The number assigned to each city remains unchanged.

The original contribution is `a_p + b_q`. The swapped contribution is `b_p + a_q`. Subtracting gives

$$
(a_p+b_q)-(b_p+a_q)=\Delta_p-\Delta_q>0.
$$

So the swap makes the schedule cheaper. Consequently, an optimal assignment cannot place a larger difference in A while a smaller difference remains in B. All A-assigned differences must be no larger than all B-assigned differences, which is exactly the sorted first-half rule.

Tied differences can appear on either side without changing the total. Python's stable tie order is irrelevant to correctness.

**How the exact code selects the halves**

After in-place sorting, `n = len(costs) >> 1` computes half the number of people. Right shift by one divides a nonnegative integer by two. The source guarantees an even length, so no rounding issue exists.

The generator iterates `i` from zero through `n - 1`. For each `i`, it adds:

- `costs[i][0]`, the city A price for a person in the lower-difference half.
- `costs[i + n][1]`, the city B price for the corresponding position in the upper-difference half.

The pairing between those positions has no business meaning; it is only a compact way to sum both halves in one loop. Every first-half person contributes an A cost once, and every second-half person contributes a B cost once.

**Trace the first example**

For `[[10,20],[30,200],[400,50],[30,20]]`, the differences are `-10`, `-170`, `350`, and `10`.

Sorted by difference, the people are:

- `[30,200]` with difference `-170`.
- `[10,20]` with difference `-10`.
- `[30,20]` with difference `10`.
- `[400,50]` with difference `350`.

There are four people, so `n = 2`. The first two go to A for `30 + 10`. The last two go to B for `20 + 50`. The total is `110`.

It would be misleading to say the first person goes to A merely because ten is cheap. The decisive fact is that the second person's A ticket saves 170 relative to B, making that assignment even more urgent.

**Why negative and positive differences need no special cases**

Sorting naturally handles every situation. If many A tickets are cheaper, their negative differences appear first. If fewer than `n` are negative, some positive differences must still go to A to satisfy the quota; sorting chooses the least painful ones. If more than `n` are negative, only the `n` greatest relative savings can use the limited A slots.

The same reasoning applies if every B ticket is cheaper. Exactly half must still go to A, and the algorithm chooses the people whose penalty for A is smallest.

**Why the result is globally optimal**

The baseline derivation turns the constrained assignment into selecting exactly `n` numeric adjustments. Selecting the `n` smallest adjustments minimizes their sum. Independently, the exchange argument proves that any assignment violating sorted order can be improved while preserving quotas.

The returned schedule has the correct cardinalities because the two halves each contain exactly `n` people. It assigns every person once and attains the smallest possible total adjustment, so the returned cost is globally minimal.

## Complexity detail

Let `P = len(costs)` be the total number of people. Computing comparison keys and sorting takes `O(P \log P)` time. The final generator visits `P / 2` paired positions and performs `O(P)` work. Sorting dominates, so total time is `O(P \log P)`, which is the manifest's `O(N \log N)` bound with `N` denoting input size.

Python's in-place list sort may use `O(P)` temporary memory for Timsort, so the manifest records `O(N)` space. The summation generator itself is lazy and needs only constant iteration state. Sorting changes the order of the caller-provided `costs` list but does not create a second full list in the solution code.

## Alternatives and edge cases

- **Start with everyone in A:** Use B-minus-A differences and switch exactly half to B. This is algebraically symmetric and produces the same assignments.
- **Dynamic programming by person and A quota:** A state can track minimum cost after assigning a certain number to A. It is correct but uses `O(P^2)` time in the straightforward form, while the difference structure gives a greedy solution.
- **Heap selection:** Keep the `n` smallest differences in a heap. This can avoid fully ordering the data but is more complex and has similar `O(P \log n)` time.
- **Quickselect:** Partition around the `n`-th difference for expected `O(P)` time, then sum the two groups. Worst-case guarantees and tie handling are more involved than sorting for at most 100 people.
- **Choose each person's cheaper city:** This can send the wrong number of people to each city and does not satisfy the central constraint.
- **Sort by A cost only:** A low A cost may still be a poor A assignment if that person's B cost is much lower. Relative difference is the correct opportunity cost.
- **Equal differences:** Swapping tied people between cities leaves total cost unchanged, so any tie order is valid.
- **All differences negative:** A is cheaper for everyone, but only half may go there. The algorithm gives A to the half with the largest relative savings.
- **All differences positive:** B is cheaper for everyone, yet the quota forces half to A. The smallest penalties are selected.
- **Exactly two people:** The smaller difference goes to A and the other person goes to B, which directly minimizes the two possible valid schedules.
- **Even-length guarantee:** `len(costs) >> 1` is exact only because the number of people is guaranteed even.
- **Input mutation:** `costs.sort(...)` changes row order. If the original order is needed afterward, sort a copy instead at the cost of additional explicit space.
- **Large individual prices:** Only subtraction and addition are used, and the stated price bounds keep totals comfortably within ordinary integer ranges.

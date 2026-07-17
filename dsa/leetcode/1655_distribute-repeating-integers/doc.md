# Distribute Repeating Integers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1655 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-repeating-integers/) |

## Problem Description
### Goal
An inventory `nums` contains repeated integer values, and each entry can be given away at most once. Customer `i` requests exactly `quantity[i]` integers. Every integer received by one customer must have the same value, although different customers may receive the same value when enough copies exist.

Determine whether every customer can be satisfied simultaneously. Inventory entries may remain unused, but a customer may not combine different integer values or receive a quantity other than the exact request.

### Function Contract
**Inputs**

- `nums`: an array of length $n$, where $1 \le n \le 10^5$, every value is between 1 and 1000, and at most 50 distinct values occur.
- `quantity`: an array of $m$ positive customer demands, where $1 \le m \le 10$ and each demand is at most $10^5$.

Let $f=\min(m,\lvert\operatorname{distinct}(\texttt{nums})\rvert)$ after retaining the $f$ largest value frequencies.

**Return value**

Return `true` if all $m$ exact demands can be assigned to value frequencies without exceeding any frequency; otherwise return `false`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], quantity = [2]`
- Output: `false`

No value occurs twice, and one customer cannot combine two different values.

**Example 2**

- Input: `nums = [1, 2, 3, 3], quantity = [2]`
- Output: `true`

Both copies of 3 satisfy the request; values 1 and 2 may remain unused.

**Example 3**

- Input: `nums = [1, 1, 2, 2], quantity = [2, 2]`
- Output: `true`

The two customers can receive the two copies of 1 and the two copies of 2, respectively.

### Required Complexity
- **Time:** $O(n+f3^m)$
- **Space:** $O(2^m+f)$

<details>
<summary>Approach</summary>

#### General

**Compress values into capacities.** Only the number of copies of each distinct value matters. Count `nums` and sort the frequencies. At most $m$ different values can be used by a solution with $m$ customers; if a solution uses a smaller frequency while a discarded larger frequency is unused, moving that entire customer group to the larger frequency remains valid. Therefore only the $m$ largest frequencies need to be retained.

**Precompute every customer-subset demand.** Represent served customers by an $m$-bit mask. For each mask, compute the sum of its requested quantities by removing its lowest set bit and extending a previously computed sum. A subset can share one integer value precisely when its total demand does not exceed that value's frequency.

**Assign one frequency at a time.** Start with only mask 0 reachable. For a frequency capacity and each previously reachable mask, enumerate every submask of the unserved customers. When that submask's precomputed demand fits the capacity, mark the union reachable for the next frequency. Keep the old mask as well, because an inventory value may remain unused.

Each transition assigns a whole customer to exactly one value through its submask membership, and the demand check prevents overusing that value. Conversely, any valid distribution partitions the customers into subsets assigned to distinct frequencies; processing those frequencies reproduces that sequence of reachable masks. Thus the full mask is reachable exactly when all customers can be satisfied.

#### Complexity detail

Counting the inventory takes $O(n)$ time. Across all served masks, enumerating submasks of their complements has the standard $O(3^m)$ total bound per retained frequency, so the dynamic program takes $O(f3^m)$ time. Subset sums and reachable masks use $O(2^m)$ space, while retained capacities use $O(f)$ space.

#### Alternatives and edge cases

- **Customer-by-customer backtracking:** Try each remaining frequency for the next largest demand and restore it afterward. Sorting and symmetry pruning can work well for $m\le10$, but the worst case explores exponentially many repeated assignments without the subset-state reuse.
- **Enumerate every customer-to-value mapping:** Trying all $f^m$ assignments and checking capacities is correct but repeats equivalent partial states and scales much worse than subset DP.
- **Greedy largest-to-largest:** Assigning each largest request to the largest current capacity can block two smaller requests that would have shared that capacity, so the local choice is not generally sound.
- Several customers may share one value if their total demand fits its frequency.
- One customer may never split a request across different values.
- Unused inventory is allowed, so capacities need not be exhausted.
- If the sum of all demands exceeds $n$, distribution is immediately impossible, although the DP also rejects it.
- A single request succeeds exactly when some frequency is at least that request.
- Equal frequencies create interchangeable choices; mask reachability avoids depending on which equal value is selected.

</details>

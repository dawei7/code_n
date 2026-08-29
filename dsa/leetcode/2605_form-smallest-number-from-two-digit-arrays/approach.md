## General

**A shared digit gives the best possible number**

The result must contain at least one digit from each array. If digit $d$ occurs in both, the one-digit number $d$ satisfies both requirements simultaneously.

Every allowed digit is from one through nine, so any one-digit candidate is smaller than every two-digit candidate. Therefore, when common digits exist, the answer is the smallest common digit.

**Without a shared digit, two digits are necessary**

If the arrays are disjoint, no single digit can represent both. A valid number needs at least one digit $a$ from `nums1` and one digit $b$ from `nums2`.

The smallest possible valid number then has exactly two digits. Adding more digits would create a number of at least three decimal places and make it larger because leading zero is impossible under the digit constraints.

For a chosen pair $(a,b)$, either order is allowed:

$$
10a+b
\quad\text{or}\quad
10b+a.
$$

The smaller order places the smaller digit in the tens position.

**Enumerate every cross-array pair**

The exact solution initializes `ans = 100`. Every valid result is at most 99, so this is a safe sentinel larger than all candidates.

For every `a in nums1` and `b in nums2`:

- when `a == b`, update with one-digit candidate `a`;
- otherwise update with both two-digit orders.

`min` retains the smallest candidate seen across all pairs.

This direct enumeration combines common-digit detection and disjoint-digit construction in one compact loop.

There is no risk that the sentinel survives. Both input arrays are nonempty, so the nested loops execute at least once. That first pair always produces either its shared one-digit value or two valid two-digit values, each strictly below 100. From then on, `ans` is always a real feasible result, and later iterations can only improve it. This detail explains both why no special initialization branch is needed and why returning `ans` after the loops is safe.

**Why checking both orders is sufficient**

For a fixed pair of distinct digits, any shortest valid decimal number using exactly those digits has one in the tens place and one in the units place. There are only two permutations, both explicitly tested.

For a common digit, writing it twice as `dd` would satisfy the requirement but is larger than the one-digit `d`, so only `d` needs consideration.

Notice that the method enumerates digit choices, not arbitrary decimal strings. Once one digit has been selected from each array, a shortest candidate is completely determined except for their order. Repeating either digit or appending a third digit cannot help: it preserves validity but increases the number of decimal places. This is the key reason the finite candidate set is exhaustive.

**Global correctness**

Take an optimal result.

If it has one digit, that digit must occur in both arrays. The nested loops encounter the equal pair and add the same candidate.

If no common digit exists, an optimal result cannot have one digit. A smallest result uses exactly two digits, one from each array; call them $a$ and $b$. The nested loops encounter this pair and evaluate both possible orders, including the optimal one.

Thus the candidate set contains every possible optimum, and `min` returns the smallest.

**Trace the examples**

For `nums1 = [4,1,3]` and `nums2 = [5,7]`, there is no common digit. Pair $(1,5)$ produces $15$ and $51$. All other pairs have a tens digit at least one and a no-smaller units arrangement; the minimum retained result is $15$.

For `nums1 = [3,5,2,6]` and `nums2 = [3,1,7]`, pair $(3,3)$ produces one-digit candidate $3$. Any two-digit number is at least $10$, so three is globally optimal.

**Simpler direct formula**

One could compute the intersection of digit sets. If nonempty, return its minimum. Otherwise let $a=\min(nums1)$ and $b=\min(nums2)$, then return

$$
10\min(a,b)+\max(a,b).
$$

The exact code instead enumerates at most $9\cdot9=81$ pairs, which is still constant under the constraints and avoids separate set logic.

**Why uniqueness is not essential to correctness**

Each array's digits are guaranteed unique, but duplicates would merely cause repeated evaluation of identical candidates. The minimum result would remain correct.

The inputs are read only and retain their order.

## Complexity detail

Let $n_1$ and $n_2$ be the array lengths. The nested loops take $O(n_1n_2)$ time and $O(1)$ auxiliary space.

Since each length is at most nine, the problem treats this as $O(1)$ time, matching the manifest. No set, sorted copy, or output collection is allocated.

## Alternatives and edge cases

- **Set intersection:** Find the smallest common digit directly, then use both array minima if none exists.
- **Sort both arrays:** Sorting is unnecessary for at most 81 direct candidates and would add mutation or copies.
- **Multiple common digits:** The nested minimum keeps the smallest one.
- **No common digit:** Exactly two digits are necessary, and both orders are tested.
- **Smaller digit from second array:** Testing `10*b+a` ensures it can occupy the tens place.
- **One-element arrays:** The sole pair yields either their shared digit or the smaller of the two orders.
- **No zero digits:** Every constructed two-digit candidate truly has two decimal digits.
- **Sentinel 100:** All valid candidates lie from one through 99, so it is safely replaced.
- **Input preservation:** Neither array is modified.

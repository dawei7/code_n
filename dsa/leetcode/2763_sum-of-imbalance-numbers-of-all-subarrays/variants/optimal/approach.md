## General

Fix a left endpoint and grow the subarray one position at a time. A set records the distinct values already present, while `imbalance` stores the number of gaps between consecutive distinct values in sorted order. Start the set with `nums[left]`; a singleton has imbalance zero.

**How one new distinct value changes the gaps**

Let the next value be `x`. A duplicate cannot change the sorted distinct values, so it leaves the imbalance unchanged. Otherwise, only the relationships next to `x` can change:

- If neither `x - 1` nor `x + 1` is present, inserting `x` creates one additional gap. This is true whether `x` lies outside the current range or splits an existing large gap into two.
- If both neighbors are present, they previously formed the counted gap from `x - 1` to `x + 1`. Inserting `x` closes that gap, so the imbalance decreases by one.
- If exactly one neighbor is present, the number of counted gaps stays the same.

After applying this constant-time update, insert `x` and add the current imbalance to the answer. Repeating the process for every right endpoint counts every subarray beginning at the fixed left endpoint. Repeating for every left endpoint counts every non-empty subarray exactly once. The update examines every possible way a new distinct integer can relate to its immediate numeric neighbors, so the maintained value always equals the imbalance of the current subarray.

## Complexity detail

There are $n$ choices of left endpoint and at most $n$ right-endpoint extensions for each one. Hash-set membership and insertion take expected $O(1)$ time, giving $O(n^2)$ expected time overall. The set for one left endpoint can contain at most $n$ distinct values, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Sort every subarray:** Building and sorting each subarray gives a direct implementation of the definition, but repeatedly sorting overlapping data is superquadratic.
- **Contribution counting:** One can derive a linear-time contribution formula for each adjacent-value gap, but its boundary accounting is substantially less direct than the quadratic method permitted by $n \leq 1000$.
- **Duplicate values:** Repeated occurrences do not alter the set of distinct sorted values and therefore do not change the current imbalance.
- **Consecutive values:** Any subarray whose distinct values form one consecutive interval has imbalance zero, regardless of their original order.
- **Singletons:** A length-one subarray has no neighboring sorted pair, so its imbalance is zero.

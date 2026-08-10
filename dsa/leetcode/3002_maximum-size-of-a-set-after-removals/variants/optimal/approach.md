## General

**Only distinct values matter after removal**

Each array keeps exactly $n/2$ elements, but the final container is a set. Keeping duplicate copies of a value contributes only one to its size. The goal is therefore to preserve as many distinct values as the two per-array capacities allow.

The code builds `s1 = set(nums1)` and `s2 = set(nums2)`. Their values fall into three disjoint categories:

- exclusive to `nums1`: `s1 - s2`;
- exclusive to `nums2`: `s2 - s1`;
- common to both: `s1 & s2`.

**Prioritize exclusive values**

An exclusive-to-first value can be contributed only by the $n/2$ elements retained from `nums1`. Keeping one copy adds a unique final-set value that the second array can never supply. The most such values that can survive is:

`a = min(len(s1 - s2), n // 2)`.

The symmetric count for second-only values is:

`b = min(len(s2 - s1), n // 2)`.

There is no benefit in giving an array slot to a duplicate while an unkept exclusive distinct value is available. Thus an optimal construction can always preserve `a` and `b` exclusives first.

**Use common values to fill remaining distinct capacity**

There are `len(s1 & s2)` possible common values. Each needs to be retained in only one array to appear in the union. Since it exists on both sides, its copy can be assigned to whichever retained half has room.

Ignoring the total element count momentarily, the available distinct categories suggest:

`a + b + len(s1 & s2)`.

However, the two remaining arrays contain only $n/2+n/2=n$ elements total. A set formed from $n$ retained elements can never have more than $n$ distinct values. The final expression is therefore:

`min(a + b + len(s1 & s2), n)`.

**Why this upper bound is attainable**

Keep one copy of each of the `a` chosen first-exclusive values in `nums1` and each of the `b` second-exclusive values in `nums2`. This uses at most half the slots on each side.

Then choose as many different common values as the remaining combined slots permit. A common value exists in both arrays, so distribute chosen common values between the two sides according to their free capacities. If an array still has unused retained slots after all useful distinct values are chosen, fill them with arbitrary duplicates; those do not change the set.

This constructs exactly the minimum of the category total and $n$, proving the formula is not only an upper bound.

**Trace the second sample**

For `nums1 = [1,2,3,4,5,6]` and `nums2 = [2,3,2,3,2,3]`:

- `s1 - s2 = {1,4,5,6}`, but the first array can keep only three elements, so `a=3`;
- `s2 - s1` is empty, so `b=0`;
- the common set is `{2,3}`.

The formula gives `min(3+0+2,6)=5`. Keep three exclusive values from the first array and common values two and three through the available slots, yielding five distinct final values.

**Why duplicates still provide padding**

The rules require removing exactly half, so each array must retain exactly half even when it has few distinct values. Duplicate occurrences can fill leftover slots. They do not reduce the already selected distinct union, so capacity is an upper bound on distinct contribution rather than a demand that every retained item be distinct.


Any solution obtains at most `a` useful first-exclusive values, at most `b` useful second-exclusive values, and at most the full common-set size. It also obtains at most $n$ total distinct values because only $n$ elements remain. Hence the returned formula bounds every solution.

The construction above reaches that bound, so it is optimal.

## Complexity detail

Let $N$ be the common array length. Creating both sets takes expected $O(N)$ time. Difference and intersection operations are linear in the set sizes, also expected $O(N)$ total at this scale. The remaining arithmetic is constant, giving expected $O(N)$ time.

The sets and temporary set-operation results can store $O(N)$ distinct values, so auxiliary space is $O(N)$. Neither input array is modified.

## Alternatives and edge cases

- **Greedy over raw occurrences:** Duplicate copies obscure the real objective; classify distinct values first.
- **Take half the distinct count from each set:** This can double-count common values and miss the value of exclusives.
- **Prioritize common values:** Exclusives are less flexible because only one array can provide them; preserving them first is never worse.
- **Disjoint sets:** Every retained distinct value is exclusive, and the answer can reach $n$ when each side has at least $n/2$ distinct values.
- **Identical sets:** There are no exclusives; the answer is limited by the shared distinct count and $n$.
- **All values identical:** The final set size is one despite retaining $n$ elements.
- **More exclusives than capacity:** `min` caps that array’s contribution at $n/2$.
- **Duplicate padding:** Exact retention counts remain achievable even after all useful distinct choices are made.
- **Expected hashing:** Python set operations have expected linear behavior under the standard hash-table model.

## General

**Local inversions are already global inversions**

A local inversion compares adjacent indices `i` and `i + 1`. This pair also satisfies the definition of a global inversion.

Therefore the two counts are equal exactly when there is no additional global inversion whose indices are separated by at least two positions. Such a pair is called a nonlocal inversion.

The task becomes detecting whether any `j <= i - 2` has `nums[j] > nums[i]`.

This reformulation is the key optimization. Counting both kinds of inversions would compute much more information than the Boolean result needs. Once the shared local pairs are conceptually removed from both counts, only the existence of an unmatched, nonlocal pair matters.

**Summarize all sufficiently earlier values with a maximum**

When examining index `i`, only values through index `i - 2` can form a nonlocal inversion ending at `i`. If their maximum is no greater than `nums[i]`, none of them is greater. If the maximum is greater, it supplies an explicit violating earlier value.

Variable `mx` stores that prefix maximum.

**Update in the correct order**

The loop begins at `i = 2`. Before comparing, it incorporates `nums[i - 2]`:

`mx = max(mx, nums[i - 2])`.

It then tests `mx > nums[i]`.

At index two, this includes only index zero, the only index at distance at least two. At the next step it includes indices zero and one, continuing correctly.

The code uses a walrus assignment to update and compare in one expression, but its meaning is exactly these two operations.

**Why starting `mx` at zero is safe**

The array is a permutation of `0..n - 1`, so every value is nonnegative. Before the first update, zero is no larger than the true included value after maximum calculation. Initializing to negative infinity would be more general, but zero is valid under this contract.

**Trace `[1,0,2]`**

At index two, `mx` becomes value one from index zero. One is not greater than two, so no nonlocal inversion exists.

The pair `(1,0)` is a local inversion and therefore also the only global inversion. Counts are equal and the method returns true.

**Trace `[1,2,0]`**

At index two, `mx` becomes one. Since one is greater than zero, indices zero and two form a nonlocal inversion.

There is also a local inversion between two and zero, so global inversions outnumber local ones. The method returns false immediately.

**Why one violation is enough**

Since every local inversion contributes equally to both counts, any nonlocal inversion increases only the global count. The existence of even one makes equality impossible. There is no need to count all inversions.

If no nonlocal inversion exists, every global inversion must be adjacent and hence local, so the sets of inversion pairs are identical.

**The invariant**

After updating at index `i`, `mx` equals `max(nums[0:i - 1])`, covering positions zero through `i - 2`. The comparison therefore tests exactly all possible nonlocal inversion partners ending at `i`.

Scanning all endpoints covers every pair with distance at least two once.

The invariant can also be established step by step. Before the first comparison at `i = 2`, adding `nums[0]` makes `mx` the maximum of exactly the eligible prefix. Suppose it is correct for one iteration. Advancing `i` by one makes the former index `i - 1` newly eligible because it is now two positions behind the new endpoint; the update incorporates exactly that value. No earlier value is lost, so the maximum again represents the complete eligible prefix.

Using only the maximum is sufficient because the question for a fixed endpoint is existential: does any earlier eligible value exceed `nums[i]`? If the largest eligible value does not exceed it, every smaller value also fails to form an inversion. If the largest does exceed it, its own index witnesses a violating pair. The algorithm therefore compresses a whole prefix without losing any information relevant to this decision.


If the method returns false, it found `j <= i - 2` with `nums[j] > nums[i]`, a global but nonlocal inversion, so the counts differ.

If it finishes, no such pair exists. All global inversions are adjacent, meaning every global inversion is local. Because every local inversion is always global, the two counts are equal and returning true is correct.

## Complexity detail

Let `n` be the permutation length. The loop visits each index from two onward once and performs constant work, giving `O(n)` time.

Only `mx`, indices, and current values are stored. Auxiliary space is `O(1)`, and the input is unchanged.

## Alternatives and edge cases

- **Check `abs(nums[i] - i) <= 1`:** For a permutation, this is another characterization of ideal permutations, but the prefix-maximum proof connects directly to nonlocal inversions.

- **Merge-sort inversion counting:** It can count all global inversions in `O(n log n)`, then compare with local count, but counting is unnecessary.

- **Nested pair loops:** Directly testing every global pair costs `O(n^2)`.

- **Length one or two:** No nonlocal pair exists, so the loop is empty and the answer is true.

- **One nonlocal violation:** Immediate false is conclusive.

- **Permutation guarantee:** It supports nonnegative initialization and uniqueness, though the prefix-maximum detection works more broadly with a proper negative-infinity start.

- **Local inversions:** They are deliberately ignored by the scan because they cannot create a count difference.

## General

**Translate the recursive definition directly**

The tree is defined by the maximum element of each current subarray:

- the maximum becomes that subtree's root;
- everything before the maximum builds the left subtree;
- everything after the maximum builds the right subtree.

The exact solution follows this definition literally. Its helper `dfs(nums)` returns the maximum binary tree for the list segment passed to it.

**The empty-segment base case**

If the current list is empty, there is no value from which to create a node, so `dfs` returns `None`. This is how missing children are represented.

The base case also ensures that `max(nums)` is called only for a nonempty list. A one-element list proceeds through the ordinary logic: its only value is the maximum, both slices are empty, and the resulting node has two null children.

**Choose the root and divide the input**

For a nonempty list, the helper performs:

1. `val = max(nums)` to find the largest value.
2. `i = nums.index(val)` to find its position.
3. Create `TreeNode(val)`.
4. Recursively construct the left child from `nums[:i]`.
5. Recursively construct the right child from `nums[i + 1:]`.

The source guarantee that all values are unique matters. It ensures the maximum has one unambiguous index. Without uniqueness, `index` would choose the first maximum, but the problem's construction rule would need to specify how ties are handled.

**Why array order is preserved**

The tree is not a binary search tree. Values are not divided by whether they are smaller or larger than the root; every other value is smaller because the root is the maximum. What determines the side is the original position.

Slicing preserves that order:

- `nums[:i]` contains exactly the prefix left of the maximum;
- `nums[i + 1:]` contains exactly the suffix right of the maximum.

Recursive calls apply the same rule inside those ordered pieces. No sorting is performed because sorting would destroy the positional relationships that define the tree.

**A complete walkthrough**

For `[3, 2, 1, 6, 0, 5]`, the maximum is six at index three. Six becomes the root. The left call receives `[3, 2, 1]` and the right call receives `[0, 5]`.

On the left:

- three is the maximum and becomes the left-subtree root;
- its left slice is empty;
- its right slice is `[2, 1]`;
- two then becomes a right child, with one as its own right child.

On the right:

- five is the maximum and becomes the right-subtree root;
- `[0]` builds its left child;
- its right slice is empty.

Every node position follows from which side of a maximum its value occupied in the current segment.

**Why the construction is correct**

Use induction on the length of the current list.

For length zero, the required tree is empty and `dfs` returns `None`. Assume the helper correctly constructs every segment shorter than a current nonempty segment.

The specification requires the current segment's unique maximum as the root. The helper selects exactly that value. The required left subtree is defined from the prefix before the maximum; `nums[:i]` is exactly that shorter prefix, so the induction assumption makes the recursive result correct. The same reasoning applies to the suffix and right subtree.

Attaching those two correct subtrees to the required maximum root produces precisely the maximum binary tree for the current segment. By induction, the top-level result is correct for the complete array.

**Why every input value becomes exactly one node**

At each call, one value is removed from further recursion by becoming the root. All earlier positions go to one child call, and all later positions go to the other. These two slices do not overlap and together contain every remaining value. Repeating the partition therefore creates one node per input value without duplication or omission.

**The exact source favors directness over the strongest bound**

This recursion is extremely close to the problem statement and is beginner-friendly conceptually. It does, however, rescan and copy subarrays. The manifest advertises a linear-time bound that belongs to the monotonic-stack construction discussed below, not to this literal source. The approach must describe the code that actually runs, so its true costs are detailed next.

## Complexity detail

Let `N` be the number of input values and let `m` be a current subarray length.

For one recursive call, `max(nums)` scans `m` values and `nums.index(val)` may scan `m` values again. Creating the two slices copies a total of `m - 1` references. Thus one call performs `O(m)` work.

If maxima repeatedly occur at an end, as in an increasing or decreasing array, the recursive sizes are `N, N - 1, N - 2, ...`. Their sum is quadratic, so worst-case time is `O(N^2)`. If maxima split segments roughly evenly, the recurrence produces `O(N log N)` time. The exact implementation is not `O(N)`.

Worst-case recursion depth is `O(N)` for a one-sided tree. Because Python slices allocate new lists and parent calls retain their own list objects while a child recurses, a skewed case can have total live slice storage of `O(N^2)`. The output tree itself contains `O(N)` nodes. Excluding output but including literal slices and recursion, worst-case auxiliary space is `O(N^2)`; without slicing and using index bounds, it would be `O(N)` for the stack.

The manifest's `O(N)` time and space match a monotonic-stack solution, not this recursive slicing implementation.

## Alternatives and edge cases

- **Monotonic decreasing stack:** Scan values once. Pop smaller nodes to become the current node's left child, and make the current node the right child of the remaining stack top. This constructs the same tree in `O(N)` time and `O(N)` space and matches the manifest.

- **Recursion with index boundaries:** Pass `left` and `right` rather than slices. This avoids quadratic slice storage but still rescans ranges for maxima, so worst-case time remains `O(N^2)`.

- **Range-maximum data structure:** Preprocess maximum-index queries, then recurse by boundaries. It can reduce repeated maximum search but is more machinery than the linear stack.

- **Sorting values first:** This is incorrect because original positions determine left and right subtrees. Sorting destroys the defining order.

- **One-element array:** The single value becomes a leaf because both recursive slices are empty.

- **Maximum at the first position:** The left child is null and every remaining value belongs to the right recursive segment.

- **Maximum at the last position:** Every remaining value belongs to the left segment and the right child is null.

- **Strictly increasing input:** The tree is completely left-skewed under the recursive definition, and the exact slicing implementation reaches its quadratic worst case.

- **Strictly decreasing input:** The tree is completely right-skewed and also triggers worst-case time, slice storage, and recursion depth.

- **Balanced maximum positions:** Runtime improves toward `O(N log N)`, but worst-case guarantees cannot assume such positions.

- **Duplicate values:** They are excluded by the contract. If allowed, a tie rule would be needed because `list.index` selects only the first occurrence.

- **Input mutation:** Slicing and scanning leave the original `nums` order and contents unchanged.

- **Recursion limit:** With up to one thousand values, a maximally skewed tree can approach Python's default recursion limit. An iterative monotonic-stack construction avoids that risk.

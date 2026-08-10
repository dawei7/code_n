## General

The linked list is already sorted in ascending order. That is exactly the order produced by an inorder traversal of a binary search tree: visit the left subtree, then the root, then the right subtree. The challenge is therefore not to sort the values. It is to choose a tree shape that preserves this inorder order and is height-balanced.

The selected solution first copies the linked-list values into a Python list named `nums`. This converts sequential-only linked-list access into constant-time indexed access. It then applies the familiar middle-element construction for a sorted array.

**Why copying the list helps**

A singly linked list can move forward from one node to the next, but it cannot jump directly to position `mid`. Repeatedly searching for the middle node inside every recursive sublist is possible, yet it scans many links again and leads to $O(n\log n)$ time.

The initial `while head` loop visits each list node once and appends its value to `nums`. After that pass, `nums[mid]` is available in constant time. The original nodes are not reused as tree nodes; their integer values are copied into newly constructed `TreeNode` objects.

Advancing the local `head` variable does not mutate the linked list. The solution reads `head.val`, then rebinds `head` to `head.next`. No `next` pointer is changed, so callers that retain the original head still have an intact list.

**The recursive interval promise**

The nested `dfs(i, j)` function uses inclusive boundaries. It returns a height-balanced binary search tree containing exactly `nums[i]` through `nums[j]`. When `i > j`, the interval is empty, so it returns `None`.

For a nonempty interval, `mid = (i + j) >> 1` chooses the lower middle index. Right shifting a nonnegative sum by one bit is equivalent to floor division by two. The solution recursively constructs:

- the left tree from `[i, mid - 1]`; and
- the right tree from `[mid + 1, j]`.

It then creates `TreeNode(nums[mid], l, r)`, placing the two completed recursive results into the root's child fields through the constructor.

Python evaluates the right-hand expressions in `l, r = dfs(...), dfs(...)` from left to right, but correctness does not depend on that order here. Both calls only read `nums` and operate on disjoint index intervals. Neither shares a moving cursor or modifies the other interval.

**Why the result obeys binary-search-tree ordering**

Because `nums` is strictly increasing, every index below `mid` contains a value smaller than `nums[mid]`, and every index above `mid` contains a value larger than it. The recursive split puts the first set exclusively in the left subtree and the second set exclusively in the right subtree.

The same reasoning applies inside each child interval. Therefore every created node has only smaller values in its left subtree and only larger values in its right subtree. This establishes the binary-search-tree property without performing a single value comparison during construction.

The intervals also account for every input exactly once. One call consumes its middle index, and its two child intervals are disjoint and cover all remaining indices. Eventually every nonempty interval reaches a one-element interval, which creates a leaf. Empty intervals create absent children. Thus no list value is lost or duplicated.

**Why midpoint splitting guarantees height balance**

An interval of $m$ values leaves $m-1$ values after selecting its root. Choosing a middle position distributes those values into groups of sizes

$$
\left\lfloor\frac{m-1}{2}\right\rfloor
\quad\text{and}\quad
\left\lceil\frac{m-1}{2}\right\rceil.
$$

The two sizes differ by at most one. Each group is divided by the same rule, so both child trees have equal height or heights differing by one. This holds recursively at every node, which is the required height-balanced property.

When an interval has even length, the lower middle is selected and the right interval receives one extra element. Selecting the upper middle would also be valid. That freedom is why an accepted tree need not have the exact level-order serialization shown in the Reference.

**Walking through the main example**

The list `[-10, -3, 0, 5, 9]` becomes the same five-element `nums` list. The first call owns indices zero through four and chooses index two, value zero, as the root.

Indices zero and one form the left side. Their lower middle is index zero, so `-10` becomes the left child of zero and `-3` becomes the right child of `-10`. Indices three and four similarly produce `5` with right child `9`.

Inorder traversal visits `-10`, `-3`, `0`, `5`, and `9`, exactly matching the original list. The root's subtrees have equal height, and every lower node's child-height difference is at most one. The shape differs from the displayed output but is explicitly one of the accepted possibilities.

**Dependencies supplied by the environment**

The selected file annotates names such as `Optional`, `ListNode`, and `TreeNode` without importing or defining them in active code. It assumes the judge or application harness supplies those names. A standalone Python file would need the typing import and the two node definitions before this class is evaluated.

## Complexity detail

Let $n$ be the number of linked-list nodes. The conversion loop visits all $n$ nodes once, taking $O(n)$ time. The recursive construction creates one tree node for each of the $n$ positions, also taking $O(n)$ time. These phases are sequential, so their sum is $O(n)$, not $O(n^2)$.

Midpoint splitting makes the recursion depth $O(\log n)$. The stack therefore uses $O(\log n)$ space.

However, the exact selected source also allocates `nums` with all $n$ values. That array is auxiliary workspace, not part of the required returned tree. Its $O(n)$ storage dominates the logarithmic stack, so the exact auxiliary-space complexity is $O(n)$.

The manifest's stated $O(\log n)$ space bound does not describe this implementation. That bound belongs to an inorder-simulation technique that advances through the linked list while recursively constructing the tree and does not allocate a value array. For this source, reporting only the recursion stack would omit a material allocation.

The returned tree itself contains $n$ new nodes and uses another $O(n)$ of output space. Whether output is counted or excluded, the overall asymptotic memory remains $O(n)$ because `nums` alone is linear.

## Alternatives and edge cases

- **Inorder simulation with one moving list pointer:** Count the nodes, recursively build the left shape, consume one list value for the root, and then build the right shape. It achieves $O(n)$ time and $O(\log n)$ auxiliary stack space without the copied array.
- **Repeated slow/fast midpoint search:** Split the linked list around its middle for every subtree. It uses only logarithmic recursion space but repeats scans, producing $O(n\log n)$ time.
- **Destructive list splitting:** Cutting `next` pointers can make midpoint recursion easier, but it mutates the caller's list and still retains the repeated-scan cost.
- **Upper-middle array construction:** Selecting the right middle for even intervals changes the valid shape but not ordering, balance, or complexity.
- **Direct ascending BST insertion:** Inserting values in list order creates a right-skewed chain, so it fails the balance requirement and can take quadratic time.
- **Empty list:** The conversion loop leaves `nums` empty; `dfs(0, -1)` immediately returns `None`, matching the `[]` output.
- **Single node:** The sole value becomes a leaf because both recursive intervals are empty.
- **Even node count:** The lower-middle convention gives the right subtree one additional node, which still keeps the height difference within one.
- **Strict ascending order:** It guarantees strict left-smaller and right-larger relationships. No duplicate-placement policy is needed.
- **Preserving the input:** Rebinding `head` while copying does not sever or rewrite any `next` link.
- **Maximum length:** Construction depth remains logarithmic for $2\cdot10^4$ nodes, though the `nums` array and returned tree both scale linearly.
- **Output comparison:** Tests must accept any tree whose inorder values match the list and whose node heights satisfy the balance rule; one fixed serialization is too restrictive.
- **Manifest discrepancy:** When evaluating this exact source, use $O(n)$ auxiliary space. Do not attribute the competitive inorder-simulation bound to the array-copy implementation.

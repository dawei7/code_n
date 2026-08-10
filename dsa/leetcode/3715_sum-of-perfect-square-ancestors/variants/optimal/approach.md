## General

**Replace a product test with a reusable value signature**

For every node, the task asks how many of its ancestors form a perfect-square product with it. Testing all ancestor pairs directly can take quadratic time on a chain-shaped tree. The crucial number-theory observation is that whether a product is a perfect square depends only on the parity of each prime exponent.

Write a positive integer in prime-factorized form:

$$
x = p_1^{e_1}p_2^{e_2}\cdots p_t^{e_t}.
$$

The integer is a perfect square exactly when every exponent `e_i` is even. Define the square-free kernel of `x` by keeping a prime once when its exponent is odd and removing it when its exponent is even:

$$
\operatorname{kernel}(x)
= \prod_{e_i\ \text{odd}} p_i.
$$

For example,

$$
12 = 2^2 \cdot 3
\quad\Longrightarrow\quad
\operatorname{kernel}(12)=3,
$$

and

$$
75 = 3 \cdot 5^2
\quad\Longrightarrow\quad
\operatorname{kernel}(75)=3.
$$

Their product is `12 * 75 = 900 = 30²`. This is not a coincidence. In a product `x * y`, the exponent of each prime is the sum of its exponents in `x` and `y`. That sum is even precisely when the two original exponents have the same parity. Therefore,

$$
x y \text{ is a perfect square}
\quad\Longleftrightarrow\quad
\operatorname{kernel}(x)=\operatorname{kernel}(y).
$$

The original pair condition has now become equality of two integer keys. The solution computes a kernel for every possible value and then counts equal keys along the current ancestor path.

**Build smallest prime factors with a sieve**

Let `limit = max(nums)`. The array `smallest_prime` has one entry for every value from zero through `limit`. The outer sieve loop examines each `prime` from two upward. If `smallest_prime[prime]` is already nonzero, a smaller prime previously marked it, so it is composite and requires no new marking pass.

If the entry is zero, the number is prime. The code records itself as its smallest prime factor. When `prime * prime <= limit`, it visits multiples beginning at `prime * prime` and fills only entries that are still zero. Starting at the square is safe because every smaller composite multiple of this prime has another factor smaller than the prime and was already encountered. Filling only zero entries ensures that the first factor recorded is the smallest one.

After this sieve, every integer `value >= 2` has `smallest_prime[value]` equal to its smallest prime factor. Values zero and one do not need a prime factor; the kernel array starts filled with one, which correctly gives `kernel[1] = 1`.

**Compute every square-free kernel without refactoring each number**

The code fills `kernel` in increasing value order. For a current `value`, let

`prime = smallest_prime[value]`

and

`quotient = value // prime`.

There are two cases:

- If `quotient % prime == 0`, then `value` contains at least two copies of `prime`. Removing `prime²` does not change any exponent parity, so `kernel[value] = kernel[quotient // prime]`.
- Otherwise, `value` contains exactly one copy of its smallest prime. That copy has odd parity and must appear in the kernel, so `kernel[value] = kernel[quotient] * prime`.

All referenced quotients are smaller than `value`, so their kernels have already been computed. For `72 = 2³ * 3²`, repeated use of the recurrence removes pairs of equal prime factors and leaves kernel two. It accomplishes the same result as full factorization while sharing work across the entire range.

**Turn the edge list into a traversable tree**

The input edges are undirected even though node zero is designated as the root. The solution constructs an adjacency list by adding each endpoint to the other's neighbor list. During traversal, each stack entry carries both `node` and `parent`. Skipping `parent` prevents immediately following the undirected edge back upward, so every other neighbor is a child in the rooted view.

**Count matching ancestors with entry and exit events**

The dictionary `active` describes only the current root-to-node traversal path. For a kernel key `k`, `active[k]` is the number of already-entered nodes with kernel `k` that are ancestors of the node about to be processed.

The explicit stack contains triples `(node, parent, entering)`. An entering event performs these operations in order:

1. Compute `key = kernel[nums[node]]`.
2. Add `active.get(key, 0)` to `answer`.
3. Increment `active[key]` so this node is visible to its descendants.
4. Push an exit event for this node.
5. Push entering events for its children.

The order of the first two path operations is essential. The answer is increased before the current node is inserted, so a node is never counted as its own ancestor. Every active matching node is a genuine strict ancestor and, by equal kernels, forms a perfect-square product with the current node.

The exit event decrements `active[key]`. Although the exit is pushed before the children, the stack is last-in, first-out: all child events and all events in their subtrees are processed before the exit is popped. Thus the node remains active throughout every descendant's visit. Once its subtree is finished, removing it prevents the node from being incorrectly treated as an ancestor of a node in a sibling subtree.

For a root-to-current path with kernels `[6, 10, 6, 6]`, the last node sees two active ancestors with kernel six and contributes two pairs immediately. There is no need to inspect those ancestors individually.

**Why the accumulated total is exact**

Consider any valid ordered descendant-ancestor pair. When the traversal enters the descendant, its ancestor has already been entered and cannot yet have exited because the descendant lies inside that ancestor's subtree. The ancestor's kernel is therefore present in `active`. Since a square product means the kernels are equal, that ancestor contributes exactly one to the lookup count.

Conversely, every unit counted by the lookup corresponds to a node currently on the strict ancestor path with the same kernel. It is therefore an ancestor, and the kernel equivalence proves that the product is a perfect square. Each pair is counted once, at the descendant's entry, so the final sum has neither omissions nor duplicates.

## Complexity detail

Let `n` be the number of nodes and let

$$
M = \max(\texttt{nums}).
$$

The smallest-prime-factor sieve takes $O(M \log\log M)$ time by the standard sieve analysis. Filling `kernel[2]` through `kernel[M]` takes $O(M)$ time because each value uses one constant-time recurrence. Building the adjacency list takes $O(n)$ time for the tree's `n - 1` edges. Entry and exit processing takes $O(n)$ expected time: every node has exactly one of each event, and dictionary operations are expected $O(1)$. The total expected time is $O(M \log\log M + n)$.

The two value-indexed arrays require $O(M)$ space. The adjacency list stores $O(n)$ vertices and edge entries. The explicit DFS stack can grow to $O(n)$, and `active` can retain up to $O(n)$ keys, including keys whose counts have returned to zero because the implementation decrements rather than deletes them. The overall auxiliary space complexity is $O(M + n)$. Using an explicit stack also avoids Python recursion-depth failure on a chain of up to $10^5$ nodes.

## Alternatives and edge cases

- **Check every node against all ancestors:** Carrying an ancestor list and testing each product is conceptually direct, but a chain has $\Theta(n^2)$ descendant-ancestor pairs. Kernel counts compress all equal-signature ancestors into one dictionary lookup.
- **Call a square-root test for each pair:** Integer square-root testing avoids floating-point errors but does not reduce the number of pairs. The bottleneck is pair enumeration, not the individual square test.
- **Factor every node independently:** Trial division up to each value's square root repeats work across equal and nearby values. The smallest-prime-factor table preprocesses the complete bounded value domain and gives constant-work kernel recurrence per value.
- **Recursive depth-first search:** The same enter/add/recurse/remove logic is valid recursively, but a tree shaped like one long chain can exceed Python's recursion limit. Explicit entry and exit events preserve the logic safely.
- **Count before versus after insertion:** Inserting the current key before adding `active[key]` would count the node paired with itself. The exact source deliberately adds the current number of matching ancestors first.
- **Forgetting the exit decrement:** Then nodes from completed sibling subtrees would remain active even though they are not ancestors of the next sibling. The path dictionary must reflect ancestry, not all nodes visited so far.
- **Kernel one:** Perfect squares such as one, four, nine, and thirty-six all have kernel one. They correctly match one another, and `1 * square` is also a square.
- **Equal values are not required:** Numbers such as 12 and 75 have the same kernel even though they differ. Grouping by the raw value would miss valid products.
- **The root:** It has no strict ancestors, and `active` is empty when its entering event is processed. It contributes zero without requiring a special branch, then becomes available for every descendant.
- **A single-node tree:** The stack processes one entry and one exit, no edge is traversed, and the returned answer is zero.
- **Repeated kernel keys on one path:** `active` stores a count rather than a Boolean. If three ancestors share the current node's key, all three distinct pairs must be added.
- **Zero-count dictionary entries:** Leaving a key with value zero is harmless because later lookups add zero and a later entry increments it again. Removing zero entries could reduce memory constants but would not change the asymptotic bound or result.
- **Large answer:** A path can contain $\Theta(n^2)$ valid pairs, so the numerical answer may be much larger than `n`. Python integers handle this automatically; fixed-width implementations should use a sufficiently wide integer type.

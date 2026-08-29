## General

Making a square is equivalent to assigning every matchstick to one of four groups whose sums are equal. The target side length is forced: it must be one quarter of the total length. The exact solution performs depth-first assignment, trying each stick on each side without ever allowing a side to exceed the target.

**Reject impossible totals immediately**

`divmod(sum(matchsticks), 4)` returns the candidate side length `x` and the remainder `mod`. A nonzero remainder means the perimeter cannot be divided into four equal integer side sums, so return false.

Even with divisible total, a stick longer than `x` cannot fit on any side because sticks cannot be broken. The check `x < max(matchsticks)` rejects that case before search.

Input is nonempty, so `max` is safe. All stick lengths are positive, which makes “do not exceed the target” a permanent pruning condition: later choices can only increase side sums.

**Place larger sticks first**

The list is sorted in descending order. Large sticks are the hardest to place and most likely to overflow a side. Trying them first exposes impossible branches near the top of the recursion tree instead of after many small-stick choices.

Sorting does not change which partitions exist, but it can dramatically improve practical search. It also mutates the input order.

**Recursive state**

`edges` stores the four current side sums. `dfs(u)` means that sticks at indices below `u` have been assigned legally and the algorithm must place `matchsticks[u:]`.

For the current stick, try side indices zero through three:

1. Add its length to `edges[i]`.
2. Continue recursively only if the sum is at most target `x`.
3. If that branch fails, subtract the stick again before trying another side.

This add-recurse-subtract pattern is backtracking. Restoring the side sum is essential so alternative branches begin from the same state.

**Why the base case needs no explicit equality check**

When `u == len(matchsticks)`, every stick has been placed, no side ever exceeded `x`, and total assigned length is exactly `4x`. Four side sums each at most `x` can total `4x` only when all four equal `x`. Therefore the base case can return true immediately.

This argument also proves every accepted assignment uses every stick exactly once: recursion advances `u` by one only after assigning the current array entry to one side.

**Skip symmetric side choices**

The four side labels are interchangeable. If two side sums are equal before placing the current stick, putting it on either produces states that differ only by swapping side names. Exploring both would repeat identical future possibilities.

The condition

`if i > 0 and edges[i - 1] == edges[i]: continue`

skips the later of adjacent equal-load sides. The recursive construction maintains the side-load ordering induced by trying sides from left to right, so equal loads occur in interchangeable runs. This removes many duplicate branches, especially at the beginning when all four sides are zero.

The pruning does not remove a unique partition: any solution using a skipped equal side can be relabeled to use the first equivalent side instead.

**Trace `[1,1,2,2,2]`**

The total is eight, so each side must sum to two. Descending sort gives `[2,2,2,1,1]`. The first three length-two sticks occupy three separate sides. The two length-one sticks join on the remaining side. Every edge reaches two, and the base case returns true.

For `[3,3,3,3,4]`, the total is 16 and target is four. The length-four stick fills one side, but each length-three stick needs a length-one partner that does not exist. Backtracking exhausts legal placements and returns false.

**Why exhaustive search is correct**

Every valid square defines one assignment of each indexed stick to a side. At recursion depth `u`, the loop includes the side used by that valid assignment. Because its final side sum is `x` and all lengths are positive, the partial sum on that branch never exceeds `x`, so the branch is not pruned. Symmetric skipping retains an equivalent relabeling. Thus some explored path reaches the base case whenever a square exists.

Conversely, every successful path assigns all sticks exactly once and, by the total-sum argument, ends with four target sums. It therefore describes a valid square.

## Complexity detail

Let $n$ be the number of matchsticks. In the unpruned worst case, each stick has four side choices, giving $O(4^n)$ recursive branches. Each call does constant work per attempted side, so $O(4^n)$ is a faithful conservative time bound. Descending order, overflow checks, and symmetry skipping greatly reduce typical exploration but do not establish the manifest's stated $O(n2^n)$ subset-DP bound for this exact backtracking source.

Recursion depth is at most $n$, and `edges` has fixed length four. Apart from sorting workspace, search uses $O(n)$ call-stack space. Python's in-place sort can use $O(n)$ temporary memory. There is no memo table of size $2^n$.

## Alternatives and edge cases

- **Subset-mask dynamic programming:** Track reachable used-stick masks and current side remainder in $O(n2^n)$ time and $O(2^n)$ space. This matches the manifest but is not the exact implementation.
- **Memoized backtracking:** Cache canonicalized side loads plus index to avoid revisiting equivalent states, at additional memory cost.
- **No descending sort:** Correct but often explores many doomed small-stick arrangements before discovering a large stick cannot fit.
- **Perimeter not divisible by four:** Rejected before recursion.
- **Largest stick too long:** Cannot fit any side and is rejected immediately.
- **Exactly four sticks:** A square exists only when all four lengths equal the forced side length.
- **Duplicate lengths:** They are distinct physical sticks, but sorting and side symmetry safely reduce equivalent assignment orders.
- **All side loads equal:** Only the first equivalent side is tried for the next stick.
- **Input mutation:** Descending sort changes `matchsticks` order.
- **Positive-length guarantee:** It makes overflow pruning permanent and supports the base-case total argument.

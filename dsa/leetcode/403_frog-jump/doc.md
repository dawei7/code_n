# Frog Jump

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 403 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/frog-jump/) |

## Problem Description
### Goal
Stones lie at integer positions sorted in ascending order along a river, beginning at position zero. A frog starts on the first stone and must make its first jump exactly one unit, landing on a stone rather than in water.

After a jump of length `k`, the next jump may have positive length $k - 1$, `k`, or $k + 1$. Return `True` when some sequence of legal landings reaches the final stone and `False` otherwise. The frog may skip stones but cannot jump backward or remain in place, and earlier choices affect which jump lengths are available later.

### Function Contract
**Inputs**

- `stones`: strictly increasing stone positions beginning at zero

**Return value**

- Return `True` when some valid jump sequence lands on the final stone; otherwise return `False`.

### Examples
**Example 1**

- Input: `stones = [0,1,3,5,6,8,12,17]`
- Output: `True`

**Example 2**

- Input: `stones = [0,1,2,3,4,8,9,11]`
- Output: `False`

**Example 3**

- Input: `stones = [0,1]`
- Output: `True`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**A stone position alone is not enough state**

Future options depend on the jump used to arrive, so associate each stone with the set of reachable last-jump lengths. Initialize position zero with jump length zero; applying $0 + 1$ enforces the required first jump.

**Propagate the three legal successors**

Process stones from left to right. For every stored last jump `k`, try $k - 1$, `k`, and $k + 1$, ignoring nonpositive lengths. If the resulting position is a stone, add that new jump length to its set.

**Merge paths that reach the same state**

Many jump sequences can arrive at the same `(position, last_jump)` pair. A set stores that pair once because all future behavior from it is identical. This prevents exponential re-exploration without discarding any distinct future option.

**Why reachability propagation is complete**

Every inserted state extends a previously reachable state by one permitted positive jump, so it represents a valid path. Conversely, take any valid path and consider its states in order: the initial state exists, and propagation tries exactly the next path jump, so induction inserts every state on that path. The final stone is reachable precisely when its set is nonempty.

#### Complexity detail

For `n` stones, a stone can be associated with $O(n)$ distinct jump lengths, and each state generates three constant-time transitions. Time and stored state are therefore $O(n^2)$.

#### Alternatives and edge cases

- **Memoized depth-first search:** explores the same position-and-jump states recursively and has the same asymptotic bounds.
- **Uncached path search:** may revisit equivalent states along exponentially many jump sequences.
- **Scan all prior edges for every candidate jump:** is correct but can take $O(n^3)$ time.
- If the second stone is not at position one, the first jump cannot land.
- Jump length zero or negative is never permitted.
- A large gap can make all later stones unreachable.
- Different last-jump lengths on the same stone must remain separate states.

</details>

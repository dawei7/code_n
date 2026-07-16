# Maximum Number of Achievable Transfer Requests

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1601 |
| Difficulty | Hard |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/) |

## Problem Description
### Goal
There are `n` full office buildings numbered from `0` through `n - 1`. Each entry `requests[i] = [from_i, to_i]` represents one employee who wants to leave building `from_i` and move into building `to_i`.

Choose as many requests as possible while leaving every building's employee count unchanged. For each building, the number of accepted requests leaving it must equal the number entering it. A request whose source and destination are equal is already balanced and may be accepted without affecting any other building. Return the maximum size of an achievable subset.

### Function Contract
**Inputs**

- `n`: the number of buildings, with $1 \le n \le 20$.
- `requests`: a list of $m$ source-destination pairs, with $1 \le m \le 16$ and both endpoints in $[0,n-1]$.

**Return value**

Return the greatest number of requests whose combined net employee change is zero at every building.

### Examples
**Example 1**

- Input: `n = 5`, `requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]`
- Output: `5`

**Example 2**

- Input: `n = 3`, `requests = [[0,0],[1,2],[2,1]]`
- Output: `3`

**Example 3**

- Input: `n = 4`, `requests = [[0,3],[3,1],[1,2],[2,0]]`
- Output: `4`

### Required Complexity
- **Time:** $O(n2^m)$
- **Space:** $O(n+m)$

<details>
<summary>Approach</summary>

#### General

Let $m$ be the number of requests.

**Represent feasibility with net changes.** Maintain an array `balance` initialized to zero. Accepting `[from, to]` subtracts one at `from` and adds one at `to`. A completed subset is achievable exactly when every entry is zero, which directly states that incoming and outgoing accepted transfers match for every building.

**Explore accept and reject choices in place.** At request index `i`, first apply its two balance changes and recurse with one more chosen request. Undo both changes on return, then recurse without the request. This restoration makes every recursive path represent one distinct subset while sharing a single $O(n)$ balance array.

**Prune branches that cannot improve the incumbent.** If `chosen + (m - i)` is no greater than the best feasible count already found, even accepting every remaining request cannot produce a better answer. Stop that branch. Trying acceptance first tends to discover large feasible subsets early and strengthens this upper bound; it does not discard any potentially improving solution.

Every subset corresponds to one unique sequence of accept/reject branches. At a leaf, the balance test accepts precisely the achievable subsets. The algorithm records the largest accepted branch count, and the pruning rule removes only branches whose theoretical maximum cannot exceed that recorded count. Therefore the final value is the maximum achievable number of requests.

#### Complexity detail

There are at most $2^m$ accept/reject leaves and fewer than twice as many recursive states. Checking all $n$ balances at an unpruned leaf gives the conservative $O(n2^m)$ time bound; the upper-bound pruning can greatly reduce actual work. The balance array uses $O(n)$ space and recursion reaches depth $m$, for $O(n+m)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate integer masks:** Rebuild the balance array for each of the $2^m$ masks. This is correct but repeats request processing and costs $O(m2^m+n2^m)$ time.
- **Meet in the middle:** Split requests into two halves and match opposite balance vectors. This can reduce the exponential base at the cost of substantially more state and bookkeeping.
- A self-transfer `[x, x]` changes no balance and can always be included.
- A single one-way transfer between different buildings cannot be achieved by itself, so the answer may be `0`.
- Several copies of the same direction may be balanced by fewer reverse requests only up to matching multiplicity.
- Buildings absent from all selected requests remain balanced automatically.

</details>

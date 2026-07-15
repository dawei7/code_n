# Number of Ways to Wear Different Hats to Each Other

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1434 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Bit Manipulation, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/) |

## Problem Description

### Goal

A group of people is choosing hats numbered from `1` through `40`. For each person `i`, `hats[i]` lists exactly the hat numbers that person is willing to wear.

Count the assignments in which every person receives exactly one liked hat and no two people receive the same hat. Two assignments are different when at least one person receives a different hat. Because the count can be large, return it modulo $1{,}000{,}000{,}007$.

### Function Contract

**Inputs**

- `hats`: a list of $p$ preference lists, where $1 \le p \le 10$.
- Each `hats[i]` contains between $1$ and $40$ distinct integers from $1$ through $40$.

**Return value**

- The number of valid one-liked-hat-per-person assignments with all assigned hats distinct, modulo $1{,}000{,}000{,}007$.

### Examples

**Example 1**

- Input: `hats = [[3,4],[4,5],[5]]`
- Output: `1`

**Example 2**

- Input: `hats = [[3,5,1],[3,5]]`
- Output: `4`

**Example 3**

- Input: `hats = [[1,2,3],[2,3,5],[1,3,5]]`
- Output: `11`

### Required Complexity

- **Time:** $O(40p2^p)$
- **Space:** $O(2^p)$

<details>
<summary>Approach</summary>

#### General

**Choose the small dimension for the mask.** There may be 40 hat numbers, so a mask over hats would require $2^{40}$ states. There are at most 10 people, making a $p$-bit mask practical. Bit `i` is set exactly when person `i` has already received a hat.

**Transpose preferences by hat.** Build `people_by_hat[h]`, the people willing to wear hat `h`. Processing hats rather than people gives each physical hat a single decision point. At that point it is either unused or assigned to one compatible unassigned person; it can never be selected again later.

**Define the processed-prefix state.** Before considering the next hat, `dp[mask]` is the number of assignments using only previously processed hat numbers that assign exactly the people in `mask`. Initially `dp[0] = 1` because using no hats assigns nobody in one way, while every other state is zero.

**Derive the two transitions for one hat.** Copy `dp` into `next_dp` to represent leaving the current hat unused. For every reachable `mask` and every compatible person `i` whose bit is clear, add `dp[mask]` to `next_dp[mask | (1 << i)]`. Use a fresh array: updating `dp` in place could assign the same current hat to several people through a chain of newly created states.

**Why each valid assignment is counted exactly once.** Inductively, `dp[mask]` counts precisely the assignments of the processed hats to `mask`. Skipping the current hat preserves each such assignment. Assigning it to one clear-bit compatible person creates every assignment that uses this hat, and the recipient uniquely identifies its predecessor after the hat is removed. The two groups are disjoint, and no transition assigns a processed hat twice. After hat 40, the full mask therefore counts exactly all valid assignments.

**Apply the modulus during accumulation.** Addition is the only counting operation, so reducing each updated state modulo $1{,}000{,}000{,}007$ preserves the final residue and keeps intermediate integers bounded. The answer is `dp[(1 << p) - 1]`, the state in which every person has been assigned.

#### Complexity detail

There are 40 hat iterations and $2^p$ masks. For a hat, at most $p$ compatible recipients are examined per reachable mask, giving $O(40p2^p)$ time. Two arrays of $2^p$ counts and the preference index use $O(2^p+40p)$ space; because 40 is fixed and $p \le 10$, the state-dominant auxiliary bound is $O(2^p)$.

#### Alternatives and edge cases

- **Backtrack by person:** Trying each liked unused hat is correct, but dense preferences can enumerate a factorial number of partial assignments before counting them.
- **Mask the hats:** A 40-bit availability mask has an infeasible $2^{40}$ state space; mask the at-most-ten people instead.
- **Process people with a used-hat set:** Memoization still needs to distinguish many subsets of up to 40 hats, losing the small-state advantage.
- **One shared hat:** If several people like only the same hat, no full assignment exists and the full-mask count remains zero.
- **Disjoint singleton preferences:** Exactly one assignment exists.
- **Unused hats:** Hats need not be assigned, which is why every iteration includes the skip transition.
- **Sparse hat numbers:** Iterating all 40 identifiers is safe; hats liked by nobody only copy the state array.
- **Duplicate counting:** Each person list contains distinct hat numbers, so the transpose should add a person once per liked hat.

</details>

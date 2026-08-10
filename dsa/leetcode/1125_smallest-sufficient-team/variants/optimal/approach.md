## General

**Represent a skill set as a bitmask**

There are at most sixteen required skills, so one integer can encode any subset. Dictionary `d` maps each skill string to a bit position.

For person `i`, mask `p[i]` starts at zero. For every skill they have,:

`p[i] |= 1 << d[skill]`

sets the corresponding bit. Repeated OR operations combine skills without duplication.

The complete required set is mask `(1 << m) - 1`, whose lowest $m$ bits are all one.

**Define the dynamic-programming state**

`f[mask]` is the smallest number of people known to cover exactly the skill union represented by `mask`. Initially every state is infinity except `f[0] = 0`, because an empty team covers no skills.

The word “exactly” refers to the union mask. A team may have overlapping skills, but OR collapses overlaps and records the total covered subset.

**Try adding every person**

From reachable mask `i`, adding person `j` produces:

`next_mask = i | p[j]`.

The candidate team size is `f[i] + 1`. If it is strictly smaller than `f[next_mask]`, the algorithm updates the size and records how this state was reached.

`g[next_mask] = j` stores the last added person, and `h[next_mask] = i` stores the previous mask.

The strict comparison means equal-sized alternatives do not replace the first one found. That is valid because the contract accepts any smallest team.

**Why one ascending pass over masks is enough**

OR can only set bits; it never clears them. A transition that adds at least one new skill produces a numeric mask greater than the old mask. A person adding no new skill leaves the same mask, but cannot improve it because it adds one person.

Therefore, useful transitions move forward in the loop’s ascending mask order. By the time state `i` is processed, every transition that could optimally reach it came from a smaller mask already processed.

This makes the bitmask states a directed acyclic progression and avoids repeated relaxation rounds.

**Why the DP finds the minimum team**

Any team can be ordered arbitrarily. Starting from mask zero and adding its people one by one creates the same sequence of OR transitions considered by the DP.

Inductively, `f[mask]` is no larger than the size of any team reaching that mask because the DP considers every possible last person. Conversely, each finite value is built by actual people recorded through transitions, so it corresponds to a real team.

Thus the value at the full mask is exactly the minimum sufficient-team size.

**Reconstruct the selected indices**

Start from the full mask. `g[i]` identifies the person used by the last improving transition, so that index is appended. `h[i]` moves to the skill mask covered before that person.

Every recorded transition strictly added a skill, so predecessor masks move toward zero and reconstruction terminates. The collected order is reverse construction order, but the contract permits any output order, so no reversal is necessary.

The guarantee that a sufficient team exists ensures the full mask is reachable and its predecessor records are valid.

The predecessor arrays are updated together with `f`. Therefore, they always describe the same improving transition that established the current minimum size, rather than a stale path from an older, larger team.

## Complexity detail

Let $s$ be the number of required skills and $p$ the number of people. Constructing person masks processes the listed skill memberships.

There are $2^s$ masks, and each reachable mask tries all $p$ people, giving $O(p2^s)$ time.

Arrays `f`, `g`, and `h` each contain $2^s$ entries, while person masks contain $p$ entries. Exact space is $O(2^s+p)$ plus the answer. The manifest’s $O(p2^s)$ space is a valid loose upper bound but is not tight for this implementation.

## Alternatives and edge cases

- **Top-down memoization:** Recursively choose uncovered skills and cache masks. It can skip unreachable states but uses recursion.
- **Store teams directly in DP:** Keep a list or bitset of people per skill mask. Reconstruction becomes easy, but copying teams increases memory and transition cost.
- **Breadth-first search over masks:** Each added person is one edge, so BFS finds a minimum number of people. DP with size relaxation expresses the same state graph.
- **Person with no required skills:** Their mask is zero and can never improve a state.
- **Redundant person:** A person whose skills add nothing to a current mask produces no update.
- **Overlapping skills:** OR safely combines them without double counting.
- **One person covers everything:** The full mask receives size one and reconstructs that index.
- **Several optimal teams:** Strict improvement preserves one arbitrary valid optimum.
- **One required skill:** The first useful person can form a size-one solution.
- **All skills unique across people:** Every necessary person is included.
- **Guaranteed solution:** No unreachable-full-mask error handling is needed.
- **Output order:** Reconstruction is backward, but arbitrary team-index order is allowed.

# Dota2 Senate

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 649 |
| Difficulty | Medium |
| Topics | String, Greedy, Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/dota2-senate/) |

## Problem Description
### Goal
The Dota2 senate contains members of the `Radiant` and `Dire` parties in the order represented by the characters of `senate`. Voting proceeds in repeated rounds, with every senator who still has rights acting in that established circular order.

On a turn, a senator may ban one opposing senator's rights for the current and all later rounds, or announce victory once every senator who still has rights belongs to the same party. Assume all senators make optimal choices. Return `"Radiant"` or `"Dire"` to name the party that eventually wins.

### Function Contract
**Inputs**

- `senate`: a nonempty string where `R` denotes a Radiant senator and `D` denotes a Dire senator in initial speaking order
- Senators make optimal choices; an active senator can ban one active opponent or declare victory when no opponent remains

**Return value**

- `"Radiant"` or `"Dire"`, naming the party that eventually retains voting rights

### Examples
**Example 1**

- Input: `senate = "RD"`
- Output: `"Radiant"`

**Example 2**

- Input: `senate = "RDD"`
- Output: `"Dire"`

**Example 3**

- Input: `senate = "DRD"`
- Output: `"Dire"`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Queue each party's next speaking positions**

Store the initial indices of Radiant senators in one queue and Dire senators in another. The front of each queue is that party's earliest active senator, so the smaller of the two indices acts first.

**Pair the next opponents greedily**

Remove one index from each queue. The earlier senator bans the later senator. Reinsert only the winner with index increased by `N`, representing that senator's position in the next circular round after every current-round position.

**Why banning the next opponent is optimal**

An acting senator gains nothing by allowing an earlier opposing turn to survive in favor of banning a later one. Banning the opponent who would act next removes the maximum immediate threat and cannot delay any allied turn. Thus each queue-front comparison faithfully represents optimal play.

**Why index extension preserves round order**

Adding `N` places a surviving senator after all positions in the current cycle while retaining its relative seat order in later cycles. The queues therefore remain chronologically ordered without explicitly rebuilding rounds. Each comparison eliminates one senator permanently; when one queue empties, the other party can declare victory.

#### Complexity detail

Initialization scans `N` senators. Each queue comparison permanently eliminates one senator and performs constant-time queue operations, so there are at most $N - 1$ comparisons and $O(N)$ total time. Both queues together store at most `N` indices, using $O(N)$ space.

#### Alternatives and edge cases

- **Single queue with pending-ban counters:** cycle senators and consume or create opposing bans; it is correct but requires careful party-count bookkeeping.
- **Rebuild the active senate each round:** simulates the statement directly, but repeated scans and deletions can become quadratic.
- **Array queues using front indices:** provides the same linear behavior as deques without removing from the physical front.
- A senate containing only one party ends immediately.
- With one senator from each party, the earlier index wins.
- A senator that survives a round may act again after its index is advanced by `N`.
- Initial majority alone does not determine the winner; circular speaking order matters.

</details>

# Incremental Memory Leak

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1860 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/incremental-memory-leak/) |

## Problem Description
### Goal
Two memory sticks initially have `memory1` and `memory2` available bits. A
faulty program requests an increasing allocation every second: at second $i$,
it needs exactly $i$ bits. The request is taken from the stick with more
available memory at that moment; when both sticks are equal, the first stick is
chosen.

The program crashes at the first second when neither stick contains enough
available bits for that second's request. Return the crash time together with
the unused memory remaining on the first and second sticks at that instant.

### Function Contract
**Inputs**

- `memory1`: the first stick's initial available memory, from $0$ through
  $2^{31}-1$ bits.
- `memory2`: the second stick's initial available memory over the same range.

Let $M = \texttt{memory1} + \texttt{memory2}$ denote the initial total memory.

**Return value**

An integer array `[crashTime, memory1Crash, memory2Crash]`, preserving the
first-stick/second-stick order of the two remaining-memory values.

### Examples
**Example 1**

- Input: `memory1 = 2, memory2 = 2`
- Output: `[3,1,0]`

The requests of one and two bits use the first and second sticks respectively;
neither can supply the three-bit request.

**Example 2**

- Input: `memory1 = 8, memory2 = 11`
- Output: `[6,0,4]`

**Example 3**

- Input: `memory1 = 0, memory2 = 0`
- Output: `[1,0,0]`

### Required Complexity
- **Time:** $O(\sqrt{M})$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Maintain the current second and the two remaining capacities. If the larger
capacity is smaller than the current second, then both sticks are too small and
the current state is exactly the required crash state.

Otherwise, compare the capacities. Subtract the current second from the first
stick when it is at least as large as the second stick; this `>=` comparison is
what implements the required first-stick tie rule. If the second stick is
larger, subtract from it instead. Then advance to the next second and repeat.
Each successful iteration reproduces one allocation from the definition, so
the first iteration that cannot run returns the correct crash time and
unchanged remaining capacities.

#### Complexity detail

After $t$ successful seconds, the program has allocated
$1+2+\cdots+t=t(t+1)/2$ bits. This cannot exceed $M$, so
$t=O(\sqrt{M})$. Each simulated second takes constant time, giving
$O(\sqrt{M})$ total time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Closed-form phase calculations:** arithmetic can skip groups of
  allocations, but handling the changing larger stick and the first-stick tie
  rule makes that approach substantially more delicate.
- **Bit-by-bit allocation:** decrementing one bit at a time produces the same
  states but performs $O(M)$ work instead of one update per second.
- If both sticks start at zero, the crash occurs immediately at second one.
- Equal capacities must select the first stick, including equalities reached
  after earlier allocations.
- A stick may become exactly zero after a successful request; the crash is
  reported only at the next request that neither stick can satisfy.

</details>

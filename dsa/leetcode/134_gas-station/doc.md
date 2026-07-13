# Gas Station

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 134 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/gas-station/) |

## Problem Description
### Goal
Stations are arranged in a circle. At station `i`, a car may add `gas[i]` units of fuel, and driving clockwise to the next station consumes `cost[i]` units. The car begins with an empty tank at whichever station you choose and cannot let its fuel balance become negative during the trip.

Return the zero-based starting index that allows one complete clockwise circuit and arrival back at that station. If no starting point can finish the circuit, return `-1`. The input guarantee makes a feasible answer unique, although fuel left over after individual legs may carry forward and compensate for later expensive segments.

### Function Contract
**Inputs**

- `gas`: fuel available at each station
- `cost`: fuel required for each corresponding outgoing edge

**Return value**

The unique valid starting index when a circuit is possible; otherwise `-1`.

### Examples
**Example 1**

- Input: `gas = [1,2,3,4,5], cost = [3,4,5,1,2]`
- Output: `3`

**Example 2**

- Input: `gas = [2,3,4], cost = [3,4,3]`
- Output: `-1`

**Example 3**

- Input: `gas = [5], cost = [4]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Total net fuel decides whether any circuit can exist**

Let `gain[i] = gas[i] - cost[i]`. Completing the circuit consumes and receives every station amount exactly once, regardless of start. If `sum(gain) < 0`, final fuel would be negative from every start, so return `-1`. A nonnegative total is necessary and, together with the reset argument, sufficient.

**One failed candidate eliminates its whole scanned prefix**

Scan gains while maintaining fuel accumulated from `candidate`. If it first becomes negative after station `i`, the candidate fails. Every prefix from candidate through a station before `i` was nonnegative before this first failure. Starting at any such later station discards that nonnegative amount, leaving fuel to `i` no greater than the already-negative total. Thus every start in `[candidate,i]` fails.

Set the next candidate to $i + 1$ and reset the local tank to zero. Keep a separate global total so discarded deficits still participate in final feasibility.

**Candidate and total track different questions**

The current candidate can traverse every processed edge since its last reset without negative fuel, and every earlier index has been eliminated. The local tank measures feasibility from that candidate; the total gain measures feasibility of the complete circle.

**Trace an initial deficit block and wraparound surplus**

Starting candidates `0`, `1`, and `2` fail within the initial deficit region. Resetting selects station `3`; its surplus carries the car through stations `4`, `0`, `1`, and `2`.

**One deficit eliminates an entire candidate interval**

Suppose a candidate first reaches negative tank at station `i`. Before that failure, every prefix from the candidate had nonnegative balance. Starting at any intermediate station discards such a nonnegative prefix, leaving no more fuel for the remaining trip to `i`, so every start in that interval also fails.

Resetting to $i + 1$ therefore skips only impossible candidates. If the total circuit balance is negative, no start can succeed. Otherwise the final noneliminated candidate's forward segment plus the global surplus covers the wraparound segment, so it completes the circuit.

#### Complexity detail

Each of `n` stations is processed once, giving $O(n)$ time. Total, tank, and candidate are scalar state, so space is $O(1)$.

#### Alternatives and edge cases

- **Simulate from every station:** can take $O(n^2)$ time.
- **Choose the station with most gas:** ignores outgoing costs and accumulated deficits.
- **Track every prefix in an array:** works but uses unnecessary $O(n)$ storage.
- A single station succeeds exactly when its gas covers its outgoing cost. Zero total gain may still have a valid candidate.
- The platform guarantees uniqueness when a solution exists; the greedy proof finds the final noneliminated valid start.

</details>

# Minimum Operations to Convert Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2059 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-convert-number/) |

## Problem Description

### Goal

An integer `x` begins at `start`. While its current value lies from $0$ through $1000$, choose any distinct operand from `nums` and replace `x` with `x + operand`, `x - operand`, or `x ^ operand`, where `^` is bitwise XOR. Operands may be reused in any order and any number of times.

An operation may produce a value outside the allowed range, and that operation can successfully reach `goal`; however, no later operation may be applied from an out-of-range result. Return the fewest operations needed to reach `goal`, or `-1` if no legal sequence does so.

### Function Contract

**Inputs**

- `nums`: an array of $m$ distinct integers, where $1 \le m \le 1000$ and each value lies from $-10^9$ through $10^9$.
- `start`: the initial value, satisfying $0 \le start \le 1000$.
- `goal`: a target from $-10^9$ through $10^9$, distinct from `start`.

Let $R$ be the number of reachable values in the expandable range $[0,1000]$, so $R\le1001$.

**Return value**

- Return the minimum number of permitted operations that converts `start` to `goal`, or `-1` if conversion is impossible.

### Examples

**Example 1**

- Input: `nums = [2,4,12], start = 2, goal = 12`
- Output: `2`
- Explanation: One shortest sequence is `2 + 12 = 14`, followed by `14 - 2 = 12`.

**Example 2**

- Input: `nums = [3,5,7], start = 0, goal = -4`
- Output: `2`
- Explanation: `0 + 3 = 3`, then `3 - 7 = -4`; the final out-of-range result is allowed.

**Example 3**

- Input: `nums = [2,8,16], start = 0, goal = 1`
- Output: `-1`

### Required Complexity

- **Time:** $O(Rm)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Values form an unweighted state graph**

Treat each expandable integer as a graph vertex. From a value, every operand creates three one-operation neighbors through addition, subtraction, and XOR. Breadth-first search explores this unweighted graph by operation count, so the first generated occurrence of `goal` has minimum distance from `start`.

**Separating success from expandable states**

Check every generated candidate against `goal` before applying the range restriction. This permits a final operation to leave `[0,1000]`. Only an in-range candidate may enter the queue, and a visited set enqueues each such value at most once. Out-of-range non-goal values are terminal and discarded.

Breadth-first layers contain exactly the values reachable in successive operation counts. Generating all three operations for every operand covers every legal transition, while visited-state suppression removes only longer revisits. Therefore returning upon first reaching `goal` is optimal, and exhausting the queue proves impossibility.

#### Complexity detail

Each of the $R$ reachable expandable values is removed from the queue once and tries three operations for each of the $m$ operands, giving $O(Rm)$ time. The queue and visited set hold at most $R\le1001$ values and use $O(R)$ space.

#### Alternatives and edge cases

- **Depth-first search:** It can establish reachability with cycle detection but does not naturally guarantee the minimum operation count.
- **List-based visited membership:** Keeping visited states in a list is correct but each membership test can cost $O(R)$, increasing the search to $O(R^2m)$.
- **Repeated operand validation:** Rescanning all operands before expanding each one preserves the transitions but adds an unnecessary factor of $m$.
- Test `candidate == goal` before rejecting out-of-range values; otherwise valid final operations are lost.
- XOR with negative operands follows the language's integer bitwise semantics and is still a permitted transition.
- Reusing an operand is allowed, but revisiting the same in-range value cannot improve a BFS distance.

</details>

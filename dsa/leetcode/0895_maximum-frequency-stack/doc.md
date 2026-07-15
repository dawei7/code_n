# Maximum Frequency Stack

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 895 |
| Difficulty | Hard |
| Topics | Hash Table, Stack, Design, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-frequency-stack/) |

## Problem Description
### Goal
Design a stack-like data structure that accepts pushed integers and removes elements according to frequency rather than only by physical top position.

An empty `FreqStack` supports two operations. Calling `push(val)` places `val` onto the stack. Calling `pop()` removes and returns a value whose current occurrence count in the stack is greatest. If several values share that maximum frequency, remove the tied value closest to the stack's top, meaning the one pushed most recently among those candidates.

The input sequence always leaves at least one element available before every `pop()` call.

### Function Contract
Let $q$ be the total number of `push` and `pop` calls in one operation sequence.

**Operations**

- `FreqStack()`: construct an empty frequency stack.
- `push(val)`: add `val` to the top, where $0 \leq \texttt{val} \leq 10^9$.
- `pop()`: remove and return the most frequent current value, breaking frequency ties by proximity to the top.
- At most $2 \cdot 10^4$ operations are issued, and every `pop()` is valid.

**App-local input**

- `operations`: the calls after construction, encoded as `["push", val]` or `["pop"]`.

**Return value**

Return the result trace: `None` for each `push` and the removed integer for each `pop`.

### Examples
**Example 1**

- Input: `operations = [["push",5],["push",7],["push",5],["push",7],["push",4],["push",5],["pop"],["pop"],["pop"],["pop"]]`
- Output: `[null,null,null,null,null,null,5,7,5,4]`

The first `pop()` returns `5` because it occurs three times. The next call sees `5` and `7` tied at frequency two and returns `7`, whose latest remaining occurrence is closer to the top. After another `5` is removed, `4`, `5`, and `7` are tied, so the most recently pushed value `4` is returned.

**Example 2**

- Input: `operations = [["push",9],["pop"]]`
- Output: `[null,9]`

**Example 3**

- Input: `operations = [["push",2],["push",1],["push",2],["push",1],["pop"],["pop"]]`
- Output: `[null,null,null,null,1,2]`

### Required Complexity
- **Time:** $O(1)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Index values by their current frequency**

Maintain `frequency[val]`, the number of live occurrences of each value. A push increments that count. A pop decrements the count of the value it removes.

**Give every frequency its own recency stack**

Maintain `groups[f]` as a stack of values in the order they attained frequency $f$. When pushing `val` raises its count to `f`, append it to `groups[f]`. Also track `max_frequency`, the largest current frequency.

The top of `groups[max_frequency]` is exactly the required answer. Every value in that group reached the maximum frequency, and stack order records which such attainment happened most recently. Therefore popping the group's top enforces both priorities: maximum frequency first and proximity to the original stack's top second.

After removing that value, decrement its current frequency. If the maximum-frequency group becomes empty, no value still has that count, so decrement `max_frequency`. Frequencies change by only one per operation; consequently the next maximum cannot skip an additional level.

The data structure starts with correct empty maps and maximum zero. Each push records the new frequency and its recency in the matching group. Each pop selects the latest value in the highest nonempty group, which is precisely the stated tie rule, then restores the same representation for the remaining elements. Thus every returned value is the required one.

#### Complexity detail

Dictionary access and stack append or pop take expected amortized $O(1)$ time, so each `push` and `pop` meets the $O(1)$ bound. Across $q$ calls, the frequency map and all live group entries occupy $O(q)$ space.

#### Alternatives and edge cases

- **Heap of frequency and timestamp entries:** A max-heap can encode both priorities, but every operation costs $O(\log q)$ and stale entries require careful handling.
- **Ordered set per value frequency:** Explicitly ordering candidates by frequency and recency also works, but updates are $O(\log q)$ instead of constant expected time.
- **Scan the physical stack on every pop:** Recounting values and searching backward is direct and correct, but one pop can take $O(q)$ time and a long trace becomes quadratic.
- **Frequency tie:** The top of the maximum-frequency group chooses the most recently pushed tied value; numeric value does not affect the decision.
- **Repeated value:** Every push appends another frequency milestone, so consecutive pops can correctly return the same value several times.
- **Zero and large values:** Values are dictionary keys, so the full allowed range from `0` through $10^9$ needs no special indexing.
- **Valid pop guarantee:** No empty-stack branch is needed because every `pop()` is issued while at least one element remains.

</details>

### 1. Description

Given the availability time slots arrays `slots1` and `slots2` of two people and a meeting duration `duration`, return the **earliest time slot** that works for both of them and is of duration `duration`.

If there is no common time slot that satisfies the requirements, return an **empty array**.

The format of a time slot is an array of two elements `[start, end]` representing an inclusive time range from `start` to `end`.

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots `[start1, end1]` and `[start2, end2]` of the same person, either `start1 > end2` or `start2 > end1`.

### 2. Function Contract

**Inputs**

- `slots1`: The first person's availability slots.
- `slots2`: The second person's availability slots.
- `duration`: The required meeting length.

Let $n = \lvert\texttt{slots1}\rvert$ and $m = \lvert\texttt{slots2}\rvert$. Every slot contains exactly two integer endpoints `[start, end]` with `start < end`. Slots belonging to the same person are pairwise nonintersecting, but neither input list is guaranteed to arrive in chronological order.

The source describes slot endpoints as inclusive. Meeting length follows elapsed-time semantics: a meeting that begins at `start` and lasts `duration` is returned as `[start, start + duration]`.

**Return value**

Return `[start, start + duration]` for the feasible meeting with the earliest `start`. Return `[]` if no pair of slots shares at least `duration` time units.

### 3. Examples

#### Example 1

- **Input:** $slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8$
- **Output:** `[60,68]`
#### Example 2

- **Input:** $slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12$
- **Output:** `[]`

### 4. Constraints

- $1 \le \text{slots1.length}, \text{slots2.length} \le 10^{4}$

- $\text{slots1}[i].length, \text{slots2}[i].length = 2$

- $\text{slots1}[i][0] < \text{slots1}[i][1]$

- $\text{slots2}[i][0] < \text{slots2}[i][1]$

- $0 \le \text{slots1}[i][j], \text{slots2}[i][j] \le 10^{9}$

- $1 \le duration \le 10^{6}$
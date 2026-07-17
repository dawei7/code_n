# Number of Students Unable to Eat Lunch

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1700 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Stack, Queue, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) |

## Problem Description
### Goal

A cafeteria has a queue of students and a stack of sandwiches. Every student prefers exactly one shape: `0` denotes circular and `1` denotes square. The first entry of `sandwiches` is the top of the stack, and the entries of `students` give the queue order from front to back.

The student at the front takes the top sandwich and leaves when its type matches that student's preference. Otherwise, the student declines it and moves to the back of the queue. This process continues until everyone has eaten or an entire remaining queue refuses the current top sandwich. Return how many students are still waiting when service stops.

### Function Contract
**Inputs**

- `students`: a list of $n$ preferences, each equal to `0` or `1`, in front-to-back queue order
- `sandwiches`: a list of $n$ sandwich types, each equal to `0` or `1`, in top-to-bottom stack order
- The common length satisfies $1 \le n \le 100$.

**Return value**

The number of students who cannot receive a sandwich before the process becomes stuck.

### Examples
**Example 1**

- Input: `students = [1, 1, 0, 0], sandwiches = [0, 1, 0, 1]`
- Output: `0`

Students rotate whenever necessary, and all four sandwich types can eventually be matched.

**Example 2**

- Input: `students = [1, 1, 1, 0, 0, 1], sandwiches = [1, 0, 0, 0, 1, 1]`
- Output: `3`

After three sandwiches are taken, the top sandwich is circular but every remaining student prefers a square one.

**Example 3**

- Input: `students = [0, 0, 1], sandwiches = [1, 0, 0]`
- Output: `0`

The square-preferring student can rotate to the front, after which the two circular sandwiches are taken.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Replace queue order with preference counts**

Count how many waiting students prefer each of the two sandwich types. The exact queue order does not affect whether the current top sandwich can be taken. If at least one waiting student wants that type, every student before that person can rotate to the back, so the matching student eventually reaches the front and takes it. Those rotations change positions but not either preference count.

Process `sandwiches` from top to bottom. When the current type still has a positive count, decrement that count to represent one matching student leaving. This produces the same number of successful servings as the explicit queue process without performing any rotations.

**Detect the first impossible sandwich**

If the count for the current top type is zero, no waiting student wants it. A full pass through the queue would therefore move every student to the back without changing the queue or sandwich stack, so service can never progress. The number of unprocessed sandwiches equals the number of students still waiting and is the required answer.

If every sandwich is processed, every student has eaten and the answer is zero. Thus the scan stops at exactly the same point as the stated simulation.

#### Complexity detail

Counting the $n$ preferences and scanning at most $n$ sandwiches takes $O(n)$ time. The two counters occupy $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Literal queue simulation:** rotating a deque follows the rules directly, but alternating demands can cause $O(n^2)$ total queue operations.
- **Consecutive-refusal counter:** simulation may stop after as many consecutive refusals as there are waiting students; it is correct but retains the slower rotation work.
- **Compare total multisets only:** equal totals imply everyone eats, but unequal totals alone do not reveal where the fixed sandwich order first blocks progress.
- **Immediate mismatch:** if nobody wants the first sandwich, all $n$ students remain.
- **Partial service:** a preference count may become zero only after several sandwiches have been consumed; the answer is then the entire unprocessed suffix length.
- **Single student:** the result is zero for a match and one for a mismatch.
- **Top-of-stack convention:** `sandwiches[0]`, not the final list element, is served first.

</details>

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

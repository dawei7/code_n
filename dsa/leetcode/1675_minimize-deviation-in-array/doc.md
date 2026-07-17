# Minimize Deviation in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1675 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-deviation-in-array/) |

## Problem Description
### Goal
The deviation of an array is the difference between its maximum and minimum values. Starting from an array of positive integers, operations may be applied to any element any number of times: an even value may be divided by two, while an odd value may be multiplied by two.

Choose any legal sequence of these operations and return the smallest deviation that can be achieved. Each element evolves independently, but the objective depends on the common range containing one reachable value from every element.

### Function Contract
**Inputs**

- `nums`: an array of $n$ positive integers.

Let $M=\max(\texttt{nums})$.

**Return value**

Return the minimum possible difference between the largest and smallest array values after any number of legal operations.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `1`

**Example 2**

- Input: `nums = [4,1,5,20,3]`
- Output: `3`

**Example 3**

- Input: `nums = [2,10,8]`
- Output: `3`

### Required Complexity
- **Time:** $O(n\log M\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn every value into a descending chain.** An odd value can only be doubled once before becoming even; halving that result returns to the original odd value. Normalize each odd input to twice itself and leave each even input unchanged. From this largest useful representative, every distinct reachable smaller value is obtained by repeatedly halving while the current value is even.

**Start from all maximum representatives.** Insert the normalized values into a max-heap and track their current minimum. This configuration chooses the top of every element's descending chain. Its range is one candidate answer.

**Reduce the only value that can improve the range.** Pop the current maximum. Any better range with a smaller upper endpoint must lower some occurrence of that maximum, so if it is even, replace it with half its value, update the current minimum, and push it back. Record the range before each reduction.

**Stop at an odd maximum.** Once the current maximum is odd, that selected value is already at the bottom of its chain and cannot be reduced. Increasing another smaller value cannot lower the maximum and cannot recover a range missed earlier, because all higher representatives were examined as the heap descended. No later configuration can improve the recorded answer.

**Why all relevant configurations are covered.** Each element contributes a finite descending chain. Starting at every chain's maximum and repeatedly advancing whichever chain owns the global maximum is the standard smallest-range traversal across sorted lists: a range can shrink only by moving its maximum endpoint downward. The heap visits each such necessary transition, so the minimum recorded range is globally optimal.

#### Complexity detail

Each element can be halved at most $O(\log M)$ times, giving at most $O(n\log M)$ heap updates. Every update costs $O(\log n)$, for $O(n\log M\log n)$ time. The heap stores exactly $n$ current representatives and uses $O(n)$ space.

#### Alternatives and edge cases

- **Linear maximum search:** Store current values in an array and rescan it before every halving. This is correct but can require $O(n^2\log M)$ time.
- **Ordered multiset:** A balanced tree can provide both endpoints and replacements in $O(\log n)$ time, matching the heap approach where such a container is available.
- **Enumerate Cartesian products:** Trying every reachable value combination grows exponentially and ignores the ordered-chain structure.
- Equal input values may already achieve deviation zero.
- A power of two can descend through every smaller power of two down to one.
- An odd input has only its original value and its doubled value as distinct reachable choices.
- Duplicate maxima must be reduced one occurrence at a time before the global maximum falls.
- The best range may occur before the final odd maximum is reached, so update the answer at every heap state.

</details>

# Generate Binary Numbers 1 to N

| | |
|---|---|
| **ID** | `queue_03` |
| **Category** | queue |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 2/10 |
| **Interview relevance** | 4/10 |
| **LeetCode Equivalent** | N/A (Fundamental Exercise) |

## Problem statement

Given an integer `N`, generate and return an array of strings representing the binary equivalents of all numbers from `1` to `N` sequentially.
Do not use built-in base-conversion functions (like Python's `bin()` or C++'s `itoa()`). Generate them using the structural properties of queues.

**Input:** An integer `N`.
**Output:** A list of strings.

**Example:**
`N = 5`
Output: `["1", "10", "11", "100", "101"]`.

## When to use it

- To understand how Queues naturally model **Level-Order Traversal** (BFS). Generating binary numbers is identical to traversing a perfectly balanced binary tree.

## Approach

Think of binary numbers as a tree:
- The root is `"1"`.
- Every node has a left child (append `"0"`) and a right child (append `"1"`).
- Root `"1"` -> Left child `"10"`, Right child `"11"`.
- `"10"` -> Left child `"100"`, Right child `"101"`.
- `"11"` -> Left child `"110"`, Right child `"111"`.

This strictly generates binary numbers in numerically increasing order!
Because we want to generate them in order, we can just perform a **Breadth-First Search (BFS)** using a Queue.

1. Create an empty Queue of strings.
2. Enqueue the root `"1"`.
3. Loop `N` times:
   - Dequeue the front string `curr`.
   - Append `curr` to the result array.
   - Enqueue its left child: `curr + "0"`.
   - Enqueue its right child: `curr + "1"`.
4. Return the result array.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for queue_03: Generate Binary Numbers (1 to n).

Generate the binary representations of 1, 2, ..., n
"""


def solve(n):
    """Generate binary strings '1', '10', '11', '100', ... up to n."""
    from collections import deque
    if n <= 0:
        return []
    result = []
    q = deque(["1"])
    for _ in range(n):
        s = q.popleft()
        result.append(s)
        q.append(s + "0")
        q.append(s + "1")
    return result
```

</details>

## Walk-through

`N = 4`

1. Start: `q = ["1"]`, `result = []`.
2. **Loop 1:**
   - Pop `"1"`.
   - `result = ["1"]`.
   - Push `"10"`, `"11"`.
   - `q = ["10", "11"]`.
3. **Loop 2:**
   - Pop `"10"`.
   - `result = ["1", "10"]`.
   - Push `"100"`, `"101"`.
   - `q = ["11", "100", "101"]`.
4. **Loop 3:**
   - Pop `"11"`.
   - `result = ["1", "10", "11"]`.
   - Push `"110"`, `"111"`.
   - `q = ["100", "101", "110", "111"]`.
5. **Loop 4:**
   - Pop `"100"`.
   - `result = ["1", "10", "11", "100"]`.
   - Push `"1000"`, `"1001"`.
   - `q = ["101", "110", "111", "1000", "1001"]`.

Loop terminates.
Output: `["1", "10", "11", "100"]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The loop runs exactly N times. In each iteration, we do constant string concatenation and $O(1)$ queue operations. Time complexity is strictly $O(N)$.
(Technically, string length grows to log N, making strict bit-wise time $O(N \log N)$, but practically bounded to $O(N)$).
Space complexity is $O(N)$ because the queue grows at a rate of 1 element per iteration (2 x \text{Push} - 1 x \text{Pop} = +1), meaning the queue holds N strings at the end.

## Variants & optimizations

- **Base-K Generation:** You can trivially adapt this to generate numbers in Base-3, Base-4, etc., by having a `for i in range(K): q.append(curr + str(i))` loop inside instead of hardcoding "0" and "1".

## Real-world applications

- **Lexicographical State Machines:** Generative algorithms in natural language processing (NLP) or brute-force password cracking utilize queue-based BFS to generate testing combinations strictly ordered by length and lexicography.

## Related algorithms in cOde(n)

- **[tree_05 - Level Order Traversal](../trees/tree_05_level-order-traversal.md)** — The exact same Queue logic applied to an explicitly defined physical tree in memory.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

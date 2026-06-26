# Sliding Window Maximum

| | |
|---|---|
| **ID** | `heap_05` |
| **Category** | heap |
| **Complexity (required)** | $O(N log K)$ using Heap, $O(N)$ using Deque |
| **Difficulty** | 8/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |

## Problem statement

Given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.
Return an array containing the maximum element inside the window at every step.

**Input:** An array of integers `nums`, and an integer `k`.
**Output:** An array of integers representing the max in each window.

## When to use it

- A highly requested interview problem to test if you know how to build a **Monotonic Queue**, which heavily outperforms the naive Priority Queue approach.
- Note: While this is categorized under "Heap", the optimal solution explicitly *avoids* using a heap!

## Approach

**Approach 1: The Lazy Max-Heap ($O(N \log N)$)**
We can maintain a Max-Heap of tuples `(value, index)`.
When the window slides to index `i`:
1. Push `(nums[i], i)` to the Max-Heap.
2. The maximum element is at `heap[0]`. BUT, wait! What if the maximum element is from index `i - k - 1` (it has fallen out of the back of the window)?
3. **Lazy Deletion:** We just `while` loop: if `heap[0].index <= i - k`, we `pop` it! We don't care about outdated elements deep inside the heap, we only care if the *current champion* is outdated.
4. Record `heap[0].value`.

**Approach 2: The Monotonic Deque ($O(N)$ - Optimal!)**
Instead of a Heap, we use a Double-Ended Queue (Deque) to store array *indices*.
We maintain a strict rule: **The values corresponding to the indices in the deque must be strictly monotonically decreasing.**
Why? If a new, giant number `100` enters the window, any smaller numbers `5, 10, 50` that entered the window *before* it are utterly useless! They can never be the maximum again, because `100` is bigger than them AND it will survive in the window longer than them!

1. Loop through `nums` at index `i`.
2. **Remove Outdated:** If the index at the `front` of the deque is \le i - k, it has fallen out of the window. `popleft()` it.
3. **Remove Losers:** While the `back` of the deque has a value \le nums[i], `pop()` it. They are dead weight.
4. **Push New:** `append(i)` to the back of the deque.
5. The maximum of the current window is always instantly available at the `front` of the deque!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for heap_05: Sliding Window Maximum.

For each window of size k, return the max. Use a max-heap keyed
on (-value, index); pop from the top while the index is outside
the current window.
"""


def solve(arr, k, n):
    if k <= 0 or k > n:
        return []
    import heapq
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))
    out = [-heap[0][0]]
    for i in range(k, n):
        heapq.heappush(heap, (-arr[i], i))
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
        out.append(-heap[0][0])
    return out
```

</details>

## Walk-through

`nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`.
`q` stores indices. Let's look at `q_vals` for conceptual clarity.

1. **i=0 (num=1):** `q=[0]`. `q_vals=[1]`.
2. **i=1 (num=3):** Pop `0` (1 <= 3). Push `1`. `q=[1]`. `q_vals=[3]`.
3. **i=2 (num=-1):** Push `2`. `q=[1, 2]`. `q_vals=[3, -1]`.
   - Window size 3 reached! Max is `nums[q[0]] = 3`. `res = [3]`.
4. **i=3 (num=-3):** Push `3`. `q=[1, 2, 3]`. `q_vals=[3, -1, -3]`.
   - Max is `3`. `res = [3, 3]`.
5. **i=4 (num=5):** Outdated check: `q[0]=1 <= 4-3` (1 <= 1). Pop `1`! (The `3` expired).
   - Loser check: Pop `-3`. Pop `-1`. Push `4`. `q=[4]`. `q_vals=[5]`.
   - Max is `5`. `res = [3, 3, 5]`.
6. **i=5 (num=3):** Push `5`. `q=[4, 5]`. `q_vals=[5, 3]`.
   - Max is `5`. `res = [3, 3, 5, 5]`.
7. **i=6 (num=6):** Loser check: Pop `3`. Pop `5`. Push `6`. `q=[6]`. `q_vals=[6]`.
   - Max is `6`. `res = [3, 3, 5, 5, 6]`.
8. **i=7 (num=7):** Loser check: Pop `6`. Push `7`. `q=[7]`. `q_vals=[7]`.
   - Max is `7`. `res = [3, 3, 5, 5, 6, 7]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(K)$ |
| **Average** | $O(N)$ | $O(K)$ |
| **Worst** | $O(N)$ | $O(K)$ |

Wait, there is a `while` loop inside the `for` loop! Doesn't that make it $O(N x K)$?
No! Using Amortized Analysis, observe that every single index in the array is `append`ed to the deque exactly once. It can therefore be `pop`ped from the deque at most exactly once. The code inside the `while` loop runs at most N times across the *entire* execution of the algorithm. Therefore, total time is strictly $O(N)$.
Space complexity is $O(K)$ because the deque will never hold more than K elements.

## Variants & optimizations

- **2D Sliding Window (Max in Matrix Subgrid):** A much harder variant where you must find the maximum in a K x K moving box. This is solved by running the 1D Monotonic Deque algorithm horizontally on every row, storing the results in a new matrix, and then running it vertically on every column of the new matrix!

## Real-world applications

- **Digital Signal Processing:** Calculating the moving maximum/minimum envelope of an audio wave or stock ticker to detect severe spikes within a rolling time frame.

## Related algorithms in cOde(n)

- **[stack_01 - Next Greater Element](../stacks/stack_01_next-greater-element.md)** — The foundation of the Monotonic data structure. The logic for evicting smaller elements is mathematically identical.
- **[heap_04 - Median in Stream](heap_04_median-in-a-stream.md)** — Another rolling window state manager.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

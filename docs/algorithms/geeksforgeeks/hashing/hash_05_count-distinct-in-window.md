# Count Distinct Elements in Every Window

| | |
|---|---|
| **ID** | `hash_05` |
| **Category** | hashing |
| **Complexity (required)** | $O(N)$ Time, $O(K)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **GeeksForGeeks Equivalent** | [Count distinct elements in every window of size K](https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/) |

## Problem statement

Given an array of integers `nums` and an integer `K`. Find the count of distinct elements in every contiguous sliding window of size `K` from left to right.

**Input:** An integer array `nums` of size `N`, and a window size `K`.
**Output:** An array of integers representing the distinct count for each window.

## When to use it

- To combine Hash Maps with the Sliding Window technique.
- When you need to maintain a running frequency tally as elements dynamically enter and exit your active sub-array.

## Approach

**1. The Flaw of Sets:**
If we just wanted the distinct count of a single array, we could throw all elements into a Hash Set and return `len(set)`.
But as the window slides, the element `nums[i - K]` falls out of the window. If we just run `set.remove(nums[i - K])`, we might accidentally delete a number that ALSO exists elsewhere inside the window! We need to know EXACTLY how many copies of that number are currently in the window.

**2. The Frequency Map:**
Instead of a Set, we use a Hash Map (Dictionary) where `Key = Number` and `Value = Frequency`.
The number of distinct elements is simply the number of active Keys in the Hash Map (i.e., `len(map)`).

**3. The Sliding Window:**
1. **Initialize:** Manually add the first `K` elements into the frequency map. Record the `len(map)` as the answer for the first window.
2. **Slide:** Loop from `i = K` to `N-1`.
   - **Add the new element:** `nums[i]` enters the window. Increment its frequency in the map.
   - **Remove the old element:** `nums[i - K]` falls out of the window. Decrement its frequency in the map.
   - **Crucial Cleanup:** If the frequency of `nums[i - K]` hits `0`, it is completely gone from the window! We MUST `del map[nums[i - K]]` to completely erase the key, so that `len(map)` correctly reflects the distinct count!
3. Append `len(map)` to the results array.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for hash_05: Count Distinct Elements in Window.

For each window of size k, return the number of distinct
elements. Sliding window + count map: O(n) total.
"""


def solve(arr, k, n):
    if k <= 0 or k > n:
        return []
    counts = {}
    out = []
    for i in range(k):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
    out.append(len(counts))
    for i in range(k, n):
        counts[arr[i]] = counts.get(arr[i], 0) + 1
        old = arr[i - k]
        counts[old] -= 1
        if counts[old] == 0:
            del counts[old]
        out.append(len(counts))
    return out
```

</details>

## Walk-through

`nums = [1, 2, 1, 3, 4, 2, 3]`, `K = 4`.

1. **Initialize first window (indices 0 to 3):** `[1, 2, 1, 3]`.
   - `freq_map = {1: 2, 2: 1, 3: 1}`.
   - `len(map) = 3`. `results = [3]`.
2. **Slide to i=4 (incoming 4, outgoing 1):**
   - Add `4`: `freq_map = {1: 2, 2: 1, 3: 1, 4: 1}`.
   - Remove `nums[4-4] = nums[0] = 1`. `freq_map[1]` goes from 2 to 1.
   - `freq_map = {1: 1, 2: 1, 3: 1, 4: 1}`.
   - `len(map) = 4`. `results = [3, 4]`.
3. **Slide to i=5 (incoming 2, outgoing 2):**
   - Add `2`: `freq_map[2]` becomes 2.
   - Remove `nums[5-4] = nums[1] = 2`. `freq_map[2]` drops back to 1.
   - `freq_map = {1: 1, 2: 1, 3: 1, 4: 1}`.
   - `len(map) = 4`. `results = [3, 4, 4]`.
4. **Slide to i=6 (incoming 3, outgoing 1):**
   - Add `3`: `freq_map[3]` becomes 2.
   - Remove `nums[6-4] = nums[2] = 1`. `freq_map[1]` drops to 0!
   - `del freq_map[1]`!
   - `freq_map = {2: 1, 3: 2, 4: 1}`.
   - `len(map) = 3`. `results = [3, 4, 4, 3]`.

Result: `[3, 4, 4, 3]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(K)$ |
| **Average** | $O(N)$ | $O(K)$ |
| **Worst** | $O(N)$ | $O(K)$ |

We iterate through the array of length N exactly once. At each step, inserting into the dictionary, decrementing, and deleting keys all take amortized $O(1)$ time. Total time complexity is strictly $O(N)$.
Space complexity is $O(K)$ because the dictionary will at most contain K distinct keys (the maximum size of the sliding window).

## Variants & optimizations

- **Sliding Window Maximum (`two_pointers_05`):** If you are asked to find the *Maximum Element* in every window of size K instead of the *Distinct Count*, a Hash Map fails because finding the `max()` of the keys takes $O(K)$ time per window! You must use a Monotonic Deque.

## Real-world applications

- **Network Traffic Monitoring:** Detecting DDoS attacks by maintaining a rolling window of the last 10,000 incoming IP addresses. If the "distinct count" drops suddenly while packet volume remains high, a single IP is flooding the server.

## Related algorithms in cOde(n)

- **[hash_03 - Longest Substring Without Repeating](hash_03_longest-substring-without-repeating.md)** — Another algorithm combining Hash Maps with Sliding Windows, but with a dynamically resizing window instead of a fixed size `K`.
- **[two_pointers_05 - Sliding Window Maximum](../two_pointers/two_pointers_05_sliding-window-maximum.md)** — The Deque-based variant for tracking extremal values in a fixed window.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

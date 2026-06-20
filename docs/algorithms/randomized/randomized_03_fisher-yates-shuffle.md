# Fisher-Yates Shuffle

| | |
|---|---|
| **ID** | `randomized_03` |
| **Category** | randomized |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) |

## Problem statement

Given an array of N elements, shuffle the array such that all permutations of the array are equally likely to occur.
You must do this in $O(N)$ time and $O(1)$ auxiliary space (in-place).

**Input:** An array `nums`.
**Output:** The same array, randomly shuffled.

## When to use it

- To randomize data perfectly and efficiently. This is the gold standard algorithm for shuffling arrays (used under the hood in `random.shuffle()` in Python and `std::shuffle` in C++).

## Approach

A naive shuffle might assign a random number to every element and sort by that number ($O(N \log N)$), or repeatedly pick random indices and swap them ($O(N^2)$ and mathematically biased).

The **Fisher-Yates Shuffle** (specifically the modern Durstenfeld variant) is elegant, $O(N)$, and mathematically perfect.

The core idea is similar to drawing cards from a deck:
1. You have a "deck" of N unpicked cards (the array indices from 0 to N-1).
2. Pick a random card from the unpicked pile.
3. Move it to the "picked" pile at the very end of the array.
4. To do this in-place, we just swap the randomly picked card with the card currently sitting at the end of the unpicked pile!
5. Shrink the size of the unpicked pile by 1.
6. Repeat until 1 card is left.

**Detailed Steps:**
Iterate `i` backwards from N-1 down to 1.
In each step:
- Generate a random index `j` such that 0 \le j \le i. (Note: `j` can equal `i`, meaning the element stays in place, which is crucial for uniform probability).
- Swap `arr[i]` and `arr[j]`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for randomized_03: Fisher-Yates Shuffle.

Given an array of n elements, return a uniformly
"""


def solve(arr, n):
    """Fisher-Yates shuffle. Returns a new list."""
    import random
    work = list(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        work[i], work[j] = work[j], work[i]
    return work
```

</details>

## Walk-through

`nums = [A, B, C, D]`

1. `i = 3` (Element D).
   - Roll random `j` between 0 and 3. Let's say `j = 1` (Element B).
   - Swap `nums[3]` and `nums[1]`.
   - `nums = [A, D, C, B]`. (`B` is now locked in its final position).
2. `i = 2` (Element C).
   - Roll random `j` between 0 and 2. Let's say `j = 2` (Element C).
   - Swap `nums[2]` and `nums[2]`. (Stays in place!).
   - `nums = [A, D, C, B]`. (`C` is now locked).
3. `i = 1` (Element D).
   - Roll random `j` between 0 and 1. Let's say `j = 0` (Element A).
   - Swap `nums[1]` and `nums[0]`.
   - `nums = [D, A, C, B]`. (`A` is locked).

Loop ends. The remaining element `D` at index 0 is trivially locked.
Final shuffled array: `[D, A, C, B]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The loop runs exactly N-1 times. The random number generation and swapping take $O(1)$ time. Time complexity is strictly $O(N)$.
All shuffling is done entirely in-place. Space complexity is $O(1)$.

## Variants & optimizations

- **Forward Iteration:** You can equivalently iterate `i` from 0 to N-2, picking random `j` between `i` and N-1. The math works exactly the same, creating a "locked" partition growing from the left instead of the right.

## Real-world applications

- **Cryptography:** Used in the RC4 stream cipher to initialize the permutation matrix (Key Scheduling Algorithm) uniformly.
- **Gaming:** Shuffling playlists in Spotify, or shuffling decks of cards in online poker to guarantee fairness.

## Related algorithms in cOde(n)

- **[randomized_02 - Reservoir Sampling](randomized_02_reservoir-sampling.md)** — A related concept for selecting a subset rather than shuffling the entire set.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

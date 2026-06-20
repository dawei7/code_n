# Reservoir Sampling

| | |
|---|---|
| **ID** | `randomized_02` |
| **Category** | randomized |
| **Complexity (required)** | $O(N)$ Time, $O(K)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Linked List Random Node](https://leetcode.com/problems/linked-list-random-node/) |

## Problem statement

Given an incoming stream of items of unknown size N (where N can be too large to fit in memory), sample K items uniformly at random from the stream.
By "uniformly at random", we mean that at the end of the stream, every single item that was processed must have exactly a \frac{K}{N} probability of being in the final sample.
You are only allowed one pass over the data, and you can only store K items in memory.

**Input:** A stream of data items and an integer K.
**Output:** An array of size K containing the randomly selected items.

## When to use it

- You need to select random elements from a dataset that is either streaming live or too massive to count beforehand (like a 10TB log file or a live Twitter feed).

## Approach

If we knew N in advance, we could just generate K random indices between 0 and N-1 and pick those. But we don't know N. The stream just keeps coming.

**The Algorithm (Algorithm R):**
1. Maintain an array called `reservoir` of size K.
2. As the first K items arrive from the stream, just put them directly into the reservoir.
3. For the i-th item arriving from the stream (where i > K):
   - Pick a random integer `j` between 1 and i (inclusive).
   - If `j <= K` (which happens with probability \frac{K}{i}):
     - Replace `reservoir[j]` with the new i-th item!
   - Otherwise, throw the i-th item away.

**Why does this work? (The Math)**
For a specific item (say, the very first item), what is the probability it survives to the end of a stream of size N?
It enters the reservoir with probability 1.
When the (K+1)-th item arrives, it replaces an existing item with probability \frac{K}{K+1}. The chance it replaces *our specific item* is \frac{1}{K+1}. So the chance our item survives is 1 - \frac{1}{K+1} = \frac{K}{K+1}.
When the (K+2)-th item arrives, the chance our item survives is \frac{K+1}{K+2}.
...
When the N-th item arrives, the chance our item survives is \frac{N-1}{N}.
Total Probability of survival = 1 x \frac{K}{K+1} x \frac{K+1}{K+2} x \dots x \frac{N-1}{N}.
All the intermediate terms cancel out perfectly, leaving exactly \frac{K}{N}!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for randomized_02: Reservoir Sampling.

Pick k items uniformly at random from a stream of unknown
length. Standard algorithm: fill the reservoir with the first
k items; for each subsequent item i (i >= k), replace a
random reservoir index with probability k / (i + 1).
"""


def solve(stream, k, n):
    import random
    if k <= 0 or n == 0:
        return []
    reservoir = list(stream[:k])
    for i in range(k, n):
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = stream[i]
    return reservoir
```

</details>

## Walk-through

`stream = [A, B, C, D]`, `k = 2`.

1. `i=0, item=A`: `i < 2`. `reservoir = [A]`.
2. `i=1, item=B`: `i < 2`. `reservoir = [A, B]`.
3. `i=2, item=C`: `i = 2`.
   - `random.randint(0, 2)` rolls `0`.
   - `0 < 2` is True. `reservoir[0] = C`.
   - `reservoir = [C, B]`.
   *(Probability C was picked: 2/3. Probability A survived: 1 * 1/2 = 1/2... wait, my math above was for 1-indexing. In 0-indexing, replacing `A` specifically is 1/3, surviving is 2/3. Math holds!)*
4. `i=3, item=D`: `i = 3`.
   - `random.randint(0, 3)` rolls `3`.
   - `3 < 2` is False. D is ignored.
   - `reservoir = [C, B]`.

Final sample: `[C, B]`. Every element had exactly a 2/4 = 50% chance of ending up in the reservoir. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(K)$ |
| **Average** | $O(N)$ | $O(K)$ |
| **Worst** | $O(N)$ | $O(K)$ |

We process every element in the stream exactly once. Doing $O(1)$ random generation and array insertion. Time complexity is strictly $O(N)$.
We only store the final K elements in memory. Space complexity is $O(K)$.

## Variants & optimizations

- **Algorithm L:** Generating a random number for *every* element in a massive stream can be computationally expensive. Algorithm L optimizes this by mathematically computing the "jump distance" (how many elements to skip before accepting the next one) using inverse cumulative distribution functions. This reduces the number of `random()` calls from $O(N)$ to $O(K log(N/K)$)!

## Real-world applications

- **A/B Testing Telemetry:** Picking a uniformly random sample of 10,000 user sessions out of a firehose stream of billions of sessions to analyze crash logs without overloading the metrics servers.

## Related algorithms in cOde(n)

- **[randomized_03 - Fisher-Yates Shuffle](randomized_03_fisher-yates-shuffle.md)** — Uses very similar probabilistic logic but shuffles an entire array in-memory rather than sampling from a stream.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

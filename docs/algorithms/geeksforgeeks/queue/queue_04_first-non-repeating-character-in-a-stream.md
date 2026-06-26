# First Non-repeating Character in a Stream

| | |
|---|---|
| **ID** | `queue_04` |
| **Category** | queue |
| **Complexity (required)** | $O(1)$ Amortized per character |
| **Difficulty** | 5/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) (Stream variation) |

## Problem statement

Given an incoming stream of characters, find the **first non-repeating character** in the stream at any given point in time.
As new characters arrive, the previous "first non-repeating character" might repeat, meaning it becomes invalid, and you must instantly output the *next* oldest non-repeating character.

**Input:** A string `s` representing the data stream.
**Output:** A string of the same length, where the i-th character is the first non-repeating character seen from index `0` to `i`. If all characters seen so far repeat, output `#`.

**Example:**
Stream: `"a a b c"`
1. `"a"`: First unique is `a`. Output: `a`
2. `"a"`: `a` repeated! All characters repeat. Output: `#`
3. `"b"`: `b` is new and unique. Output: `b`
4. `"c"`: `c` is new, but `b` is older and still unique. Output: `b`
Final Output string: `"a#bb"`.

## When to use it

- Solving real-time stream processing problems where historical chronological order matters.
- A classic interview problem teaching the dual usage of Hash Maps (for state) and Queues (for chronology).

## Approach

We need to track two things simultaneously:
1. **Chronology:** Which valid character arrived *first*? A **Queue** is perfect for this.
2. **Frequency:** Has this character arrived before? A **Hash Map (or Array)** is perfect for this.

**The Logic:**
For every incoming character `char`:
1. Increment its count in the Hash Map.
2. If the count is exactly `1` (it's completely new), enqueue it to the back of the Queue.
3. Now, we must check the character currently sitting at the **front** of the Queue (the oldest candidate).
   - Look up the front character's count in the Hash Map.
   - If its count is `> 1`, it means it has repeated since it was originally enqueued! It is "dead". Dequeue it and throw it away.
   - Repeat this `while` loop until the Queue is empty OR the front character has a count of exactly `1`.
4. If the Queue is empty, output `#`. Otherwise, output the character at the front of the Queue.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for queue_04: First Non-Repeating Character in a Stream.

Given a stream of characters (a string), for each
"""


def solve(stream, n):
    """First non-repeating char in each prefix of stream."""
    from collections import deque, Counter
    if n == 0:
        return ""
    q = deque()
    freq = Counter()
    result = []
    for ch in stream:
        freq[ch] += 1
        q.append(ch)
        # Pop from the front of the queue while the head has
        # appeared more than once.
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append("_")
    return "".join(result)
```

</details>

## Walk-through

`stream = "aabc"`

1. **`char = 'a'`**:
   - `freq['a'] = 1`.
   - Queue push `'a'`. `q = ['a']`.
   - `q[0]` is `'a'`. `freq['a'] == 1`. Loop ignores.
   - Result: `a`.
2. **`char = 'a'`**:
   - `freq['a'] = 2`.
   - `q[0]` is `'a'`. `freq['a'] > 1`! Pop it! `q = []`.
   - Queue is empty.
   - Result: `#`.
3. **`char = 'b'`**:
   - `freq['b'] = 1`.
   - Queue push `'b'`. `q = ['b']`.
   - `q[0]` is `'b'`. `freq['b'] == 1`. Loop ignores.
   - Result: `b`.
4. **`char = 'c'`**:
   - `freq['c'] = 1`.
   - Queue push `'c'`. `q = ['b', 'c']`.
   - `q[0]` is `'b'`. `freq['b'] == 1`. Loop ignores.
   - Result: `b`.

Output: `"a#bb"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ amortized | $O(1)$ / $O(U)$ |
| **Average** | $O(1)$ amortized | $O(1)$ / $O(U)$ |
| **Worst** | $O(1)$ amortized | $O(1)$ / $O(U)$ |

Updating the hash map takes $O(1)$. Pushing to the queue takes $O(1)$.
Although there is a `while` loop, any given character is pushed into the queue at most *once* and popped at most *once* over the entire lifetime of the stream. Thus, the inner while loop evaluates to $O(1)$ amortized time.
Space complexity: Since there are only 26 lowercase English letters (or 256 ASCII characters), the queue and hash map will never exceed $O(U)$ where U is the size of the unique alphabet. Therefore, strictly $O(1)$ auxiliary space regardless of how massive the stream N gets!

## Variants & optimizations

- **Doubly Linked List + Hash Map (LRU Cache variant):** If you absolutely need strict $O(1)$ worst-case time per character (no amortized loops), you can use a Doubly Linked List. The Hash Map stores direct pointers to the DLL Nodes. When a character repeats, you instantly `O(1)` delete its Node from the middle of the DLL. The head of the DLL is always the answer.

## Real-world applications

- **Network Routing:** Real-time deduplication of network packets to identify the first unique sequence ID that was dropped and requires retransmission.

## Related algorithms in cOde(n)

- **[linked_list_06 - LRU Cache](../linked_list/ll_06_lru-cache.md)** — The advanced structural variant of this problem using DLLs.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

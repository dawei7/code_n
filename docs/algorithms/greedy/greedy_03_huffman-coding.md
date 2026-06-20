# Huffman Coding

| | |
|---|---|
| **ID** | `greedy_03` |
| **Category** | greedy |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) |

## Problem statement

Given an array of unique characters and their corresponding frequencies in a text file. Construct a Huffman Tree to generate a variable-length binary code for each character.
The goal is to minimize the total number of bits required to compress the text file.

**Input:** Two arrays `chars[]` and `freq[]`.
**Output:** A dictionary mapping each character to its optimal binary string (e.g., `{'a': '0', 'b': '10', 'c': '11'}`).

## When to use it

- To solve the optimal prefix-free binary encoding problem.
- To demonstrate how Priority Queues (Min-Heaps) can be used to construct binary trees from the bottom up.

## Approach

**1. The Prefix-Free Rule:**
If 'a' is encoded as `0`, no other character's code can START with `0` (like `01` or `011`). If they did, a decoder seeing a `0` wouldn't know whether to stop at 'a' or keep reading!
A Binary Tree naturally guarantees this! If we place characters ONLY at the leaf nodes, the path from the root to any leaf (left=0, right=1) is guaranteed to be prefix-free.

**2. The Greedy Insight:**
Characters that appear very frequently (like 'e' or 'a') should have very SHORT codes (shallow in the tree). Characters that appear rarely (like 'z' or 'q') should have LONG codes (deep in the tree).
Therefore, we should greedily take the two characters with the ABSOLUTE LOWEST frequencies, and push them as deep into the tree as possible by making them siblings!

**3. The Algorithm (Bottom-Up Tree Building):**
1. Create a leaf node for every character, storing its frequency. Push all leaf nodes into a **Min-Heap** (Priority Queue) sorted by frequency.
2. While there is more than 1 node in the Min-Heap:
   - Pop the two nodes with the lowest frequencies (let's call them `left` and `right`).
   - Create a new "internal" parent node. Its frequency is `left.freq + right.freq`.
   - Attach `left` and `right` as its children.
   - Push this new parent node back into the Min-Heap!
3. Eventually, only 1 node remains in the Min-Heap. This is the Root of the entire Huffman Tree!

**4. Code Generation:**
Run a simple DFS from the Root. When you go left, append a '0'. When you go right, append a '1'. When you hit a leaf node, save the accumulated string to your dictionary for that character.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_03: Huffman Coding.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(chars, freq, n):
    import heapq
    if n == 0:
        return 0
    if n == 1:
        return freq[0]
    heap = [[f, 0, ""] for f in freq]
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = [a[0] + b[0], 0, ""]
        total += merged[0]
        heapq.heappush(heap, merged)
    return total
```

</details>

## Walk-through

Characters: `a:5`, `b:9`, `c:12`, `d:13`, `e:16`, `f:45`.
`pq = [a:5, b:9, c:12, d:13, e:16, f:45]` (Sorted).

1. Pop `a:5`, `b:9`. Merge into `1:14`.
   `pq = [c:12, d:13, 1:14, e:16, f:45]`.
2. Pop `c:12`, `d:13`. Merge into `2:25`.
   `pq = [1:14, e:16, 2:25, f:45]`.
3. Pop `1:14`, `e:16`. Merge into `3:30`.
   `pq = [2:25, 3:30, f:45]`.
4. Pop `2:25`, `3:30`. Merge into `4:55`.
   `pq = [f:45, 4:55]`.
5. Pop `f:45`, `4:55`. Merge into `5:100`.
   `pq = [5:100]`.
6. Only 1 node left! It's the root.

**DFS from `5:100`:**
- Left to `f:45` -> Code **"0"**.
- Right to `4:55` \implies Code "1".
  - Left to `2:25` -> Code "10".
    - Left to `c:12` -> Code **"100"**.
    - Right to `d:13` -> Code **"101"**.
  - Right to `3:30` \implies Code "11".
    - Left to `1:14` -> Code "110".
      - Left to `a:5` -> Code **"1100"**.
      - Right to `b:9` -> Code **"1101"**.
    - Right to `e:16` -> Code **"111"**.

Notice how `f` (highest freq 45) gets 1 bit, while `a` (lowest freq 5) gets 4 bits! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

Building the initial Min-Heap takes $O(N)$.
We pop two nodes and push one node N-1 times. Priority Queue operations take $O(\log N)$. Thus, the while loop takes $O(N \log N)$ time.
The DFS takes $O(N)$ time to visit the 2N-1 total nodes in the tree.
Total time complexity is dominated by the Priority Queue: $O(N \log N)$.
Space complexity is $O(N)$ to store the Nodes in the Heap, the Nodes in the Tree, and the output dictionary.

## Variants & optimizations

- **Two Queue Optimization:** If the initial input arrays are ALREADY strictly sorted by frequency, you can achieve $O(N)$ time! Instead of a Min-Heap, use two standard FIFO queues. Queue 1 holds the initial sorted leaves. Queue 2 holds the newly generated internal nodes. At each step, just compare the front of Queue 1 and Queue 2 to find the absolute minimum.

## Real-world applications

- **Data Compression:** Huffman Coding is the fundamental entropy-encoding engine inside the massive DEFLATE algorithm, which powers ZIP files, GZIP, and PNG images! It is literally used billions of times a second across the internet.

## Related algorithms in cOde(n)

- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — Another algorithm where sorting heavily dictates a greedy choice.
- **[graph_10 - Prim's MST](../graphs/graph_10_prim-s-mst.md)** — Another application that heavily relies on popping from a Priority Queue to build a Tree.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*

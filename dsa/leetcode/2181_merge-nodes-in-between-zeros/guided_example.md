# Guided Example: Merge Nodes in Between Zeros

We trace the single-pass sentinel accumulator algorithm on a representative zero-delimited linked list instance, demonstrating how partitioning linked nodes into zero-bounded intervals collapses consecutive positive values into merged sum nodes in $O(n)$ time.

- **Input:** `head = [0, 3, 1, 0, 4, 5, 2, 0]`
- **Output:** `[4, 11]`

This instance illustrates zero-delimiter boundary detection, running prefix-sum accumulation, dummy sentinel chaining, and tail pointer progression.

---

## 1. Problem Overview & Representative Instance

We are given the `head` of a singly-linked list with the following structural properties:
1. The list begins with a node with value $0$ and ends with a node with value $0$.
2. There are no two consecutive nodes with value $0$ (every zero-delimited segment contains at least one positive integer).
3. We must merge every contiguous sequence of nodes lying strictly between two consecutive $0$ nodes into a single node whose value is the sum of all merged nodes.
4. The delimiter $0$ nodes themselves are discarded from the final output list.

In our representative instance:
- Linked list: `0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0`.
- Segment 1: Lies between the initial $0$ and the second $0$. Nodes are $3$ and $1$. Sum: $3 + 1 = 4$.
- Segment 2: Lies between the second $0$ and the third (terminal) $0$. Nodes are $4$, $5$, and $2$. Sum: $4 + 5 + 2 = 11$.
- Resulting merged list: `4 -> 11`.

---

## 2. Mathematical & Algorithmic Principles

### Zero-Delimited Interval Partitioning

Let the linked list nodes be indexed $v_0, v_1, \dots, v_{m-1}$ where $v_0 = 0$ and $v_{m-1} = 0$.
Let the indices of all zero nodes be $0 = z_0 < z_1 < \dots < z_k = m - 1$.
The problem partitions the positive elements into $k$ disjoint subsegments:
$$I_j = \{v_p \mid z_{j-1} < p < z_j\}, \quad 1 \le j \le k$$

Each output node value $u_j$ is the exact sum of the elements in interval $I_j$:
$$u_j = \sum_{p = z_{j-1} + 1}^{z_j - 1} v_p$$

### Sentinel Chaining and Running Accumulator

Rather than modifying the input list with complicated pointer rewiring or performing a multi-pass scan:
- Maintain a dummy sentinel node `dummy` whose `next` will anchor the head of the output list.
- Maintain a pointer `tail` pointing to the last created node of the output list (initialized to `dummy`).
- Maintain an integer accumulator `s = 0`.
- Advance pointer `cur` starting from `head.next` (skipping the leading zero).
- **Rule 1 (Accumulation):** If `cur.val != 0`, add `cur.val` to `s`:
  $$s \leftarrow s + \text{cur.val}$$
- **Rule 2 (Boundary Splicing):** If `cur.val == 0`, a zero delimiter is reached.
  - Create a new node with value $s$.
  - Link it to the tail: `tail.next = ListNode(s)`.
  - Advance tail: `tail = tail.next`.
  - Reset accumulator: $s \leftarrow 0$.

| Variable / Pointer | Structural Purpose | Invariant Maintained |
|---|---|---|
| Sentinel `dummy` | Fixed anchor of the output list | `dummy.next` always points to the first merged node |
| Builder `tail` | Predecessor of the next appended node | Points to the most recently materialized merged node |
| Accumulator $s$ | Integer sum | Holds cumulative sum of non-zero values in current interval |
| Cursor `cur` | Linear scanner | Visits every node of the original list exactly once |

```mermaid
accTitle: Zero Delimiter Splicing Flowchart
accDescr: Flowchart illustrating accumulation of positive values and appending of sum node upon encountering a zero delimiter.
flowchart TD
    Scan["Advance cur to cur.next"] --> Check{"Is cur.val == 0?"}
    Check -- "No (Positive value)" --> Add["Accumulate: s += cur.val"]
    Check -- "Yes (Zero delimiter)" --> Splic["Append new node with value s: tail.next = Node(s)<br/>tail = tail.next<br/>Reset s = 0"]
    Add & Splic --> Loop{"Has cur reached None?"}
    Loop -- "No" --> Scan
    Loop -- "Yes" --> Done["Return dummy.next"]
```

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `head = [0, 3, 1, 0, 4, 5, 2, 0]`.

### Step 1: Initialization
- Create sentinel `dummy = ListNode()`, set `tail = dummy`.
- Accumulator `s = 0`.
- Cursor begins at first non-zero node: `cur = head.next` (node with value $3$).

### Step 2: Processing First Interval ($3 \to 1 \to 0$)
- **Node 1 (`cur.val = 3`):**
  - Non-zero: $s = 0 + 3 = 3$.
  - Advance: `cur` points to node $1$.
- **Node 2 (`cur.val = 1`):**
  - Non-zero: $s = 3 + 1 = 4$.
  - Advance: `cur` points to node $0$.
- **Node 3 (`cur.val = 0`):**
  - Zero delimiter encountered!
  - Append node with value $s = 4$: `tail.next = ListNode(4)`.
  - Advance `tail` to node $4$. Output list is now `dummy -> 4`.
  - Reset accumulator: $s = 0$.
  - Advance: `cur` points to node $4$.

### Step 3: Processing Second Interval ($4 \to 5 \to 2 \to 0$)
- **Node 4 (`cur.val = 4`):**
  - Non-zero: $s = 0 + 4 = 4$.
  - Advance: `cur` points to node $5$.
- **Node 5 (`cur.val = 5`):**
  - Non-zero: $s = 4 + 5 = 9$.
  - Advance: `cur` points to node $2$.
- **Node 6 (`cur.val = 2`):**
  - Non-zero: $s = 9 + 2 = 11$.
  - Advance: `cur` points to node $0$.
- **Node 7 (`cur.val = 0`):**
  - Zero delimiter encountered!
  - Append node with value $s = 11$: `tail.next = ListNode(11)`.
  - Advance `tail` to node $11$. Output list is now `dummy -> 4 -> 11`.
  - Reset accumulator: $s = 0$.
  - Advance: `cur` becomes `None`.

### Step 4: Loop Termination and Result Extraction
- `cur` is `None`; loop terminates.
- Return `dummy.next`, which is the linked list `4 -> 11`.

---

## 4. Comprehensive State Trace

The full step-by-step cursor progression is recorded below:

| Traversal Step | Node Visited (`cur.val`) | Node Type | Accumulator $s$ (After) | Output List State | Action Taken |
|---|---|---|---|---|---|
| Init | — | Setup | 0 | `dummy` | Set `cur = head.next` (val 3) |
| 1 | 3 | Value | 3 | `dummy` | Add to accumulator |
| 2 | 1 | Value | 4 | `dummy` | Add to accumulator |
| 3 | 0 | Delimiter | **0** | `dummy -> 4` | Append node $4$, reset $s = 0$ |
| 4 | 4 | Value | 4 | `dummy -> 4` | Add to accumulator |
| 5 | 5 | Value | 9 | `dummy -> 4` | Add to accumulator |
| 6 | 2 | Value | 11 | `dummy -> 4` | Add to accumulator |
| 7 | 0 | Delimiter | **0** | `dummy -> 4 -> 11` | Append node $11$, reset $s = 0$ |
| Halt | `None` | Terminal | 0 | `dummy -> 4 -> 11` | Return `dummy.next` (`[4, 11]`) |

### Segment Decomposition Matrix

| Segment Index $j$ | Start Delimiter Index | End Delimiter Index | Member Values | Evaluated Sum | Appended Node Value |
|---|---|---|---|---|---|
| 1 | 0 | 3 | $[3, 1]$ | $3 + 1 = 4$ | **4** |
| 2 | 3 | 7 | $[4, 5, 2]$ | $4 + 5 + 2 = 11$ | **11** |

---

## 5. Algorithmic Correctness & Soundness

### Partition Completeness and Disjointness
Because the input list begins and ends with $0$, every positive node lies between two consecutive zero nodes.
Because `cur` begins at `head.next` and advances through `cur.next` until `None`, every node is visited exactly once.
Every positive value is added to $s$ in the unique interval to which it belongs.
When a zero node is reached, the exact sum of the completed interval is materialized, and $s$ is reset to $0$, preventing leakage into subsequent intervals.
Hence, the constructed list contains exactly $k$ nodes with values $u_1, u_2, \dots, u_k$ corresponding to the mathematical sums of all $k$ zero-bounded intervals.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Single Zero-Bounded Segment:**
   - E.g., `head = [0, 1, 0]`. Single segment with sum $1$. Output: `[1]`.
2. **Multiple Single-Node Segments:**
   - E.g., `head = [0, 5, 0, 7, 0]`. Output: `[5, 7]`.
3. **Large Segment Sums:**
   - Individual node values up to $1000$, list length up to $2 \times 10^5$.
   - Segment sums fit comfortably in standard 32-bit and 64-bit integers.

### Anti-Patterns to Avoid
- **Rewiring In-Place Without Proper Next Caching:** Attempting to mutate `next` pointers of original nodes while traversing risks dropping the pointer to the rest of the list, leading to memory leaks or premature truncation.
- **Handling Leading Zero Separately:** Starting `cur` at `head.next` cleanly bypasses the initial boundary $0$, avoiding complex boolean initialization flags.
- **Double Counting or Leaving Residual Sums:** Resetting $s = 0$ immediately after node creation ensures subsequent segments start from a clean slate.

---

## 7. Complexity Analysis

- **Time Complexity:** $O(n)$ where $n$ is the number of nodes in the linked list. The algorithm visits each node in the list exactly once. Each step performs $O(1)$ arithmetic addition or node pointer allocation.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space excluding the returned nodes. If modifying in place, auxiliary space is strictly $O(1)$. When allocating the $k$ output nodes, space is $O(k)$ where $k < n$ is the number of zero-bounded intervals.
# Guided Example: Merge k Sorted Lists

We trace the step-by-step execution of the optimal $k$-way min-heap (priority queue) merge on a representative instance:

- **Input:** $\text{lists} = [[1, 4, 5], [1, 3, 4], [2, 6]]$
- **Required output:** $[1, 1, 2, 3, 4, 4, 5, 6]$

This instance demonstrates initializing a min-heap across $k = 3$ list heads, extracting the global minimum in $O(\log k)$ time, replenishing the heap with the successor node, and maintaining a single linked chain in place.

---

## 1. Instance & Teaching Goal

We are given $k = 3$ individually sorted linked lists containing a total of $N = 8$ nodes:
- List 0: $1 \to 4 \to 5 \to \text{None}$
- List 1: $1 \to 3 \to 4 \to \text{None}$
- List 2: $2 \to 6 \to \text{None}$

The objective is to merge all lists into one sorted linked list:
$$
1 \to 1 \to 2 \to 3 \to 4 \to 4 \to 5 \to 6 \to \text{None}
$$

A naive approach merges lists sequentially one by one ($O(k \cdot N)$ time), or dumps all values into an array and sorts them ($O(N \log N)$ time and $O(N)$ auxiliary space). The optimal algorithm uses a min-heap of size at most $k$, extracting the minimum node and inserting its successor in $O(\log k)$ time, achieving an optimal $O(N \log k)$ runtime with $O(k)$ auxiliary space.

**Where this instance sits among the candidate methods.** Four plausible strategies solve the same $k = 3$, $N = 8$ instance, and the table records the concrete cost each one pays here rather than only its asymptotic class.

| Method | Mechanism on this instance | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---|:---|:---|
| Sequential pairwise merging | Merge $L_0$ with $L_1$ (lists of length $3$ and $3$), then merge that $6$-node result with $L_2$ (length $2$) | Between $5$ and $12$ comparisons: $\min(3,3) + \min(6,2)$ up to $(3+3-1) + (6+2-1)$ | $O(1)$ | Cost grows with $k$; the worst case $O(kN)$ is unacceptable once $k$ approaches $10^{4}$ |
| Collect all values, then sort | Read the $8$ values, sort them, and build a fresh $8$-node chain | $O(N \log N)$ | $O(N)$ | Allocates $N$ replacement nodes and abandons the input nodes, so node identity is not preserved |
| Divide-and-conquer pairwise merging | Merge list pairs in $\lceil \log_2 k \rceil = 2$ rounds, halving the number of active lists each round | $O(N \log k)$ | $O(k)$ head handles | Same asymptotics as the heap, but needs an array of active head positions plus a two-list merge routine |
| $k$-way min-heap (this lesson) | $8$ pops and $8$ pushes on a heap whose size never exceeds $k = 3$ | $O(N \log k)$ | $O(k)$ | Every pop must be followed by a successor push; an exhausted list simply stops contributing candidates |

---

## 2. Conceptual Foundation & Invariants

### The $k$-Way Min-Heap
At any moment, the next globally smallest node must be one of the current front-runners among the $k$ lists. We maintain a min-heap $H$ containing at most $k$ entries:
$$
H = \{ (\text{node.val}, \text{list\_id}, \text{node}) \}
$$

### Algorithm Transitions
1. **Heap Initialization:** For each non-empty list $i \in [0, k-1]$, push its head node onto $H$.
2. **Sentinel Anchor:** Initialize $\text{dummy}$ and tail pointer $\text{tail} = \text{dummy}$.
3. **Extraction & Replenishment:** While $H$ is not empty:
   - Extract the root entry $(\text{val}, i, \text{node}) = \text{heappop}(H)$.
   - Append to merged chain: $\text{tail.next} \leftarrow \text{node}$, and advance $\text{tail} \leftarrow \text{node}$.
   - If $\text{node.next} \ne \text{None}$, push $(\text{node.next.val}, i, \text{node.next})$ into $H$.
4. **Termination:** When $H$ becomes empty, return $\text{dummy.next}$.

> **Invariant.** At step $m$, $\text{tail}$ points to the $m$-th smallest element across all $k$ lists. The min-heap $H$ holds the current unmerged head of every non-exhausted list. Therefore, the minimum of $H$ is unconditionally the $(m+1)$-th smallest element in the global sequence.

---

## 3. Step-by-Step Worked Execution

We trace the $k=3$ lists: $L_0 = [1, 4, 5]$, $L_1 = [1, 3, 4]$, $L_2 = [2, 6]$.

### Initialization
Push the head of each list into $H$:
- From $L_0$: $\text{Node}(1)$
- From $L_1$: $\text{Node}(1)$
- From $L_2$: $\text{Node}(2)$
- Initial Heap: $\{1_{(L_0)}, 1_{(L_1)}, 2_{(L_2)}\}$. $\text{tail} = \text{dummy}$.

---

### Step 1: Pop $1_{(L_0)}$
- Min element: $\text{Node}(1)$ from $L_0$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(1)$.
- Advance $L_0 \to \text{Node}(4)$. Push $4_{(L_0)}$ into $H$.
- Heap state: $\{1_{(L_1)}, 2_{(L_2)}, 4_{(L_0)}\}$.
- Merged chain: $\text{dummy} \to 1$.

---

### Step 2: Pop $1_{(L_1)}$
- Min element: $\text{Node}(1)$ from $L_1$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(1)$.
- Advance $L_1 \to \text{Node}(3)$. Push $3_{(L_1)}$ into $H$.
- Heap state: $\{2_{(L_2)}, 3_{(L_1)}, 4_{(L_0)}\}$.
- Merged chain: $\text{dummy} \to 1 \to 1$.

---

### Step 3: Pop $2_{(L_2)}$
- Min element: $\text{Node}(2)$ from $L_2$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(2)$.
- Advance $L_2 \to \text{Node}(6)$. Push $6_{(L_2)}$ into $H$.
- Heap state: $\{3_{(L_1)}, 4_{(L_0)}, 6_{(L_2)}\}$.
- Merged chain: $\text{dummy} \to 1 \to 1 \to 2$.

---

### Step 4: Pop $3_{(L_1)}$
- Min element: $\text{Node}(3)$ from $L_1$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(3)$.
- Advance $L_1 \to \text{Node}(4)$. Push $4_{(L_1)}$ into $H$.
- Heap state: $\{4_{(L_0)}, 4_{(L_1)}, 6_{(L_2)}\}$.
- Merged chain: $\text{dummy} \to 1 \to 1 \to 2 \to 3$.

---

### Step 5: Pop $4_{(L_0)}$
- Min element: $\text{Node}(4)$ from $L_0$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(4)$.
- Advance $L_0 \to \text{Node}(5)$. Push $5_{(L_0)}$ into $H$.
- Heap state: $\{4_{(L_1)}, 5_{(L_0)}, 6_{(L_2)}\}$.
- Merged chain: $\text{dummy} \to 1 \to 1 \to 2 \to 3 \to 4$.

---

### Step 6: Pop $4_{(L_1)}$
- Min element: $\text{Node}(4)$ from $L_1$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(4)$.
- Advance $L_1 \to \text{None}$ ($L_1$ exhausted). No push.
- Heap state: $\{5_{(L_0)}, 6_{(L_2)}\}$.
- Merged chain: $\text{dummy} \to 1 \to 1 \to 2 \to 3 \to 4 \to 4$.

---

### Step 7: Pop $5_{(L_0)}$
- Min element: $\text{Node}(5)$ from $L_0$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(5)$.
- Advance $L_0 \to \text{None}$ ($L_0$ exhausted). No push.
- Heap state: $\{6_{(L_2)}\}$.
- Merged chain: $\text{dummy} \to 1 \to 1 \to 2 \to 3 \to 4 \to 4 \to 5$.

---

### Step 8: Pop $6_{(L_2)}$
- Min element: $\text{Node}(6)$ from $L_2$.
- Append to result: $\text{tail.next} \leftarrow \text{Node}(6)$.
- Advance $L_2 \to \text{None}$ ($L_2$ exhausted). No push.
- Heap state: $\emptyset$ (empty).
- Terminate: Set $\text{tail.next} = \text{None}$. Return $\text{dummy.next}$.

---

## 4. Complete Execution Trace

| Step | Popped Node | Origin List | Spliced Node Value | Successor Pushed to Heap | Min-Heap Contents After Step | Active Merged Chain |
|:---:|:---:|:---:|:---:|:---:|:---|:---|
| 0 (Init) | - | - | - | Heads: $1_{(0)}, 1_{(1)}, 2_{(2)}$ | $\{1_{(0)}, 1_{(1)}, 2_{(2)}\}$ | $\text{dummy}$ |
| 1 | $\text{Node}(1)$ | $L_0$ | 1 | $4_{(0)}$ | $\{1_{(1)}, 2_{(2)}, 4_{(0)}\}$ | $\text{dummy} \to 1$ |
| 2 | $\text{Node}(1)$ | $L_1$ | 1 | $3_{(1)}$ | $\{2_{(2)}, 3_{(1)}, 4_{(0)}\}$ | $\text{dummy} \to 1 \to 1$ |
| 3 | $\text{Node}(2)$ | $L_2$ | 2 | $6_{(2)}$ | $\{3_{(1)}, 4_{(0)}, 6_{(2)}\}$ | $\text{dummy} \to 1 \to 1 \to 2$ |
| 4 | $\text{Node}(3)$ | $L_1$ | 3 | $4_{(1)}$ | $\{4_{(0)}, 4_{(1)}, 6_{(2)}\}$ | $\text{dummy} \to 1 \to 1 \to 2 \to 3$ |
| 5 | $\text{Node}(4)$ | $L_0$ | 4 | $5_{(0)}$ | $\{4_{(1)}, 5_{(0)}, 6_{(2)}\}$ | $\text{dummy} \dots \to 4$ |
| 6 | $\text{Node}(4)$ | $L_1$ | 4 | None (Exhausted) | $\{5_{(0)}, 6_{(2)}\}$ | $\text{dummy} \dots \to 4 \to 4$ |
| 7 | $\text{Node}(5)$ | $L_0$ | 5 | None (Exhausted) | $\{6_{(2)}\}$ | $\text{dummy} \dots \to 4 \to 4 \to 5$ |
| 8 | $\text{Node}(6)$ | $L_2$ | 6 | None (Exhausted) | $\emptyset$ | $\text{dummy} \dots \to 5 \to 6 \to \text{None}$ |

---

## 5. Algorithmic Correctness

**Soundness.** Each of the $k$ input lists is sorted in non-decreasing order. Therefore, for any list $i$, the head node is $\le$ all subsequent nodes in list $i$. At any point, the global minimum among all remaining unmerged nodes must reside at one of the $k$ current list heads. Maintaining these heads in a min-heap guarantees that $\text{heappop}$ always extracts the global minimum.

**Completeness.** Every node from every list is pushed into the heap exactly once and popped exactly once. The algorithm continues until the heap is empty, ensuring that all $N$ nodes are incorporated into the output list.

---

## 6. Traps This Instance Exposes

- **Empty Input / Lists of Empty Nodes:** The input $\text{lists}$ may be empty `[]`, or contain empty heads `[None, None]`. Pushing only non-empty heads (`if node: heappush(...)`) guards against `AttributeError`.
- **Node Comparison in Priority Queue:** In Python, tuples `(val, node)` will attempt to compare `node < node` if `val == val`. Because `ListNode` does not define `<` by default, this raises a `TypeError`. Storing `(node.val, list_index, node)` provides a unique integer tie-breaker, preventing node object comparisons.
- **Dangling Tail Pointers:** When splicing existing nodes, the last popped node might still point to other nodes in its original list. Explicitly terminating $\text{tail.next} = \text{None}$ prevents accidental cycles.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log k)$, where $N$ is the total number of nodes across all lists and $k$ is the number of linked lists. There are $N$ nodes total; each node is pushed and popped from the min-heap of size at most $k$ exactly once. Each heap operation takes $O(\log k)$ time.
- **Auxiliary Space Complexity:** $O(k)$. The min-heap stores at most $k$ node references simultaneously. Node rewires are performed in place.

**Heap occupancy accounting for this instance.** Each of the $N = 8$ nodes is pushed exactly once and popped exactly once, so this instance costs exactly $2N = 16$ heap operations. The table shows where those operations occur and confirms that the heap never holds more than $k = 3$ entries.

| Extraction | Entry popped | Heap size $h$ before pop | Height $\lfloor \log_2 h \rfloor$ | Successor pushed | Heap size after | Cumulative heap operations |
|:---:|:---|:---:|:---:|:---|:---:|:---:|
| 1 | $1_{(L_0)}$ | 3 | 1 | $4_{(L_0)}$ | 3 | 5 |
| 2 | $1_{(L_1)}$ | 3 | 1 | $3_{(L_1)}$ | 3 | 7 |
| 3 | $2_{(L_2)}$ | 3 | 1 | $6_{(L_2)}$ | 3 | 9 |
| 4 | $3_{(L_1)}$ | 3 | 1 | $4_{(L_1)}$ | 3 | 11 |
| 5 | $4_{(L_0)}$ | 3 | 1 | $5_{(L_0)}$ | 3 | 13 |
| 6 | $4_{(L_1)}$ | 3 | 1 | none ($L_1$ exhausted) | 2 | 14 |
| 7 | $5_{(L_0)}$ | 2 | 1 | none ($L_0$ exhausted) | 1 | 15 |
| 8 | $6_{(L_2)}$ | 1 | 0 | none ($L_2$ exhausted) | 0 | 16 |

The cumulative column begins with the three initial head insertions and then adds one pop plus every successor push, giving $3 + 8 + 5 = 16$ operations. Because the heap never holds more than $k = 3$ entries, its height never exceeds $\lfloor \log_2 3 \rfloor = 1$, so each extraction moves an entry across at most one level. That is the concrete reason the $O(\log k)$ factor is small for this instance while still growing only logarithmically as $k$ approaches $10^{4}$.
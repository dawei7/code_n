# Guided Example: Partition List

We trace the step-by-step dual-sentinel chain partitioning and splicing on a representative linked list:

- **Input:** $\text{head} = [1, 4, 3, 2, 5, 2]$, $x = 3$
- **Required output:** $[1, 2, 2, 4, 3, 5]$

This instance demonstrates partitioning nodes into two independent linked lists (`less` and `greater_or_equal`), preserving original relative order within both partitions, null-terminating the trailing partition to prevent cycles, and concatenating the two sublists in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given the head of a linked list:
$$
1 \longrightarrow 4 \longrightarrow 3 \longrightarrow 2 \longrightarrow 5 \longrightarrow 2 \longrightarrow \emptyset
$$
and a partition value $x = 3$, partition the list such that all nodes with values less than $x$ come before nodes with values greater than or equal to $x$.
You must preserve the original relative order of the nodes in each of the two partitions.

In this instance:
- Partition 1 ($< 3$): nodes $1, 2, 2$ (in original sequence: $1 \to 2 \to 2$).
- Partition 2 ($\ge 3$): nodes $4, 3, 5$ (in original sequence: $4 \to 3 \to 5$).
- Concatenated result: $1 \longrightarrow 2 \longrightarrow 2 \longrightarrow 4 \longrightarrow 3 \longrightarrow 5 \longrightarrow \emptyset$.

A naive approach copying values into an array requires extra memory and node re-allocation.
Using two dummy sentinel heads (`less_head` and `greater_head`), we route each incoming node into one of two output streams in a single linear pass, concatenating them at the end.

| Approach | Mechanism | Time | Auxiliary space | Tradeoff or failure mode |
|:---|:---|:---:|:---:|:---|
| Two sentinel chains with pointer splicing | Route each visited node into one of two chains, sever the trailing chain, then splice | $O(N)$ | $O(1)$ | Fastest and allocation-free, but forgetting the trailing null leaves a live cycle in the result. |
| Collect values, partition the array, write values back | Gather the $N$ values, apply a stable split, then overwrite the existing nodes | $O(N)$ | $O(N)$ | Simple to reason about, but it rewrites values rather than relinking nodes and needs a second pass. |
| Collect node references into two buffers, then relink | Push each node reference into one of two buffers and rebuild the links afterwards | $O(N)$ | $O(N)$ | Preserves identity and order, yet allocates two buffers proportional to the list length. |
| Repeated prefix repair | Scan forward and move each small node into the growing prefix region | $O(N^2)$ | $O(1)$ | Re-walks the prefix for every relocation, so a long list degrades quadratically. |

---

## 2. Conceptual Foundation & Invariants

### Dual-Sentinel Stream Partitioning
We allocate two sentinel nodes:
- $\text{less\_dummy}$ with pointer $\text{less} = \text{less\_dummy}$
- $\text{greater\_dummy}$ with pointer $\text{greater} = \text{greater\_dummy}$

We iterate $\text{cur}$ through the input list:
1. **Routing:**
   - If $\text{cur.val} < x$:
     $$
     \text{less.next} \leftarrow \text{cur}, \quad \text{less} \leftarrow \text{less.next}
     $$
   - Else ($\text{cur.val} \ge x$):
     $$
     \text{greater.next} \leftarrow \text{cur}, \quad \text{greater} \leftarrow \text{greater.next}
     $$
2. **Cycle Prevention (Null Termination):**
   The last node in the `greater` partition might still reference a later node in the original list that was routed to the `less` partition, creating an infinite cycle!
   We explicitly sever the trailing reference:
   $$
   \text{greater.next} \leftarrow \emptyset
   $$
3. **Splicing:**
   Connect the tail of the `less` chain to the head of the `greater` chain:
   $$
   \text{less.next} \leftarrow \text{greater\_dummy.next}
   $$
   Return $\text{less\_dummy.next}$.

> **Invariant.** The relative order of nodes within both `less` and `greater` sublists strictly mirrors their original order in the input list.

---

## 3. Step-by-Step Worked Execution

We trace $[1, 4, 3, 2, 5, 2]$ with $x = 3$:

### Initialization
- $\text{less\_dummy} \to \emptyset$, $\text{greater\_dummy} \to \emptyset$.
- $\text{less} = \text{less\_dummy}$, $\text{greater} = \text{greater\_dummy}$.
- $\text{cur} = \text{Node}(1)$.

---

### Step 1: Node 1 ($\text{val} = 1 < 3$)
- Route to `less`: $\text{less.next} \leftarrow \text{Node}(1)$.
- Advance `less` to $\text{Node}(1)$.
- `less` chain: $\text{dummy}_L \to 1$.

---

### Step 2: Node 4 ($\text{val} = 4 \ge 3$)
- Route to `greater`: $\text{greater.next} \leftarrow \text{Node}(4)$.
- Advance `greater` to $\text{Node}(4)$.
- `greater` chain: $\text{dummy}_G \to 4$.

---

### Step 3: Node 3 ($\text{val} = 3 \ge 3$)
- Route to `greater`: $\text{greater.next} \leftarrow \text{Node}(3)$.
- Advance `greater` to $\text{Node}(3)$.
- `greater` chain: $\text{dummy}_G \to 4 \to 3$.

---

### Step 4: Node 2 ($\text{val} = 2 < 3$)
- Route to `less`: $\text{less.next} \leftarrow \text{Node}(2)$.
- Advance `less` to first $\text{Node}(2)$.
- `less` chain: $\text{dummy}_L \to 1 \to 2$.

---

### Step 5: Node 5 ($\text{val} = 5 \ge 3$)
- Route to `greater`: $\text{greater.next} \leftarrow \text{Node}(5)$.
- Advance `greater` to $\text{Node}(5)$.
- `greater` chain: $\text{dummy}_G \to 4 \to 3 \to 5$.

---

### Step 6: Node 2 ($\text{val} = 2 < 3$)
- Route to `less`: $\text{less.next} \leftarrow \text{Node}(2)$.
- Advance `less` to second $\text{Node}(2)$.
- `less` chain: $\text{dummy}_L \to 1 \to 2 \to 2$.

---

### Concatenation & Termination
1. Sever greater tail: $\text{Node}(5).\text{next} \leftarrow \emptyset$.
2. Link chains: $\text{less.next} \leftarrow \text{greater\_dummy.next} \implies \text{Node}(2).\text{next} \leftarrow \text{Node}(4)$.
3. Result: $1 \longrightarrow 2 \longrightarrow 2 \longrightarrow 4 \longrightarrow 3 \longrightarrow 5 \longrightarrow \emptyset$.

---

## 4. Complete Execution Trace

| Step | Visited Node $\text{cur}$ | Condition ($\text{val} < 3$) | Destination Partition | `less` Sublist State | `greater` Sublist State |
|:---:|:---:|:---:|:---:|:---|:---|
| 1 | $\text{Node}(1)$ | $1 < 3$ (True) | `less` | $\text{dummy}_L \to 1$ | $\text{dummy}_G$ |
| 2 | $\text{Node}(4)$ | $4 < 3$ (False) | `greater` | $\text{dummy}_L \to 1$ | $\text{dummy}_G \to 4$ |
| 3 | $\text{Node}(3)$ | $3 < 3$ (False) | `greater` | $\text{dummy}_L \to 1$ | $\text{dummy}_G \to 4 \to 3$ |
| 4 | $\text{Node}(2)$ | $2 < 3$ (True) | `less` | $\text{dummy}_L \to 1 \to 2$ | $\text{dummy}_G \to 4 \to 3$ |
| 5 | $\text{Node}(5)$ | $5 < 3$ (False) | `greater` | $\text{dummy}_L \to 1 \to 2$ | $\text{dummy}_G \to 4 \to 3 \to 5$ |
| 6 | $\text{Node}(2)$ | $2 < 3$ (True) | `less` | $\text{dummy}_L \to 1 \to 2 \to 2$ | $\text{dummy}_G \to 4 \to 3 \to 5$ |
| Splice | - | - | Connect | $\text{less.next} \to \text{greater\_dummy.next}$ | $\text{greater.next} \to \emptyset$ |
| Final | - | - | - | **$1 \to 2 \to 2 \to 4 \to 3 \to 5 \to \emptyset$** | - |

### Node-Identity Ledger

Both partitions contain three nodes, and the value $2$ occurs twice, so the result can
only be checked by tracking node identity. Naming each node by its original index makes
the stability claim exact:

| Original index | Node value | Route test `val < 3` | Destination | Arrival rank inside its partition | Final output index |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | true | `less` | 1 of 3 | 0 |
| 1 | 4 | false | `greater` | 1 of 3 | 3 |
| 2 | 3 | false | `greater` | 2 of 3 | 4 |
| 3 | 2 | true | `less` | 2 of 3 | 1 |
| 4 | 5 | false | `greater` | 3 of 3 | 5 |
| 5 | 2 | true | `less` | 3 of 3 | 2 |

The mapping is a bijection on indices: no node is dropped, duplicated, or reordered
inside its partition. A `less` node at rank $k$ lands at output index $k - 1$, and a
`greater` node at rank $k$ lands at output index $\lvert \text{less} \rvert + k - 1 = 3 + k - 1$.
The two nodes holding the value $2$ sit at original indices $3$ and $5$ and therefore
arrive at output positions $1$ and $2$; the earlier of the two still comes first, which is
exactly what stability means here.

---

## 5. Algorithmic Correctness

**Soundness.** Every node in the original list is examined and appended to either the `less` list or the `greater` list. Because elements are appended in the exact order they are encountered, their relative order within each partition is strictly maintained.

**Completeness.** Terminating $\text{greater.next} = \emptyset$ eliminates any residual links from original positions, preventing circular loops. Connecting `less.next = greater_dummy.next` produces a single valid acyclic linked list.

---

## 6. Traps This Instance Exposes

- **Memory Cycle Without Suffix Severing:** In this instance, the last node processed was $\text{Node}(2)$, but the last node in `greater` was $\text{Node}(5)$. In the original list, $\text{Node}(5)$ pointed to the second $\text{Node}(2)$. If you do not set $\text{greater.next} = \emptyset$, $\text{Node}(5)$ will continue pointing to $\text{Node}(2)$, forming an infinite circular loop: $1 \to 2 \to 2 \to 4 \to 3 \to 5 \to 2 \to 4 \dots$!
- **Empty Less Partition:** If all elements are $\ge x$ (e.g. $[4, 5]$ with $x = 3$), `less` remains at `less_dummy`. The assignment `less.next = greater_dummy.next` seamlessly attaches the entire `greater` list directly to `less_dummy`, returning the unaltered list.

### Boundary Instances and Their Verdicts

| Instance | `head` | $x$ | Expected output | Boundary exercised | Why the routing is correct |
|:---|:---|:---:|:---|:---|:---|
| Interleaved partitions | $[1, 4, 3, 2, 5, 2]$ | 3 | $[1, 2, 2, 4, 3, 5]$ | Both partitions non-empty and interleaved | Each node is appended once, so the two $2$-nodes retain their relative order and the greater chain stays $4, 3, 5$. |
| Reverse partition groups | $[2, 1]$ | 2 | $[1, 2]$ | The pivot value itself appears in the input | The comparison is strict, so $2 \ge 2$ routes to `greater` while $1$ goes to `less`. |
| Empty list | $[\ ]$ | 0 | $[\ ]$ | No nodes at all | Both sentinels stay unlinked and `less_dummy.next` is still null, which is the required answer. |
| All values below pivot | $[1, 2, 3]$ | 10 | $[1, 2, 3]$ | `greater` partition empty | Every node enters `less`, so the trailing sever is applied to an untouched `greater` sentinel and the splice adds nothing. |
| Order inside both groups | $[3, 1, 2, 3, 0, 2]$ | 3 | $[1, 2, 0, 2, 3, 3]$ | Stability under a longer interleaving | `less` receives $1, 2, 0, 2$ in arrival order and `greater` receives $3, 3$; no traversal ever reorders within a chain. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. Each node is traversed exactly once.
- **Auxiliary Space Complexity:** $O(1)$. Reorganizes pointers in place using two dummy sentinel heads.

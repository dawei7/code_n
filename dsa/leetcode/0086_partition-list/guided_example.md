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

---

## 5. Algorithmic Correctness

**Soundness.** Every node in the original list is examined and appended to either the `less` list or the `greater` list. Because elements are appended in the exact order they are encountered, their relative order within each partition is strictly maintained.

**Completeness.** Terminating $\text{greater.next} = \emptyset$ eliminates any residual links from original positions, preventing circular loops. Connecting `less.next = greater_dummy.next` produces a single valid acyclic linked list.

---

## 6. Traps This Instance Exposes

- **Memory Cycle Without Suffix Severing:** In this instance, the last node processed was $\text{Node}(2)$, but the last node in `greater` was $\text{Node}(5)$. In the original list, $\text{Node}(5)$ pointed to the second $\text{Node}(2)$. If you do not set $\text{greater.next} = \emptyset$, $\text{Node}(5)$ will continue pointing to $\text{Node}(2)$, forming an infinite circular loop: $1 \to 2 \to 2 \to 4 \to 3 \to 5 \to 2 \to 4 \dots$!
- **Empty Less Partition:** If all elements are $\ge x$ (e.g. $[4, 5]$ with $x = 3$), `less` remains at `less_dummy`. The assignment `less.next = greater_dummy.next` seamlessly attaches the entire `greater` list directly to `less_dummy`, returning the unaltered list.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of nodes in the linked list. Each node is traversed exactly once.
- **Auxiliary Space Complexity:** $O(1)$. Reorganizes pointers in place using two dummy sentinel heads.
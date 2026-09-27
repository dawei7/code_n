# Guided Example: Sort List

We trace the step-by-step divide-and-conquer bisection and in-place sorted list merging of Merge Sort on representative singly linked list instances:

- **Input:** $\text{head} = [4, 2, 1, 3]$
- **Required output:** $[1, 2, 3, 4]$
- **Odd-Length Negative Instance:** $\text{head} = [-1, 5, 3, 4, 0] \implies [-1, 0, 3, 4, 5]$

This instance demonstrates top-down divide-and-conquer on linked structures, finding the median node using slow/fast pointers, severing sublists cleanly at `prev.next = None`, merging two sorted lists in-place with a dummy sentinel node, and achieving guaranteed $O(N \log N)$ time with $O(\log N)$ recursion stack space.

---

## 1. Instance & Teaching Goal

Given the head of an unsorted linked list:
$$
4 \longrightarrow 2 \longrightarrow 1 \longrightarrow 3
$$
Sort the list in ascending order in $O(N \log N)$ time.

Quick Sort on linked lists degrades to $O(N^2)$ time on adversarial sorted inputs.
Insertion Sort takes $O(N^2)$ time.
Merge Sort is the optimal sorting algorithm for singly linked lists:
- In arrays, Merge Sort requires $O(N)$ auxiliary buffer allocation.
- In linked lists, merging two sorted lists requires **zero node reallocation**—it simply splices existing pointer links in place!
Dividing the list in halves takes $O(N)$ time via slow/fast pointers, and merging two sorted halves of size $N/2$ takes $O(N)$ pointer rewires, yielding the recurrence $T(N) = 2T(N/2) + O(N) = O(N \log N)$.

---

## 2. Conceptual Foundation & Invariants

### Divide-and-Conquer Protocol

#### 1. Base Case:
If $\text{head} == \emptyset$ or $\text{head.next} == \emptyset$:
A list of length 0 or 1 is already sorted. Return `head`.

#### 2. Split into Halves (Divide):
Use slow and fast pointers to find the median:
- Initialize $\text{prev} = \emptyset, \, \text{slow} = \text{head}, \, \text{fast} = \text{head}$.
- While $\text{fast}$ and $\text{fast.next}$:
  $$
  \text{prev} = \text{slow}, \quad \text{slow} = \text{slow.next}, \quad \text{fast} = \text{fast.next.next}
  $$
- Sever the list:
  $$
  \text{prev.next} = \emptyset
  $$
- The two halves are $\text{left} = \text{head}$ and $\text{right} = \text{slow}$.

#### 3. Recurse:
$$
L_1 = \text{sortList}(\text{left}), \quad L_2 = \text{sortList}(\text{right})
$$

#### 4. Merge Two Sorted Lists (Conquer):
Using sentinel $\text{dummy} = \text{Node}(0)$ and pointer `curr`:
- While $L_1$ and $L_2$:
  - If $L_1.\text{val} \le L_2.\text{val}$: $\text{curr.next} = L_1, \, L_1 = L_1.\text{next}$.
  - Else: $\text{curr.next} = L_2, \, L_2 = L_2.\text{next}$.
  - $\text{curr} = \text{curr.next}$.
- Attach remainder: $\text{curr.next} = L_1 \text{ if } L_1 \text{ else } L_2$.
- Return $\text{dummy.next}$.

> **Invariant.** The return value of $\text{merge}(L_1, L_2)$ is a single connected list containing all nodes from $L_1$ and $L_2$ in strictly non-decreasing order.

---

## 3. Step-by-Step Worked Execution

We trace the recursive tree on $\text{head} = [4, 2, 1, 3]$:

### Level 1: Split at Midpoint
- `slow` lands on `Node(1)` (index 2).
- Sever: $\text{prev} = \text{Node}(2) \implies \text{Node}(2).\text{next} = \emptyset$.
- Left half: $4 \to 2 \to \emptyset$.
- Right half: $1 \to 3 \to \emptyset$.

---

### Level 2 (Left Branch): Sort $[4, 2]$
- Split $[4, 2]$:
  - Left: $[4]$ (base case $\implies$ returns $[4]$).
  - Right: $[2]$ (base case $\implies$ returns $[2]$).
- **Merge $[4]$ and $[2]$:**
  - Compare $4$ vs $2$: $2 < 4 \implies$ pick $2$.
  - Remainder is $4 \implies$ attach $4$.
  - Result of left branch: $2 \to 4 \to \emptyset$.

---

### Level 2 (Right Branch): Sort $[1, 3]$
- Split $[1, 3]$:
  - Left: $[1]$ (base case $\implies$ returns $[1]$).
  - Right: $[3]$ (base case $\implies$ returns $[3]$).
- **Merge $[1]$ and $[3]$:**
  - Compare $1$ vs $3$: $1 \le 3 \implies$ pick $1$.
  - Remainder is $3 \implies$ attach $3$.
  - Result of right branch: $1 \to 3 \to \emptyset$.

---

### Level 1 (Final Merge): Merge $[2, 4]$ and $[1, 3]$
Initialize $\text{dummy} \to \emptyset, \, \text{curr} = \text{dummy}$.
- $L_1 = [2, 4], \, L_2 = [1, 3]$.

- **Comparison 1 ($2$ vs $1$):**
  - $1 < 2 \implies \text{curr.next} = \text{Node}(1)$.
  - $L_2$ advances to $\text{Node}(3)$.
  - `curr` advances to $\text{Node}(1)$.
  - List: $\text{dummy} \to 1$.

- **Comparison 2 ($2$ vs $3$):**
  - $2 \le 3 \implies \text{curr.next} = \text{Node}(2)$.
  - $L_1$ advances to $\text{Node}(4)$.
  - `curr` advances to $\text{Node}(2)$.
  - List: $\text{dummy} \to 1 \to 2$.

- **Comparison 3 ($4$ vs $3$):**
  - $3 < 4 \implies \text{curr.next} = \text{Node}(3)$.
  - $L_2$ becomes null.
  - `curr` advances to $\text{Node}(3)$.
  - List: $\text{dummy} \to 1 \to 2 \to 3$.

- **Attach Exhaustion Remainder:**
  - $L_2$ is empty. Attach remaining $L_1$ ($\text{Node}(4)$):
  - $\text{curr.next} = \text{Node}(4)$.
  - List: $\text{dummy} \to 1 \to 2 \to 3 \to 4 \to \emptyset$.

Return `dummy.next = Node(1)`: $[1, 2, 3, 4]$.

---

## 4. Complete Execution Trace

```text
Recursion Tree:
                [4, 2, 1, 3]
               /            \
          [4, 2]            [1, 3]
          /    \            /    \
        [4]    [2]        [1]    [3]
          \    /            \    /
          [2, 4]            [1, 3]
               \            /
                [1, 2, 3, 4]
```

| Recursion Level | Operation | Input Sublists | Sublist Halves Generated | Merged Output |
|:---:|:---:|:---:|:---|:---:|
| Level 2a | Divide | $[4, 2]$ | $[4]$ and $[2]$ | - |
| Level 2a | Merge | $[4]$ and $[2]$ | Compare $4$ vs $2$ | **$[2, 4]$** |
| Level 2b | Divide | $[1, 3]$ | $[1]$ and $[3]$ | - |
| Level 2b | Merge | $[1]$ and $[3]$ | Compare $1$ vs $3$ | **$[1, 3]$** |
| **Level 1** | **Final Merge** | **$[2, 4]$ and $[1, 3]$** | Compare $2$ vs $1$, then $2$ vs $3$, then $4$ vs $3$ | **$[1, 2, 3, 4]$** |

---

## 5. Algorithmic Correctness

**Soundness.** Base cases of 0 or 1 node are sorted. By the induction hypothesis, recursive calls return sorted sublists $L_1$ and $L_2$. The standard two-way merge picks the minimum available head node at each step, preserving the sorted invariant throughout the concatenation.

**Completeness.** Splitting at the median partitions all elements into two disjoint halves without dropping nodes. Every node from both sublists is re-linked into the merged list.

---

## 6. Traps This Instance Exposes

- **Infinite Recursion on Median Split:** If the split does not sever the link ($\text{prev.next} = \emptyset$), the left half will still contain the right half, causing `len(left) == len(head)` and triggering infinite recursion!
- **Uneven Midpoint Choice:** When $N = 2$ (e.g. $[4, 2]$), `slow` must advance to the second node while `prev` terminates the first node, producing $[4]$ and $[2]$. If `slow` stayed at $[4]$, splitting would fail.
- **Empty List:** Handled cleanly by `if not head or not head.next: return head`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \log N)$ in all cases (worst, average, and best). Finding the midpoint takes $O(N)$ and merging takes $O(N)$. With $\log N$ levels of recursive bisection, $T(N) = 2T(N/2) + O(N) = O(N \log N)$ by the Master Theorem.
- **Auxiliary Space Complexity:** $O(\log N)$ call stack depth for top-down recursion. Pointer merging itself uses $O(1)$ extra heap memory.
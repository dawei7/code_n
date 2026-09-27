# Guided Example: Convert Sorted List to Binary Search Tree

We trace the step-by-step conversion of a sorted singly linked list into a height-balanced BST using both tortoise-and-hare bisection and $O(N)$ inorder pointer simulation:

- **Input:** $\text{head} = [-10, -3, 0, 5, 9]$
- **Required output:** $[0, -3, 9, -10, \text{null}, 5]$ (or $[0, -10, 5, \text{null}, -3, \text{null}, 9]$)
- **Base Instance:** $\text{head} = [] \implies \emptyset, \quad \text{head} = [0] \implies [0]$

This instance demonstrates finding the linked list median via slow and fast pointers, severing left prefixes in-place, and the advanced $O(N)$ Inorder Tree Simulation technique that builds the BST in lockstep with sequential linked list traversal.

---

## 1. Instance & Teaching Goal

Given the head of a sorted singly linked list:
$$
-10 \longrightarrow -3 \longrightarrow 0 \longrightarrow 5 \longrightarrow 9 \longrightarrow \emptyset
$$
convert it to a **height-balanced** Binary Search Tree.

In an array (LeetCode 108), the median index $M = \lfloor N/2 \rfloor$ is accessible in $O(1)$ time. In a singly linked list, accessing the $k$-th node requires $O(k)$ pointer advances.

Two distinct algorithms resolve this:
1. **Tortoise and Hare Bisection ($O(N \log N)$ Time, $O(\log N)$ Space):**
   A fast pointer moves two steps while a slow pointer moves one step to find the list's midpoint. A predecessor pointer severs the left sublist (`prev.next = None`).
2. **Inorder Simulation ($O(N)$ Time, $O(\log N)$ Space):**
   First measure the length $N$. Then recurse over index ranges $[L, R]$, constructing the left subtree first, consuming the active list node as the root (`head = head.next`), and then constructing the right subtree. This mirrors an inorder traversal ($L \to \text{Root} \to R$), achieving $O(N)$ linear time without pointer severing.

---

## 2. Conceptual Foundation & Invariants

### Method 1: Tortoise and Hare Midpoint Severing
To partition list $[start \dots end]$:
1. Initialize `slow = head`, `fast = head`, `prev = None`.
2. While `fast` and `fast.next`:
   - `prev = slow`
   - `slow = slow.next`
   - `fast = fast.next.next`
3. Sever left half:
   If `prev` is not null:
   $$
   \text{prev.next} = \emptyset
   $$
4. Construct node:
   $$
   \text{root} = \text{TreeNode}(\text{slow.val})
   $$
   - If `prev` is not null, recurse $\text{root.left} = \text{sortedListToBST}(\text{head})$.
   - Recurse $\text{root.right} = \text{sortedListToBST}(\text{slow.next})$.

### Method 2: Inorder Global Cursor Simulation
Let `curr` point to `head`.
Define $\text{build}(L, R)$:
- If $L > R$: return $\emptyset$.
- $M = L + \lfloor (R - L) / 2 \rfloor$.
- $\text{left\_child} = \text{build}(L, M - 1)$.
- Create root:
  $$
  \text{root} = \text{TreeNode}(\text{curr.val})
  $$
  $$
  \text{curr} \leftarrow \text{curr.next} \quad (\text{Advance sequential cursor})
  $$
- $\text{right\_child} = \text{build}(M + 1, R)$.
- Link $\text{root.left} = \text{left\_child}, \text{root.right} = \text{right\_child}$.
- Return `root`.

> **Invariant.** Under Inorder Simulation, the global linked list pointer `curr` is read and advanced exactly when its left subtree has been completely assembled, precisely matching the inorder property of BSTs.

---

## 3. Step-by-Step Worked Execution

We trace Inorder Simulation on $[-10, -3, 0, 5, 9]$ ($N = 5$, range $[0, 4]$):

### Initialization
- Compute length: $N = 5$.
- Range: $L = 0, R = 4$.
- Global pointer `curr` initially at $\text{Node}(-10)$.

---

### Step 1: Global Root Setup ($[0, 4]$)
- Midpoint: $M = 0 + \lfloor 4 / 2 \rfloor = 2$.
- Must build left subtree from range $[0, 1]$ before creating root.

---

### Step 2: Build Left Subtree ($[0, 1]$)
- Midpoint: $M = 0 + \lfloor 1 / 2 \rfloor = 0$.
- Must build left child from range $[0, -1]$:
  - Range $0 > -1 \implies$ returns $\emptyset$.
- **Read & Advance Cursor:**
  - `curr` has value $-10$.
  - Create node: $T_0 = \text{TreeNode}(-10)$.
  - Advance `curr` to $\text{Node}(-3)$.
- Build right child of $T_0$ from range $[1, 1]$:
  - Midpoint: $M = 1$.
  - Left child $[1, 0] \implies \emptyset$.
  - **Read & Advance Cursor:**
    - `curr` has value $-3$.
    - Create node: $T_1 = \text{TreeNode}(-3)$.
    - Advance `curr` to $\text{Node}(0)$.
  - Right child $[2, 1] \implies \emptyset$.
  - Link: $T_1.\text{left} = \emptyset, T_1.\text{right} = \emptyset$.
- Link: $T_0.\text{right} = T_1$.
- Left subtree of root complete: $-10$ with right child $-3$.

---

### Step 3: Global Root Node Construction (Midpoint $M = 2$)
- Left subtree completed!
- **Read & Advance Cursor:**
  - `curr` is at $\text{Node}(0)$.
  - Create root node: $\text{Root} = \text{TreeNode}(0)$.
  - Link: $\text{Root.left} = T_0$.
  - Advance `curr` to $\text{Node}(5)$.

---

### Step 4: Build Right Subtree ($[3, 4]$)
- Midpoint: $M = 3 + \lfloor 1 / 2 \rfloor = 3$.
- Build left child $[3, 2] \implies \emptyset$.
- **Read & Advance Cursor:**
  - `curr` has value $5$.
  - Create node: $T_3 = \text{TreeNode}(5)$.
  - Advance `curr` to $\text{Node}(9)$.
- Build right child of $T_3$ from range $[4, 4]$:
  - Midpoint: $M = 4$. Left $[4, 3] \implies \emptyset$.
  - **Read & Advance Cursor:**
    - `curr` has value $9$.
    - Create node: $T_4 = \text{TreeNode}(9)$.
    - Advance `curr` to $\emptyset$.
  - Right $[5, 4] \implies \emptyset$.
  - Link: $T_4.\text{left} = \emptyset, T_4.\text{right} = \emptyset$.
- Link: $T_3.\text{right} = T_4$.
- Right subtree complete: $5$ with right child $9$.

---

### Step 5: Final Link
- Link: $\text{Root.right} = T_3$.
- Returns $\text{TreeNode}(0)$ with balanced subtrees.

---

## 4. Complete Execution Trace

```text
               Root 0 (mid=2)
              /              \
     Node -10 (mid=0)        Node 5 (mid=3)
           \                       \
        Node -3 (mid=1)         Node 9 (mid=4)
```

| Order of Construction | Interval $[L, R]$ | Mid $M$ | Subtree Action | Linked List Node Read | Advanced Next Cursor |
|:---:|:---:|:---:|:---|:---:|:---|
| 1 | $[0, -1]$ | - | Base empty left child | None | $\text{Node}(-10)$ |
| 2 | $[0, 1]$ | 0 | **Build Node -10** | $\text{Node}(-10)$ | $\text{Node}(-3)$ |
| 3 | $[1, 0]$ | - | Base empty child | None | $\text{Node}(-3)$ |
| 4 | $[1, 1]$ | 1 | **Build Node -3** | $\text{Node}(-3)$ | $\text{Node}(0)$ |
| 5 | $[2, 1]$ | - | Base empty child | None | $\text{Node}(0)$ |
| 6 | $[0, 4]$ | 2 | **Build Root 0** | $\text{Node}(0)$ | $\text{Node}(5)$ |
| 7 | $[3, 2]$ | - | Base empty child | None | $\text{Node}(5)$ |
| 8 | $[3, 4]$ | 3 | **Build Node 5** | $\text{Node}(5)$ | $\text{Node}(9)$ |
| 9 | $[4, 3]$ | - | Base empty child | None | $\text{Node}(9)$ |
| 10 | $[4, 4]$ | 4 | **Build Node 9** | $\text{Node}(9)$ | $\emptyset$ |
| Final | - | - | Complete Balanced Tree | - | **Return Root 0** |

### The Same Instance Under Tortoise-and-Hare Bisection

Before the recursion can create a node, the slow and fast pointers must agree on where the midpoint is. Walking them across $[-10, -3, 0, 5, 9]$ gives the following probe record:

| Pass | slow before $\to$ after | fast before $\to$ after | prev | Are `fast` and `fast.next` both non-empty? | What the iteration does |
|:---:|:---:|:---:|:---:|:---|:---|
| Start | $-10 \to -10$ | $-10 \to -10$ | $\emptyset$ | not tested yet | Both pointers are placed on the head node before the first test. |
| 1 | $-10 \to -3$ | $-10 \to 5$ | $-10$ | Yes: `fast` is $-10$ and `fast.next` is $-3$ | slow advances by one node while fast advances by two. |
| 2 | $-3 \to 0$ | $5 \to \emptyset$ | $-3$ | Yes: `fast` is $5$ and `fast.next` is $9$ | fast steps off the end, so slow has arrived at the true middle node. |
| Exit | $0$ (unchanged) | $\emptyset$ (unchanged) | $-3$ | No: `fast` is $\emptyset$ | The loop stops with slow on the median $0$ and prev on its predecessor $-3$. |

Severing happens only after the loop: the link from $-3$ to $0$ is cut, which splits the list into the disjoint sublists $[-10, -3]$ and $[5, 9]$. The median node $0$ becomes the current root, and the two sublists are handed to the two recursive calls. The complete call sequence is:

| Call Order | Current Sublist | slow Lands On (Root Value) | prev | Left Sublist After Severing | Right Sublist | Node Created |
|:---:|:---|:---:|:---:|:---|:---|:---|
| 1 | $[-10, -3, 0, 5, 9]$ | $0$ | $-3$ | $[-10, -3]$ | $[5, 9]$ | root $0$ |
| 2 | $[-10, -3]$ | $-3$ | $-10$ | $[-10]$ | $[\,]$ | left child of $0$, value $-3$ |
| 3 | $[-10]$ | $-10$ | $\emptyset$ | $[\,]$ (no severing is needed) | $[\,]$ | left child of $-3$, value $-10$, a leaf |
| 4 | $[5, 9]$ | $9$ | $5$ | $[5]$ | $[\,]$ | right child of $0$, value $9$ |
| 5 | $[5]$ | $5$ | $\emptyset$ | $[\,]$ (no severing is needed) | $[\,]$ | left child of $9$, value $5$, a leaf |

Reading the created nodes back in level order gives $[0, -3, 9, -10, \text{null}, 5]$: the root is $0$, its children are $-3$ and $9$, node $-3$ owns the single left child $-10$, node $9$ owns the single left child $5$, and the remaining child slots are empty. Both methods necessarily place a middle value at the root, but they need not agree on the rest of the shape. Method 2's lower-median index rule gave the left subtree $-10$ above $-3$, while severing at the slow pointer makes $-3$ the left child and $-10$ its child; both trees are valid height-balanced BSTs over the same values, which is why the representation is checked structurally rather than compared literally.

---

## 5. Algorithmic Correctness

**Soundness.** The inorder traversal of any BST visits nodes in strictly sorted non-decreasing order. By structuring the recursion tree so that $\text{curr}$ is evaluated strictly between its left and right subtree builds, the list values are read in natural sorted sequence, generating a BST that strictly maintains ordering and height balance.

**Completeness.** Midpoint bisection guarantees that the number of nodes allocated to left and right subtrees differs by at most 1 at every level, guaranteeing $|H_L - H_R| \le 1$ everywhere.

---

## 6. Traps This Instance Exposes

- **Failing to Sever in Slow/Fast Approach:** In Method 1, forgetting `prev.next = None` causes the left recursive call to traverse past the midpoint into the right half, resulting in infinite recursion.
- **Single Node List in Slow/Fast Approach:** When only one node remains (`head.next == None`), `prev` remains `None`. Handling `if prev: prev.next = None` prevents null pointer exceptions.
- **Inorder Simulation Head Advancement:** In Method 2, `curr` must be a mutable global reference (or stored in an object/nonlocal variable) so that recursive child frames advance the cursor for subsequent parent and sibling frames.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Inorder Simulation:** $O(N)$. Measuring length takes $N$ steps, and each tree node is created in $O(1)$ time during the single forward traversal.
  - **Slow/Fast Bisection:** $O(N \log N)$ as the list is repeatedly scanned to find medians across $\log N$ levels.
- **Auxiliary Space Complexity:** $O(\log N)$ recursion stack frames for balanced height $H = \lceil \log_2 N \rceil$.
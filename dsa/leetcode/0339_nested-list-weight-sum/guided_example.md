# Guided Example: Nested List Weight Sum

We trace the step-by-step recursive depth tracking, `NestedInteger` interface polymorphism (`isInteger()`, `getInteger()`, `getList()`), depth-scaled product accumulation ($\text{val} \times \text{depth}$), and hierarchical list aggregation on representative nested integer structures:

- **Input:** `nestedList = [[1, 1], 2, [1, 1]]`
- **Required output:** $10$
  - Elements at depth 1:
    - Single integer $2 \implies 2 \times 1 = 2$
  - Elements at depth 2:
    - First nested list `[1, 1]`: two integers of value $1 \implies (1 \times 2) + (1 \times 2) = 4$
    - Second nested list `[1, 1]`: two integers of value $1 \implies (1 \times 2) + (1 \times 2) = 4$
  - Total weighted sum: $2 + 4 + 4 = \mathbf{10}$
- **Deep Nesting Instance:** `nestedList = [1, [4, [6]]]`
  - $1$ at depth 1: $1 \times 1 = 1$
  - $4$ at depth 2: $4 \times 2 = 8$
  - $6$ at depth 3: $6 \times 3 = 18$
  - Total: $1 + 8 + 18 = 27$
- **Empty List Base Cases:**
  - `nestedList = [] \implies 0$
  - `nestedList = [[]] \implies 0$ (depth 2 list containing zero integers)

This instance demonstrates recursive depth-first traversal over recursive tree-like data structures, explains why top-level elements begin at `depth = 1`, proves how the call stack mirrors the nesting hierarchy without auxiliary flattening buffers, and analyzes $O(N)$ linear time and $O(D)$ recursion depth space bounds.

---

## 1. Instance & Teaching Goal

Given a nested list of integers:
$$
\text{nestedList} = [[1, 1], \; 2, \; [1, 1]]
$$
Each item in the list is a `NestedInteger` object that either holds a single integer or a nested list.
The **depth** of an integer is the number of enclosing lists it is contained within (the top-level list has depth 1).
Calculate the sum of each integer multiplied by its respective depth:
$$
\text{Total} = \sum_{\text{all integers } x} x \times \text{depth}(x)
$$

```text
Hierarchical Depth Structure:
Level 1 (depth = 1):
  [  ...  ,   2   ,  ...  ]   -> 2 * 1 = 2
    /               \
Level 2 (depth = 2):
 [1, 1]            [1, 1]     -> (1*2 + 1*2) + (1*2 + 1*2) = 8

Total Weighted Sum: 2 + 8 = 10
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Recursive Contract `dfs(nestedList, depth)`
- Input: A list of `NestedInteger` elements and their current `depth`.
- Initial Invocation: `dfs(nestedList, 1)`.
- Accumulator: `depth_sum = 0`.

### 2. Polymorphic Handling per Element:
For each `item` in `nestedList`:
1. **If `item.isInteger()` is True:**
   Retrieve the scalar integer value and weight it by the current depth:
   $$
   depth\_sum \mathrel{+}= item.\text{getInteger}() \times depth
   $$
2. **If `item.isInteger()` is False (Nested List):**
   Recurse on the child list with incremented depth ($depth + 1$):
   $$
   depth\_sum \mathrel{+}= dfs(item.\text{getList}(), \; depth + 1)
   $$

Return `depth_sum`.

> **Invariant.** At every call `dfs(list, depth)`, the parameter `depth` accurately reflects the exact nesting layer of all direct elements in `list`.

---

## 3. Step-by-Step Worked Execution

We trace `dfs([[1, 1], 2, [1, 1]], depth=1)`:

---

### Step 1: Element 0 (`item` is list `[1, 1]`)
- `item.isInteger()` is **False**.
- Recurse into child list: call `dfs([1, 1], depth=2)`.
  - Child call initialized: `depth_sum = 0`.
  - **Child Item 0:** `isInteger()` is True, value $= 1$.
    $$
    depth\_sum \mathrel{+}= 1 \times 2 = \mathbf{2}
    $$
  - **Child Item 1:** `isInteger()` is True, value $= 1$.
    $$
    depth\_sum \mathrel{+}= 1 \times 2 = \mathbf{2}
    $$
  - Child call completes and returns $2 + 2 = \mathbf{4}$.
- Top-level updates:
  $$
  depth\_sum = 0 + 4 = \mathbf{4}
  $$

---

### Step 2: Element 1 (`item` is integer `2`)
- `item.isInteger()` is **True**.
- Retrieve value: `item.getInteger() = 2`.
- Weight by current depth ($depth = 1$):
  $$
  depth\_sum \mathrel{+}= 2 \times 1 = \mathbf{2}
  $$
- Top-level accumulator:
  $$
  depth\_sum = 4 + 2 = \mathbf{6}
  $$

---

### Step 3: Element 2 (`item` is list `[1, 1]`)
- `item.isInteger()` is **False**.
- Recurse into child list: call `dfs([1, 1], depth=2)`.
  - Child call initialized: `depth_sum = 0`.
  - **Child Item 0:** value $1 \implies 1 \times 2 = 2$.
  - **Child Item 1:** value $1 \implies 1 \times 2 = 2$.
  - Child call completes and returns $2 + 2 = \mathbf{4}$.
- Top-level updates:
  $$
  depth\_sum = 6 + 4 = \mathbf{10}
  $$

---

### Step 4: Final Return
All 3 top-level elements processed.
Return total weighted sum:
$$
\mathbf{10}
$$

---

## 4. Complete Execution Trace

```text
dfs(nestedList=[[1, 1], 2, [1, 1]], depth=1):
  item 0: list [1, 1] -> call dfs([1, 1], depth=2)
    item 0: int 1 -> 1 * 2 = 2
    item 1: int 1 -> 1 * 2 = 2
    returns 4
  accumulator = 4

  item 1: int 2 -> 2 * 1 = 2
  accumulator = 4 + 2 = 6

  item 2: list [1, 1] -> call dfs([1, 1], depth=2)
    item 0: int 1 -> 1 * 2 = 2
    item 1: int 1 -> 1 * 2 = 2
    returns 4
  accumulator = 6 + 4 = 10

returns 10
```

| Traversal Frame | Element Inspected | Type | Value / Child | Depth Multiplier | Contribution | Frame Accumulator |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `dfs(..., 1)` | Element 0 | List | `[1, 1]` | - | `dfs([1, 1], 2)` | Pending |
| `dfs([1, 1], 2)` | Child 0 | Integer | 1 | 2 | $1 \times 2 = 2$ | 2 |
| `dfs([1, 1], 2)` | Child 1 | Integer | 1 | 2 | $1 \times 2 = 2$ | 4 |
| `dfs(..., 1)` | Element 0 (Resolved) | List | Return 4 | 1 | 4 | 4 |
| `dfs(..., 1)` | Element 1 | Integer | 2 | 1 | $2 \times 1 = 2$ | 6 |
| `dfs(..., 1)` | Element 2 | List | `[1, 1]` | - | `dfs([1, 1], 2)` | Pending |
| `dfs([1, 1], 2)` | Child 0 | Integer | 1 | 2 | $1 \times 2 = 2$ | 2 |
| `dfs([1, 1], 2)` | Child 1 | Integer | 1 | 2 | $1 \times 2 = 2$ | 4 |
| `dfs(..., 1)` | Element 2 (Resolved) | List | Return 4 | 1 | 4 | **10 (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** The interface guarantee provides that `item.isInteger()` distinguishes scalars from sublists. Multiplying each integer value strictly by its call parameter `depth` ensures that depth scaling matches the mathematical problem specification. Returning the sum of child calls preserves additive linearity across the entire tree hierarchy.

**Completeness.** The `for item in nestedList` loop iterates over every element in each list. Every nested sublist is entered recursively, ensuring that no integer, regardless of nesting depth, is omitted from the accumulation.

---

## 6. Traps This Instance Exposes

- **0-Indexed vs 1-Indexed Depth:** Starting recursion at `depth = 0` produces $0$ for top-level integers and undercounts all deeper layers by 1. The root list elements have depth 1.
- **Empty Nested Lists:** Elements like `[[]]` represent valid nested lists that contain zero integers. The code must gracefully iterate over empty child lists without failing or contributing to the sum.
- **Speculating on `NestedInteger` Class Internals:** Directly accessing non-existent attributes (e.g. `item.val` or `isinstance(item, list)`) fails because `NestedInteger` is an abstract interface. Always use `.isInteger()`, `.getInteger()`, and `.getList()`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total number of `NestedInteger` objects across all nesting levels. Every object (both integer-holding and list-holding) is visited exactly once.
- **Auxiliary Space Complexity:** $O(D)$, where $D$ is the maximum nesting depth of the list, representing the maximum call stack depth.

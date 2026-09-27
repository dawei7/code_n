# Guided Example: Mini Parser

We trace the step-by-step recursive grammar descent, bracket depth state tracking (`depth`), top-level comma delimiter splitting (`depth == 0 and s[i] == ','`), and hierarchical `NestedInteger` tree construction on representative serialized strings:

- **Input:** $s = \text{"[123, [456, [789]]]"}$
- **Required output:** `NestedInteger` representing $[123, [456, [789]]]$
  - Outer list level:
    - Child 1: substring `"123"` at depth 0 $\implies$ recurses to scalar integer `NestedInteger(123)`
    - Child 2: substring `"[456, [789]]"` at depth 0 $\implies$ recurses to nested list
  - Mid list level (`"[456, [789]]"`):
    - Child 1: `"456"` $\implies$ scalar integer `NestedInteger(456)`
    - Child 2: `"[789]"` $\implies$ nested list with single element `NestedInteger(789)`
  - Reassembled structure: `[123, [456, [789]]]`
- **Scalar Non-List Input:** $s = \text{"324"} \implies$ returns scalar `NestedInteger(324)`
- **Empty List Input:** $s = \text{"[]"} \implies$ returns empty list `NestedInteger()`
- **Negative Integers:** $s = \text{"[-1, 2]"} \implies$ handles `-` seamlessly via `int(s)`

This instance demonstrates recursive descent tokenization and parsing of context-free languages, mathematically proves why tracking bracket depth isolates top-level delimiter boundaries without splitting inner nested sub-lists, and derives $O(N)$ runtime and $O(D)$ recursion stack space bounds.

---

## 1. Instance & Teaching Goal

Given a serialized string $s = \text{"[123, [456, [789]]]"}$ representing a nested list of integers:
Deserialize the string into a hierarchical `NestedInteger` object conforming to the interface:
- `isInteger()`: returns True if holding a single integer, False if holding a list.
- `getInteger()`: returns the integer value.
- `getList()`: returns the list of `NestedInteger` elements.
- `add(elem)`: appends a child `NestedInteger` to this list object.

```text
Input String: "[123, [456, [789]]]"

Hierarchical Grammar Tree:
       [ List ]
      /        \
   123        [ List ]
             /        \
          456        [ List ]
                        |
                       789

Challenge: When scanning the outer list, the commas inside "[456, [789]]" must NOT
split the outer list. Only commas at depth 0 represent outer sibling boundaries!
```

---

## 2. Conceptual Foundation & Invariants

### 1. Base Cases (Terminal Rules):
1. **Empty String or List:**
   If `not s or s == '[]'`: return `NestedInteger()` (Empty list container).
2. **Scalar Integer:**
   If `s[0] != '['`: the substring contains no brackets and represents a single signed integer.
   Return `NestedInteger(int(s))`.

### 2. Recursive List Grammar & Depth Tracking:
When `s[0] == '['` and $s \ne \text{"[]"}$:
- The string represents a bracketed list `[ ... ]`.
- Strip the enclosing outer brackets by scanning $i$ from $1$ to $\text{len}(s) - 1$.
- Maintain:
  - `depth = 0`: Number of currently open bracket pairs inside this list level.
  - `j = 1`: Start index of the current unparsed child token.
- **Delimiter Rules:**
  - Encounter `'['`: $depth \leftarrow depth + 1$.
  - Encounter `']'`: $depth \leftarrow depth - 1$.
  - Encounter `','` or reaching the end $i = \text{len}(s) - 1$:
    If and only if $depth == 0$:
    - The substring $s[j \dots i - 1]$ is a complete child element.
    - Recurse: `ans.add(self.deserialize(s[j:i]))`.
    - Advance start pointer: $j \leftarrow i + 1$.

> **Invariant.** A comma at index $i$ separates immediate child elements of the current list if and only if $depth == 0$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"[123, [456, [789]]]"}$ ($N = 21$):

---

### Step 1: Outer Level Execution (`"[123, [456, [789]]]"`)
- Not empty, starts with `'['`.
- Create list container: `ans = NestedInteger()`.
- Initial pointers: $depth = 0, j = 1$.
- **Scan $i = 1 \dots 20$:**
  - $i = 1 \dots 3$: characters `'1'`, `'2'`, `'3'`.
  - $i = 4$: character is `','` and $depth == 0$!
    - Child slice: $s[j:i] = s[1:4] = \text{"123"}$.
    - Recurse: `deserialize("123")` $\implies$ returns `NestedInteger(123)`.
    - Attach: `ans.add(NestedInteger(123))`.
    - Advance: $j \leftarrow 4 + 1 = \mathbf{5}$.
  - $i = 5$: character `'['` $\implies depth \leftarrow 0 + 1 = \mathbf{1}$.
  - $i = 6 \dots 9$: characters `'4'`, `'5'`, `'6'`, `','` (ignored because $depth = 1 \ne 0$).
  - $i = 11$: character `'['` $\implies depth \leftarrow 1 + 1 = \mathbf{2}$.
  - $i = 15$: character `']'` $\implies depth \leftarrow 2 - 1 = \mathbf{1}$.
  - $i = 16$: character `']'` $\implies depth \leftarrow 1 - 1 = \mathbf{0}$.
  - $i = 17$: reaching closing bracket (last character of outer list, $i = 17$ in slice):
    - Condition $depth == 0$ and $i = \text{len}(s) - 1$ triggers!
    - Child slice: $s[5:17] = \text{"[456, [789]]"}$.
    - Recurse: `deserialize("[456, [789]]")`.
    - Attach returned child list to outer `ans`.
- Outer `ans` is complete and returned.

---

### Step 2: Inner Level Execution (`"[456, [789]]"`)
- Create sub-list container: `ans_sub = NestedInteger()`.
- Pointers: $depth = 0, j = 1$.
- At comma separating 456 ($i = 4, depth = 0$):
  - Slice: `"456"`.
  - Recurse: `deserialize("456")` $\implies$ returns `NestedInteger(456)`.
  - Attach: `ans_sub.add(NestedInteger(456))`.
  - $j \leftarrow 5$.
- At final closing bracket:
  - Slice: `"[789]"`.
  - Recurse: `deserialize("[789]")` $\implies$ returns sub-sub-list containing $789$.
  - Attach to `ans_sub`.
- Return `ans_sub`.

---

### Step 3: Innermost Level Execution (`"[789]"`)
- Create container `ans_inner = NestedInteger()`.
- $j = 1$.
- At end: slice `"789"` $\implies$ recurses to scalar `NestedInteger(789)`.
- Attach `NestedInteger(789)` to `ans_inner`.
- Return `ans_inner`.

---

## 4. Complete Execution Trace

```text
deserialize("[123, [456, [789]]]")
  ans = []
  i=4, s[4]=',', depth=0 -> add(deserialize("123")) -> [123]
  i=17, end of list, depth=0 -> add(deserialize("[456, [789]]"))
    deserialize("[456, [789]]")
      ans_sub = []
      i=4, s[4]=',', depth=0 -> add(deserialize("456")) -> [456]
      i=11, end of list, depth=0 -> add(deserialize("[789]"))
        deserialize("[789]")
          ans_inner = []
          i=4, end of list -> add(deserialize("789")) -> [789]
          return [789]
      return [456, [789]]
  return [123, [456, [789]]]
```

| Recursion Frame | Input String $s$ | Token Extracted | Child Type | Depth at Trigger | Action Taken |
|:---:|:---|:---|:---:|:---:|:---|
| Frame 1 (Outer) | `"[123, [456, [789]]]"` | `"123"` | Scalar Integer | 0 | `ans.add(123)` |
| Frame 2 (Mid) | `"[456, [789]]"` | `"456"` | Scalar Integer | 0 | `ans_sub.add(456)` |
| Frame 3 (Inner) | `"[789]"` | `"789"` | Scalar Integer | 0 | `ans_inner.add(789)` |
| **Result** | Root Object | - | Nested Structure | - | **`[123, [456, [789]]]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Every valid JSON-like serialized nested list has properly balanced bracket pairs. Because `depth` increments on `'['` and decrements on `']'`, `depth == 0` holds strictly when the scanner is between top-level siblings of the current list. Splitting only at `depth == 0` guarantees that child lists are parsed as intact atomic substrings.

**Completeness.** Every character between matching outer brackets is either part of a scalar number or part of a sub-list. The slice range $s[j:i]$ partitions the internal content completely, ensuring no token is skipped or discarded.

---

## 6. Traps This Instance Exposes

- **Global String Splitting on Commas:** Calling `s.split(',')` splits all nested inner lists indiscriminately, corrupting structure. Splitting must respect bracket nesting depth.
- **Empty List Case:** Serialized string `"[]"` must return an empty list `NestedInteger()`. Without the explicit `s == '[]'` check, the loop would attempt to slice $s[1:1]$ (empty string) and error.
- **Negative Integer Handling:** Substrings like `"-123"` have $s[0] == \text{'-'}$. Testing `s[0] != '['` correctly identifies negative numbers as scalar integers without misclassifying them as lists.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot D)$, where $N$ is the string length and $D$ is the maximum nesting depth. In the worst case, string slicing copies substrings at each level of recursion. (Can be implemented in strictly $O(N)$ using an explicit index pointer or iterative stack parser).
- **Auxiliary Space Complexity:** $O(D)$ recursion stack space, bounded by the maximum bracket nesting depth $D$.

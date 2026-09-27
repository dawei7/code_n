# Guided Example: Longest Absolute File Path

We trace the step-by-step indentation level parsing (`ident` via `\t`), ancestor chain directory stack maintenance (`len(stk) > ident \implies stk.pop()`), cumulative path length accumulation with `/` separators (`cur += stk[-1] + 1`), and maximum file path resolution on representative serialized file system trees:

- **Input:** `input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`
- **Required output:** `20`
  - Serialized entries and depth levels:
    1. `"dir"`: depth $0$, directory $\implies stk = [3]$ (`"dir"`)
    2. `"\tsubdir1"`: depth $1$, directory $\implies stk = [3, 11]$ (`"dir/subdir1"`)
    3. `"\tsubdir2"`: depth $1$, directory $\implies$ pop depth 1, push $11 \implies stk = [3, 11]$ (`"dir/subdir2"`)
    4. `"\t\tfile.ext"`: depth $2$, file (`.`) $\implies cur = 11 + 1 + 8 = 20$ (`"dir/subdir2/file.ext"`)
  - Longest absolute path length to any file: $\mathbf{20}$
- **Multi-Level Branching:** `input = "dir\n\tsubdir1\n\t\tfile1.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` $\implies 32$
- **No Files Present:** `input = "dir\n\tsubdir1\n\tsubdir2"` $\implies 0$ (Directories alone do not constitute file paths)
- **Root File:** `input = "a.txt"` $\implies 5$ (Root file length without `/`)

This instance demonstrates modeling hierarchical file tree structures with explicit ancestor stacks, mathematically proves why tracking cumulative scalar path lengths eliminates costly string concatenations, and derives $O(N)$ runtime and $O(D)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a string representing a file system where indentation (`\t`) indicates directory depth and newlines (`\n`) separate entries:
`input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`
Find the **length of the longest absolute path** to a **file** within the file system:

```text
Visual Directory Tree:
dir
 ├── subdir1
 └── subdir2
      └── file.ext

Reconstructed Absolute Paths:
- "dir/subdir1"           (Directory, ignored for final answer)
- "dir/subdir2/file.ext"  (File! Length = 3 + 1 + 7 + 1 + 8 = 20)

Max File Path Length: 20
```

### Cumulative Length Accounting vs String Concatenation
Reconstructing full path strings like `"dir/subdir2/file.ext"` through repeated string concatenation wastes time and memory copying prefixes.
Instead, we only need the **cumulative integer length** of directory paths at each depth:
$$
\text{path\_len} = \text{parent\_path\_len} + 1 \text{ (for '/')} + \text{name\_len}
$$

---

## 2. Conceptual Foundation & Invariants

### 1. The Indentation Stack:
- `stk`: A stack where `stk[d]` stores the cumulative absolute path length of the active directory at depth $d$.
- `ident`: Number of leading `\t` characters, defining the depth of the current line.

### 2. State Machine Transitions:
For each line:
1. **Depth Parsing:** Count leading `\t` characters $\implies ident$.
2. **Name & Type Extraction:** Scan until `\n` or end of string:
   - Compute character count `cur`.
   - If character is `.` $\implies isFile = True$.
3. **Stack Alignment (Backtracking Ancestors):**
   If `len(stk) > ident`:
   We have moved out of the previous subdirectories. Pop from `stk` until `len(stk) == ident`:
   $$
   \text{while } \text{len}(stk) > ident: \quad stk.\text{pop}()
   $$
4. **Cumulative Length Calculation:**
   If `len(stk) > 0`:
   Add parent directory path length plus 1 for the `/` separator:
   $$
   cur \leftarrow cur + stk[-1] + 1
   $$
5. **Update State:**
   - If `not isFile` (Directory):
     Push `cur` onto `stk` as the active directory at this depth.
   - If `isFile` (File):
     Update global maximum:
     $$
     ans \leftarrow \max(ans, \; cur)
     $$

> **Invariant.** At any step, `stk` stores precisely the cumulative path lengths of the direct ancestor directories of the current node from root down to depth $ident - 1$.

---

## 3. Step-by-Step Worked Execution

We trace `input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`:
Initial: $ans = 0, stk = []$.

---

### Step 1: Entry 1 (`"dir"`)
- Count tabs: no `\t` $\implies ident = 0$.
- Name: `"dir"`, length $cur = 3$, contains `.`? No $\implies isFile = False$.
- Stack pop: $\text{len}(stk) = 0 \le ident$. No pops.
- Parent addition: stack empty $\implies cur = 3$.
- Type: Directory $\implies stk.\text{append}(3)$.
- Stack state:
  $$
  stk = [3] \quad (\text{Path: "dir"})
  $$

---

### Step 2: Entry 2 (`"\tsubdir1"`)
- Count tabs: one `\t` $\implies ident = 1$.
- Name: `"subdir1"`, length $cur = 7$, contains `.`? No $\implies isFile = False$.
- Stack pop: $\text{len}(stk) = 1 \le ident (1)$. No pops.
- Parent addition: stack non-empty $\implies cur \mathrel{+}= stk[-1] + 1$:
  $$
  cur = 7 + 3 + 1 = \mathbf{11} \quad (\text{"dir/subdir1"})
  $$
- Type: Directory $\implies stk.\text{append}(11)$.
- Stack state:
  $$
  stk = [3, \; 11]
  $$

---

### Step 3: Entry 3 (`"\tsubdir2"`)
- Count tabs: one `\t` $\implies ident = 1$.
- Name: `"subdir2"`, length $cur = 7$, contains `.`? No $\implies isFile = False$.
- Stack pop: $\text{len}(stk) = 2 > ident (1)$!
  - `subdir1` has ended; pop from stack:
    $$
    stk.\text{pop}() \implies stk = [3]
    $$
- Parent addition: $cur \mathrel{+}= stk[-1] + 1$:
  $$
  cur = 7 + 3 + 1 = \mathbf{11} \quad (\text{"dir/subdir2"})
  $$
- Type: Directory $\implies stk.\text{append}(11)$.
- Stack state:
  $$
  stk = [3, \; 11]
  $$

---

### Step 4: Entry 4 (`"\t\tfile.ext"`)
- Count tabs: two `\t` $\implies ident = 2$.
- Name: `"file.ext"`, length $cur = 8$, contains `.`? Yes $\implies isFile = \mathbf{True}$.
- Stack pop: $\text{len}(stk) = 2 \le ident (2)$. No pops.
- Parent addition: $cur \mathrel{+}= stk[-1] + 1$:
  $$
  cur = 8 + 11 + 1 = \mathbf{20} \quad (\text{"dir/subdir2/file.ext"})
  $$
- Type: **File**!
  - Update global answer:
    $$
    ans = \max(0, \; 20) = \mathbf{20}
    $$
  - Do NOT push files onto directory stack.

---

### Step 5: Termination
Input exhausted. Return maximum file path length:
$$
\mathbf{20}
$$

---

## 4. Complete Execution Trace

```text
input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

Entry 1: "dir"
  ident=0, cur=3, isFile=False
  pop while len(stk) > 0 -> stk=[]
  stk.append(3) -> stk=[3]

Entry 2: "\tsubdir1"
  ident=1, cur=7, isFile=False
  pop while len(stk) > 1 -> none
  cur += stk[-1] + 1 = 7 + 3 + 1 = 11
  stk.append(11) -> stk=[3, 11]

Entry 3: "\tsubdir2"
  ident=1, cur=7, isFile=False
  pop while len(stk) > 1 -> pops 11 -> stk=[3]
  cur += stk[-1] + 1 = 7 + 3 + 1 = 11
  stk.append(11) -> stk=[3, 11]

Entry 4: "\t\tfile.ext"
  ident=2, cur=8, isFile=True
  pop while len(stk) > 2 -> none
  cur += stk[-1] + 1 = 8 + 11 + 1 = 20
  ans = max(0, 20) = 20

Return ans = 20
```

| Entry | Line Token | Depth $ident$ | Base Name Length | Is File? | Stack Before | Stack Action | Cumulative Length $cur$ | Global Max $ans$ |
|:---:|:---|:---:|:---:|:---:|:---|:---|:---:|:---:|
| 1 | `"dir"` | 0 | 3 | False | `[]` | Push 3 | 3 | 0 |
| 2 | `"\tsubdir1"` | 1 | 7 | False | `[3]` | Push 11 | 11 | 0 |
| 3 | `"\tsubdir2"` | 1 | 7 | False | `[3, 11]` | Pop 11, Push 11 | 11 | 0 |
| **4** | **`"\t\tfile.ext"`** | **2** | **8** | **True** | **`[3, 11]`** | **None (File)** | **20** | **$\mathbf{20}$ (Final)** |

---

## 5. Algorithmic Correctness

**Soundness.** Because the input represents a preorder traversal of a tree, an entry at depth $d$ is always a child of the most recently processed directory at depth $d - 1$. Popping directories at depth $\ge ident$ ensures that siblings and finished subtrees do not corrupt the parent path. Adding $stk[-1] + 1$ accounts exactly for the full parent directory prefix and the separating slash.

**Completeness.** Every entry in the serialized string is inspected. If a file exists, its full path length is calculated and considered for $ans$. If no file exists, $ans$ remains 0, satisfying the contract.

---

## 6. Traps This Instance Exposes

- **Directory vs File Path Accounting:** Only paths terminating in a **file** (containing a `.` character) qualify for $ans$. A deep directory tree with no files must return 0.
- **Root Files:** A file at depth 0 (e.g. `"file.ext"`) has $ident = 0$ and empty stack, so its length is simply the filename length without a leading slash.
- **Multiple Files in the Same Directory:** When multiple sibling files appear consecutively at depth $d$, neither should be pushed to the stack. Each computes its length using the same parent $stk[-1]$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the total length of the input string.
  - The pointer $i$ advances monotonically from $0$ to $N$.
  - Each character is inspected a constant number of times.
  - Each directory length is pushed and popped from `stk` at most once.
  - Overall time is strictly linear $O(N)$.
- **Auxiliary Space Complexity:** $O(D)$, where $D$ is the maximum directory depth, storing cumulative lengths in the stack `stk` ($D \le N$).

# Guided Example: Find Duplicate File in System

We trace the step-by-step directory path tokenization, file entry lexical parsing (`filename(content)`), content inverted index mapping ($content \to [path_1, path_2, \dots]$), canonical path concatenation ($dir + \text{"/"} + filename$), multi-instance duplicate cluster filtering ($|group| > 1$), and single-instance file omission on representative filesystem snapshots:

- **Input:**
  $$
  paths = [
    \text{"root/a 1.txt(abcd) 2.txt(efgh)"},
    \text{"root/c 3.txt(abcd)"},
    \text{"root/c/d 4.txt(efgh)"},
    \text{"root 4.txt(efgh)"}
  ]
  $$
- **Required output:**
  $$
  [
    [\text{"root/a/1.txt"}, \; \text{"root/c/3.txt"}],
    [\text{"root/a/2.txt"}, \; \text{"root/c/d/4.txt"}, \; \text{"root/4.txt"}]
  ]
  $$
  *(Order of groups and order within groups may appear in any permutation)*.
  - Contract & Duplicate definition:
    - Files are duplicates if and only if they share the **exact same textual content**.
    - Filenames and directory paths do not matter for equality; only file contents matter.
    - A duplicate group must contain **at least two files** ($|group| \ge 2$). Unique files that do not collide with any other file are excluded.
- **Inverted Index Hash Architecture ($d[\text{content}] \to [\text{paths}]$):**
  - Construct a hash map $d$ where:
    - **Key:** The raw file content string extracted between the parentheses `(...)`.
    - **Value:** A list of complete, canonical filesystem paths (`"dir/filename"`).
  - As we parse each file:
    $$
    d[content].\text{append}(dir + \text{"/"} + filename)
    $$
  - After processing all directories, filter the hash map values:
    $$
    \{v \mid v \in d.\text{values}(), \; |v| > 1\}
    $$
- **Step-by-Step Worked Parsing & Indexing Trace:**
  - Initialize empty hash table $d = \{\}$.
  - **Directory Entry 1 (`"root/a 1.txt(abcd) 2.txt(efgh)"`):**
    - Split tokens by whitespace:
      - Directory prefix: $dir = \text{"root/a"}$.
      - File token 1: `"1.txt(abcd)"`
        - Filename: `"1.txt"`, Content: `"abcd"`.
        - Canonical path: `"root/a/1.txt"`.
        - Append to $d[\text{"abcd"}]$:
          $$
          d[\text{"abcd"}] = [\text{"root/a/1.txt"}]
          $$
      - File token 2: `"2.txt(efgh)"`
        - Filename: `"2.txt"`, Content: `"efgh"`.
        - Canonical path: `"root/a/2.txt"`.
        - Append to $d[\text{"efgh"}]$:
          $$
          d[\text{"efgh"}] = [\text{"root/a/2.txt"}]
          $$
  - **Directory Entry 2 (`"root/c 3.txt(abcd)"`):**
    - Directory prefix: $dir = \text{"root/c"}$.
    - File token: `"3.txt(abcd)"`
      - Filename: `"3.txt"`, Content: `"abcd"`.
      - Canonical path: `"root/c/3.txt"`.
      - Content `"abcd"` already exists in $d$!
      - Append path:
        $$
        d[\text{"abcd"}] = [\text{"root/a/1.txt"}, \; \text{"root/c/3.txt"}]
        $$
  - **Directory Entry 3 (`"root/c/d 4.txt(efgh)"`):**
    - Directory prefix: $dir = \text{"root/c/d"}$.
    - File token: `"4.txt(efgh)"`
      - Filename: `"4.txt"`, Content: `"efgh"`.
      - Canonical path: `"root/c/d/4.txt"`.
      - Append path:
        $$
        d[\text{"efgh"}] = [\text{"root/a/2.txt"}, \; \text{"root/c/d/4.txt"}]
        $$
  - **Directory Entry 4 (`"root 4.txt(efgh)"`):**
    - Directory prefix: $dir = \text{"root"}$.
    - File token: `"4.txt(efgh)"`
      - Filename: `"4.txt"`, Content: `"efgh"`.
      - Canonical path: `"root/4.txt"`.
      - Append path:
        $$
        d[\text{"efgh"}] = [\text{"root/a/2.txt"}, \; \text{"root/c/d/4.txt"}, \; \text{"root/4.txt"}]
        $$
  - **Step 5: Filter Duplicate Groups ($|group| > 1$):**
    - Group for `"abcd"`:
      - Paths: `["root/a/1.txt", "root/c/3.txt"]`
      - Size $2 > 1 \implies \mathbf{Retain}$
    - Group for `"efgh"`:
      - Paths: `["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]`
      - Size $3 > 1 \implies \mathbf{Retain}$
  - Final Output:
    $$
    [[\text{"root/a/1.txt"}, \text{"root/c/3.txt"}], \; [\text{"root/a/2.txt"}, \text{"root/c/d/4.txt"}, \text{"root/4.txt"}]]
    $$
- **Unique File Filtering Instance:**
  - Suppose a file `"root/z 9.txt(unique)"` was also processed.
  - Its list has size $|d[\text{"unique"}]| = 1$.
  - Filter condition $|v| > 1$ excludes it, keeping output restricted strictly to true duplicates.
- **Empty Duplicate List:**
  - If all files across the entire file system have unique content, return `[]`.

This instance demonstrates inverted indexing over hierarchical path taxonomies, mathematically proves why content-keyed multi-maps identify equivalence classes under relational projection, and derives $O(N \cdot L)$ runtime and $O(N \cdot L)$ space bounds.

---

## 1. Instance & Teaching Goal

Given directory listings containing files and their parenthesized contents:
Group files by identical content and return all groups with **size $\ge 2$**.

```text
Input:
  "root/a 1.txt(abcd) 2.txt(efgh)"
  "root/c 3.txt(abcd)"
  "root/c/d 4.txt(efgh)"
  "root 4.txt(efgh)"

Content Inverted Index:
  "abcd" -> ["root/a/1.txt", "root/c/3.txt"]               (Count = 2, Duplicate!)
  "efgh" -> ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"] (Count = 3, Duplicate!)

Output:
  [["root/a/1.txt", "root/c/3.txt"], ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]]
```

### Key Insight: Content-Keyed Equivalence Classes
- Two files are duplicates if and only if their contents are character-by-character identical.
- By using the file content as the hash map key and the full canonical file path as the value list, we naturally partition all files into equivalence classes.
- A simple filter `len(group) > 1` isolates all duplicate clusters.

---

## 2. Conceptual Foundation & Invariants

### 1. Token Splitting:
- For each directory string $P$:
  - Split by space into $[dir, entry_1, entry_2, \dots]$.
  - For each entry:
    - Split at the first `'('` into $name$ and $content$.
    - Build full path: $dir + \text{"/"} + name$.
    - Add to hash map: $d[content].\text{append}(path)$.

### 2. The Duplicate Condition:
$$
\text{Result} = [paths \text{ for } paths \in d.\text{values}() \text{ if } |paths| \ge 2]
$$

> **Equivalence Partition Invariant.** Grouping files by hash of content defines an equivalence relation where files in the same bucket have equivalent content, and buckets of cardinality $\ge 2$ represent duplicates.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Parse and Populate Map
- `root/a 1.txt(abcd)` $\to d[\text{"abcd"}] = [\text{"root/a/1.txt"}]$
- `root/a 2.txt(efgh)` $\to d[\text{"efgh"}] = [\text{"root/a/2.txt"}]$
- `root/c 3.txt(abcd)` $\to d[\text{"abcd"}].\text{append}(\text{"root/c/3.txt"})$
- `root/c/d 4.txt(efgh)` $\to d[\text{"efgh"}].\text{append}(\text{"root/c/d/4.txt"})$
- `root 4.txt(efgh)` $\to d[\text{"efgh"}].\text{append}(\text{"root/4.txt"})$

---

### Step 2: Inspect Group Cardinalities
- Key `"abcd"`: 2 paths $\ge 2 \implies$ **Include**.
- Key `"efgh"`: 3 paths $\ge 2 \implies$ **Include**.

---

### Step 3: Format Result
$$
[[\text{"root/a/1.txt"}, \text{"root/c/3.txt"}], \; [\text{"root/a/2.txt"}, \text{"root/c/d/4.txt"}, \text{"root/4.txt"}]]
$$

---

## 4. Complete Execution Trace

| Directory Prefix | File Token | Extracted Filename | Extracted Content | Full Path Appended | Bucket Size |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `root/a` | `1.txt(abcd)` | `1.txt` | `"abcd"` | `root/a/1.txt` | $1$ |
| `root/a` | `2.txt(efgh)` | `2.txt` | `"efgh"` | `root/a/2.txt` | $1$ |
| `root/c` | `3.txt(abcd)` | `3.txt` | `"abcd"` | `root/c/3.txt` | **$2$** (Duplicate!) |
| `root/c/d` | `4.txt(efgh)` | `4.txt` | `"efgh"` | `root/c/d/4.txt` | **$2$** (Duplicate!) |
| `root` | `4.txt(efgh)` | `4.txt` | `"efgh"` | `root/4.txt` | **$3$** (Duplicate!) |

---

## 5. Boundary Cases & Failure Modes

- **Directory with No Files (`"root/a"`):** Split array has length 1; loop over files does not run.
- **No Duplicate Files in System:** All buckets have size 1 $\implies$ returns `[]`.
- **Files in Same Directory with Same Name:** Impossible by filesystem contract; duplicate content always has distinct paths.
- **Deeply Nested Paths (`"a/b/c/d/e/f file.txt(content)"`):** Handled with standard string join.

---

## 6. Traps & Common Anti-Patterns

- **Including Groups of Size 1:** Returning a single file that has no duplicate violates the problem definition. Only include groups where `len(v) > 1`.
- **Using Full Path as Key Instead of Content:** Grouping by filename or path is incorrect; files with completely different names (e.g. `1.txt` and `3.txt`) are duplicates if their contents match.
- **Regex Overhead on High Volume:** Calling complex regular expressions for each token is much slower than direct string slicing (`f.find('(')`).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be total number of files and $L$ be the maximum string length of a file path/content.
  - Splitting strings and hashing content: $\mathcal{O}(N \cdot L)$ time.
  - Filtering duplicate lists: $\mathcal{O}(U)$ where $U \le N$ is the number of distinct contents.
  - Total Time: strictly linear $\mathcal{O}(N \cdot L)$. Completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N \cdot L)$ space to store the inverted index hash table.

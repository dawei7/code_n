# Guided Example: Simplify Path

We trace the step-by-step Unix file path canonicalization using a directory token stack on representative path instances:

- **Input:** $\text{path} = \text{"/a/./b/../../c/"}$
- **Required output:** $\text{"/c"}$
- **Boundary Root Pop:** $\text{"/../"} \implies \text{"/"}$
- **Consecutive Slashes:** $\text{"/home//foo/"} \implies \text{"/home/foo"}$

This instance demonstrates splitting paths by slash delimiters, ignoring empty tokens and current directory markers (`"."`), handling parent directory navigation (`".."`) via stack pop operations with root boundary safety, and formatting the canonical Unix path string.

---

## 1. Instance & Teaching Goal

Given an absolute Unix-style file path string $\text{path}$, transform it into its simplified canonical path.

The canonical path rules require that:
1. The path starts with a single slash `'/'`.
2. Any two directories are separated by exactly one slash `'/'`.
3. The path does not end with a trailing `'/'` (unless it is the root directory `"/"`).
4. Current directory symbols `"."` are omitted.
5. Parent directory symbols `".."` pop the immediately preceding directory. Navigating up from root `"/"` remains at `"/"`.
6. Multiple consecutive slashes (e.g. `"//"`) are treated as a single separator.

Using a Last-In, First-Out (LIFO) stack of directory strings naturally models recursive folder entry (push) and parent traversal (pop) in $O(N)$ time.

---

## 2. Conceptual Foundation & Invariants

### Tokenization and Stack Transitions
1. **Tokenize:** Split $\text{path}$ on delimiter `'/'`:
   $$
   \text{tokens} = \text{path.split('/')}
   $$
2. **Process Tokens:**
   Initialize an empty list $\text{stack} = []$.
   For each token $T \in \text{tokens}$:
   - If $T == \text{""}$ (consecutive or boundary slashes): Ignore.
   - If $T == \text{"."}$ (reference to current directory): Ignore.
   - If $T == \text{".."}$ (reference to parent directory):
     - If $\text{stack}$ is non-empty: $\text{stack.pop()}$.
     - If $\text{stack}$ is empty: remain at root (no-op).
   - Else: $T$ is a valid directory or file name (e.g. `"a"`, `"..."`, `"my_folder"`):
     - $\text{stack.append}(T)$.

3. **Reconstruct Canonical String:**
   Join the stack with single slashes and prepend the root slash:
   $$
   \text{canonical} = \text{"/"} + \text{"/".join}(\text{stack})
   $$

> **Invariant.** At every token $T$, `stack` contains the exact sequence of valid directory names representing the current working directory relative to root.

---

## 3. Step-by-Step Worked Execution

We trace $\text{path} = \text{"/a/./b/../../c/"}$:

### Tokenization
Splitting by `'/'` yields 8 tokens:
$$
[\text{""}, \, \text{"a"}, \, \text{"."}, \, \text{"b"}, \, \text{".."}, \, \text{".."}, \, \text{"c"}, \, \text{""}]
$$

---

### Step-by-Step Stack Processing
- **Token 0 (`""`):** Empty string from leading slash. Ignored. Stack: `[]`.
- **Token 1 (`"a"`):** Directory name. Push onto stack.
  - Stack: `['a']`.
- **Token 2 (`"."`):** Current directory marker. Ignored.
  - Stack: `['a']`.
- **Token 3 (`"b"`):** Directory name. Push onto stack.
  - Stack: `['a', 'b']`.
- **Token 4 (`".."`):** Parent directory marker.
  - Action: Pop top directory (`"b"`).
  - Stack: `['a']`.
- **Token 5 (`".."`):** Parent directory marker.
  - Action: Pop top directory (`"a"`).
  - Stack: `[]`.
- **Token 6 (`"c"`):** Directory name. Push onto stack.
  - Stack: `['c']`.
- **Token 7 (`""`):** Empty string from trailing slash. Ignored.
  - Stack: `['c']`.

---

### Path Reassembly
- Remaining directories in stack: `['c']`.
- Join with slashes: $\text{"/"} + \text{"/".join}([\text{"c"}]) = \text{"/c"}$.

Emitted result: `"/c"`.

### A Second Instance: Dots That Are Names, Not Operators

Re-running the same token loop on $\text{path} = \text{"/.../a/./b/../../c/"}$ isolates the literal-name trap, because `"..."` must be pushed while `".."` must pop:

| Token index | Token | Classification | Stack action | Stack after | Depth |
|:---:|:---:|:---|:---|:---|:---:|
| 0 | `""` | Empty from the leading slash | Skip | `[]` | 0 |
| 1 | `"..."` | Directory name (not the parent operator) | Push `"..."` | `['...']` | 1 |
| 2 | `"a"` | Directory name | Push `"a"` | `['...', 'a']` | 2 |
| 3 | `"."` | Current directory | Skip | `['...', 'a']` | 2 |
| 4 | `"b"` | Directory name | Push `"b"` | `['...', 'a', 'b']` | 3 |
| 5 | `".."` | Parent directory | Pop `"b"` | `['...', 'a']` | 2 |
| 6 | `".."` | Parent directory | Pop `"a"` | `['...']` | 1 |
| 7 | `"c"` | Directory name | Push `"c"` | `['...', 'c']` | 2 |
| 8 | `""` | Empty from the trailing slash | Skip | `['...', 'c']` | 2 |

Reassembly gives `"/"` followed by the joined stack `".../c"`, that is `"/.../c"`. Both `".."` tokens in this instance were absorbed by pops rather than by the root guard, so the same code path serves tokens 5 and 6 here and tokens 4 and 5 of the main trace.

---

## 4. Complete Execution Trace

| Token Index | Token Extracted | Token Classification | Condition Evaluated | Stack Action | Stack State After Step |
|:---:|:---:|:---:|:---|:---|:---|
| 0 | `""` | Empty (Leading slash) | $T \in \{\text{""}, \text{"."}\}$ | Skip | `[]` |
| 1 | `"a"` | Directory name | Valid directory | Push `"a"` | `['a']` |
| 2 | `"."` | Current directory | $T == \text{"."}$ | Skip | `['a']` |
| 3 | `"b"` | Directory name | Valid directory | Push `"b"` | `['a', 'b']` |
| 4 | `".."` | Parent directory | $T == \text{".."}$ | Pop `"b"` | `['a']` |
| 5 | `".."` | Parent directory | $T == \text{".."}$ | Pop `"a"` | `[]` |
| 6 | `"c"` | Directory name | Valid directory | Push `"c"` | `['c']` |
| 7 | `""` | Empty (Trailing slash) | $T \in \{\text{""}, \text{"."}\}$ | Skip | `['c']` |
| Format | - | Assembly | `"/" + "/".join(stack)` | Join | **`"/c"`** |

---

## 5. Algorithmic Correctness

**Soundness.** Every valid file path is a tree traversal rooted at `"/"`. A child directory descends one level (`push`), and a parent reference moves up one level (`pop`). Popping from an empty stack is a no-op because the root directory has no parent. Joining stack components with `"/"` guarantees single delimiters and avoids trailing slashes.

**Completeness.** String splitting divides the entire path into exhaustive non-overlapping tokens. Every token is classified and processed in linear sequence, ensuring all navigational modifiers are fully evaluated.

---

## 6. Traps This Instance Exposes

- **Popping from Root (`"/../"`):** If the stack is empty, encountering `".."` must not raise an `IndexError`. Checking `if stack: stack.pop()` safely absorbs root-level parent requests.
- **Valid Name With Dots (`"..."` or `".hidden"`):** Only exact strings `"."` and `".."` represent navigational operators. Names like `"..."` or `"..hidden"` are valid file/folder names and must be pushed onto the stack.
- **Empty Stack Formatting:** If the stack is empty after all tokens are processed (e.g. `path = "/a/.."`), returning `"/" + "/".join([])` correctly produces `"/"` rather than an empty string `""`.

Each canonicalization rule is pinned by a concrete instance, and in every case the observable output follows from the stack state alone:

| Instance | Input path | Terminal stack | Expected output | Rule that produces it |
|:---|:---|:---|:---|:---|
| Remove trailing separator | `/home/` | `['home']` | `/home` | The empty token after the final slash is skipped, so no trailing `'/'` is emitted. |
| Repeated separators | `/home//foo/` | `['home', 'foo']` | `/home/foo` | The empty token produced by `"//"` is skipped, collapsing the double slash to one. |
| Parent component | `/home/user/Documents/../Pictures` | `['home', 'user', 'Pictures']` | `/home/user/Pictures` | One pop removes exactly the most recent directory, `"Documents"`. |
| Parent at root | `/../` | `[]` | `/` | The `".."` meets an empty stack, so the root guard absorbs it and formatting yields `"/"`. |
| Above root | `/../../..` | `[]` | `/` | Three consecutive `".."` tokens are all absorbed; the depth never drops below $0$. |
| Literal dots | `/.../a/./b/../../c/` | `['...', 'c']` | `/.../c` | `"..."` is a name and is pushed; only the exact string `".."` pops. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of $\text{path}$. Splitting the string takes $O(N)$ time, and iterating through tokens takes $O(N)$ operations with $O(1)$ push/pop actions per token.
- **Auxiliary Space Complexity:** $O(N)$ to store the tokens list and directory stack.

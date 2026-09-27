# Guided Example: Palindrome Partitioning

We trace the step-by-step backtracking decision tree and palindrome prefix verification on representative string partitioning instances:

- **Input:** $s = \text{"aab"}$
- **Required output:** `[["a", "a", "b"], ["aa", "b"]]`
- **Single-Character Base:** $s = \text{"a"} \implies [[\text{"a"}]]$

This instance demonstrates exploring string partition cuts via depth-first backtracking, precomputing or dynamically verifying palindrome substrings in $O(1)$ time ($s[i \dots j]$ is palindromic if $s[i] == s[j] \land s[i+1 \dots j-1]$ is palindromic), pruning non-palindrome branches early, and executing state rollback with `path.pop()`.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"aab"}$, partition $s$ such that every substring in the partition is a palindrome. Return all possible valid palindrome partitionings.

There are $2^{N-1} = 2^{3-1} = 4$ ways to partition a 3-letter string:
1. `["a", "a", "b"]`: `'a'`, `'a'`, and `'b'` are all single-letter palindromes $\implies$ **Valid!**
2. `["aa", "b"]`: `'aa'` is a 2-letter palindrome, `'b'` is a palindrome $\implies$ **Valid!**
3. `["a", "ab"]`: `'ab'` is not a palindrome $\implies$ **Rejected.**
4. `["aab"]`: `'aab'` is not a palindrome $\implies$ **Rejected.**
Output: `[["a", "a", "b"], ["aa", "b"]]`.

A naive brute-force partitioner generates all $2^{N-1}$ partitions and tests each substring afterwards.
Backtracking prunes invalid branches early: as soon as a proposed prefix substring `s[start:end]` fails the palindrome test, the entire subtree of cuts rooted at `end` is discarded immediately, avoiding unnecessary recursive descent.

---

## 2. Conceptual Foundation & Invariants

### Backtracking DFS with Palindrome Gating
Let $N = |s|$.
Maintain a dynamic list `path` storing the current sequence of palindrome substrings.
Define recursive search $\text{dfs}(\text{start})$:

1. **Terminal Success Base Case:**
   If $\text{start} == N$:
   All characters have been consumed into valid palindromes.
   $$
   \text{results.append}(\text{list}(\text{path}))
   $$
2. **Explore Forward Cut Positions:**
   For $\text{end}$ from $\text{start} + 1$ to $N$:
   - Let candidate substring be $\text{sub} = s[\text{start} : \text{end}]$.
   - **Palindrome Gate:**
     If $\text{isPalindrome}(\text{sub})$:
     - Push: $\text{path.append}(\text{sub})$
     - Recurse: $\text{dfs}(\text{end})$
     - Backtrack Rollback: $\text{path.pop()}$
   - If $\text{sub}$ is not a palindrome, prune this branch and continue loop.

### 2D Palindrome Lookup Table ($O(1)$ Query)
To avoid $O(L)$ palindrome checks, precompute an $N \times N$ boolean table $\text{is\_pal}[i][j]$:
$$
\text{is\_pal}[i][j] = (s[i] == s[j]) \land (j - i \le 2 \lor \text{is\_pal}[i + 1][j - 1])
$$

> **Invariant.** At depth $d$, every substring currently residing in `path` is guaranteed to be a valid palindrome, and their concatenation equals $s[0 \dots \text{start}-1]$.

---

## 3. Step-by-Step Worked Execution

We trace the backtracking search tree on $s = \text{"aab"}$ ($N = 3$, indices $0, 1, 2$):

### Root Call: $\text{dfs}(\text{start} = 0)$

#### Branch 1: Cut at $\text{end} = 1$ ($\text{sub} = s[0:1] = \text{"a"}$)
- $\text{"a"}$ is a palindrome.
- Push: `path = ["a"]`.
- Recurse: $\text{dfs}(\text{start} = 1)$.

  - **Sub-Branch 1.1: Cut at $\text{end} = 2$ ($\text{sub} = s[1:2] = \text{"a"}$)**
    - $\text{"a"}$ is a palindrome.
    - Push: `path = ["a", "a"]`.
    - Recurse: $\text{dfs}(\text{start} = 2)$.
      - Cut at $\text{end} = 3$ ($\text{sub} = s[2:3] = \text{"b"}$):
        - $\text{"b"}$ is a palindrome.
        - Push: `path = ["a", "a", "b"]`.
        - Recurse: $\text{dfs}(\text{start} = 3)$.
          - $\text{start} == 3 == N \implies$ **Terminal Match 1!**
          - Capture snapshot: `results.append(["a", "a", "b"])`.
        - Pop: `path = ["a", "a"]`.
    - Pop: `path = ["a"]`.

  - **Sub-Branch 1.2: Cut at $\text{end} = 3$ ($\text{sub} = s[1:3] = \text{"ab"}$)**
    - Check palindrome: $\text{"ab"}$ is **not** a palindrome ($'a' \ne 'b'$).
    - **Pruned!** No recursive call made.

- Pop: `path = []`.

---

#### Branch 2: Cut at $\text{end} = 2$ ($\text{sub} = s[0:2] = \text{"aa"}$)
- $\text{"aa"}$ is a palindrome ($'a' == 'a'$).
- Push: `path = ["aa"]`.
- Recurse: $\text{dfs}(\text{start} = 2)$.
  - Cut at $\text{end} = 3$ ($\text{sub} = s[2:3] = \text{"b"}$):
    - $\text{"b"}$ is a palindrome.
    - Push: `path = ["aa", "b"]`.
    - Recurse: $\text{dfs}(\text{start} = 3)$.
      - $\text{start} == 3 == N \implies$ **Terminal Match 2!**
      - Capture snapshot: `results.append(["aa", "b"])`.
    - Pop: `path = ["aa"]`.
- Pop: `path = []`.

---

#### Branch 3: Cut at $\text{end} = 3$ ($\text{sub} = s[0:3] = \text{"aab"}$)
- Check palindrome: $\text{"aab"}$ is **not** a palindrome ($s[0] \ne s[2]$).
- **Pruned!** No recursive call made.

Search finishes.
Returned partitions: `[["a", "a", "b"], ["aa", "b"]]`.

---

## 4. Complete Execution Trace

### Decision Tree of Partition Cuts

```text
                               start=0 (s="aab")
                       /               |               \
             sub="a" [Valid]     sub="aa" [Valid]   sub="aab" [PRUNED]
                   /                   |
             start=1                 start=2
             /     \                    |
      sub="a"       sub="ab"         sub="b" [Valid]
      [Valid]       [PRUNED]            |
        |                            start=3
      start=2                      [SNAPSHOT 2: ["aa","b"]]
        |
      sub="b" [Valid]
        |
      start=3
   [SNAPSHOT 1: ["a","a","b"]]
```

| Traversal Step | Active Interval $[\text{start}, \text{end})$ | Substring Candidate | Palindrome? | Path State Before Call | Action Taken | Emitted Partition |
|:---:|:---:|:---:|:---:|:---|:---|:---:|
| 1 | $[0, 1)$ | `"a"` | Yes | `[]` | Recurse to $\text{start}=1$ | - |
| 1.1 | $[1, 2)$ | `"a"` | Yes | `["a"]` | Recurse to $\text{start}=2$ | - |
| 1.1.1 | $[2, 3)$ | `"b"` | Yes | `["a", "a"]` | Recurse to $\text{start}=3$ | - |
| **1.1.1.1** | $[3, 3)$ | Base ($\text{start}=3$) | - | `["a", "a", "b"]` | **Capture Snapshot** | `["a", "a", "b"]` |
| 1.2 | $[1, 3)$ | `"ab"` | **No** | `["a"]` | **Pruned (Skip)** | - |
| 2 | $[0, 2)$ | `"aa"` | Yes | `[]` | Recurse to $\text{start}=2$ | - |
| 2.1 | $[2, 3)$ | `"b"` | Yes | `["aa"]` | Recurse to $\text{start}=3$ | - |
| **2.1.1** | $[3, 3)$ | Base ($\text{start}=3$) | - | `["aa", "b"]` | **Capture Snapshot** | `["aa", "b"]` |
| 3 | $[0, 3)$ | `"aab"` | **No** | `[]` | **Pruned (Skip)** | - |

### Palindromic Substring Table for $s = \text{"aab"}$

The recurrence $\text{is\_pal}[i][j] = (s[i] == s[j]) \land (j - i \le 2 \lor \text{is\_pal}[i + 1][j - 1])$ is evaluated from the main diagonal outward, so every dependency is ready before it is needed.

| Fill order | Cell(s) $(i, j)$ | Span $j - i$ | Value | Dependency and reason |
|:---:|:---:|:---:|:---:|:---|
| 1 | $(0, 0)$, $(1, 1)$, $(2, 2)$ | 0 | $\text{True}$ | Initialized directly: a single character is always a palindrome and has no dependency. |
| 2 | $(1, 2)$ | 1 | $\text{False}$ | $s[1] = \text{'a'} \ne s[2] = \text{'b'}$, so the span rule is never consulted. |
| 3 | $(0, 1)$ | 1 | $\text{True}$ | $s[0] = s[1] = \text{'a'}$ and the span $1 \le 2$ means there is no interior left to verify. |
| 4 | $(0, 2)$ | 2 | $\text{False}$ | $s[0] = \text{'a'} \ne s[2] = \text{'b'}$, so the interior value $\text{is\_pal}[1][1]$ is never read. |

Only cell $(0, 1)$ among the spans of length at least $1$ is `True`, which is exactly why the search accepts the first cuts $[0, 1)$ and $[0, 2)$ and prunes the cut $[0, 3)$.

---

## 5. Algorithmic Correctness

**Soundness.** A partition is emitted if and only if $\text{start}$ reaches $N$ through a sequence of successful palindrome tests. By induction, every token in `path` was individually checked and confirmed to be a palindrome, so any recorded partition meets all constraints.

**Completeness.** The loop over `end` from $\text{start} + 1 \dots N$ checks all possible first cuts for the remaining suffix. Backtracking explores all valid branches without omission.

---

## 6. Traps This Instance Exposes

- **Deep Copy Requirement on Base Case:** Storing `results.append(path)` stores a reference to the mutable list. When backtracking rolls back to the root, `path` becomes empty, ruining the results. Using `results.append(list(path))` is required.
- **Forgetting to Backtrack:** Omitting `path.pop()` causes previously explored tokens to contaminate alternate sibling branches.
- **Repeated Substring Reversal Overhead:** Calling `sub == sub[::-1]` inside the loop takes $O(L)$ time per check. For longer strings ($N \le 16$), precomputing the 2D boolean palindrome table reduces each check to $O(1)$.

### Boundary and Degenerate Instances

| Instance | Input condition | Expected | Why the search produces it |
|:---|:---|:---|:---|
| $s = \text{"aab"}$ | Two valid cut patterns and two pruned ones | `[["a", "a", "b"], ["aa", "b"]]` | The cuts $[1, 3)$ and $[0, 3)$ fail the palindrome gate; the surviving routes reach $\text{start} = 3$ and are captured. |
| $s = \text{"a"}$ | A single character, $N = 1$ | `[["a"]]` | The root loop offers only the cut $[0, 1)$, whose substring is trivially palindromic, so the recursion reaches $\text{start} = 1 = N$ immediately. |
| $s = \text{"efe"}$ | The whole string is itself a palindrome | `[["e", "f", "e"], ["efe"]]` | Cuts are tried shortest first, so the singleton route is emitted before the whole-string route; the intermediate cuts `"ef"` and `"fe"` are rejected. |
| $s = \text{"abc"}$ | No substring of length at least $2$ is a palindrome | `[["a", "b", "c"]]` | Every multi-character candidate fails the gate, so the only surviving route is the three-singleton partition. |
| $s = \text{"aaa"}$ | Every substring is a palindrome | All four cut patterns | Each of the $2^{3-1} = 4$ ways to place the two cuts passes the gate, so no branch is pruned and four partitions are emitted. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^N)$. There are $2^{N-1}$ possible partitions. For each valid partition, copying a path of length up to $N$ into results takes $O(N)$ time. Precomputing the palindrome table takes $O(N^2)$ time, which is dominated by $O(N \cdot 2^N)$.
- **Auxiliary Space Complexity:** $O(N^2)$ to store the 2D palindrome table and $O(N)$ recursion stack depth and path buffer.

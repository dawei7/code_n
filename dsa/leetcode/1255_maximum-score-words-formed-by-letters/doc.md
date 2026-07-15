# Maximum Score Words Formed by Letters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1255 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Counting, Bitmask |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-score-words-formed-by-letters/) |

## Problem Description

### Goal

You are given candidate lowercase `words`, a multiset of available lowercase `letters`, and a 26-element `score` array. The value of a letter is `score[0]` for `"a"`, `score[1]` for `"b"`, and so on.

Choose any subset of the words. Every occurrence of a letter used by the chosen words must be supplied by a distinct occurrence in `letters`, so an available letter cannot be reused. A word may be selected at most once. Return the maximum total score of all letters in a feasible chosen subset; selecting no words is allowed and scores zero.

### Function Contract

**Inputs**

- `words`: $w$ lowercase words, where $1 \le w \le 14$ and each word has length from $1$ through $15$.
- `letters`: between $1$ and $100$ available lowercase letters, with multiplicity.
- `score`: 26 nonnegative letter scores, each at most `10`.
- Let $L=\sum_{x\in\texttt{words}}\lvert x\rvert$.

**Return value**

- Return the largest total letter score of any subset formable from `letters`.

### Examples

**Example 1**

- Input: `words = ["dog", "cat", "dad", "good"]`, `letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]`
- Output: `23`

**Example 2**

- Input: `words = ["xxxz", "ax", "bx", "cx"]`, `letters = ["z", "a", "b", "c", "x", "x", "x"]`
- Output: `27`

**Example 3**

- Input: `words = ["leetcode"]`, `letters = ["l", "e", "t", "c", "o", "d"]`
- Output: `0`
- Explanation: The missing second `"e"` prevents forming the only candidate word.

### Required Complexity

- **Time:** $O(2^w L)$
- **Space:** $O(w+L)$

<details>
<summary>Approach</summary>

#### General

The small limit of 14 words permits exploring the include-or-exclude choice for every word. Precompute each word's letter-frequency map and score so a recursive branch can test feasibility without rescanning the word's characters repeatedly.

**State and branching**

At word index `i`, first explore skipping the word. Then check whether the remaining letter multiset contains every required occurrence. If it does, subtract those counts, explore the branch that includes the word, add its precomputed score, and take the larger result. Copying the remaining counts keeps sibling branches independent.

**Why the search finds the optimum**

Every subset has a unique sequence of include and exclude decisions, so the recursion examines it exactly once. A branch is discarded only when its selected words require more of some letter than is available; adding more words can never repair that shortage. Thus every feasible subset remains represented, and maximizing over both choices at each level returns the best score.

The empty subset supplies a score of zero, which is important when no candidate word is feasible or all relevant letter scores are zero.

#### Complexity detail

There are at most $2^w$ decision paths. Across feasibility checks and count updates, a conservative bound is $O(2^wL)$ time. Precomputed word counts contain $O(L)$ entries in total, and recursion plus branch-local count storage uses $O(w+L)$ live space under the small fixed alphabet.

#### Alternatives and edge cases

- **Bitmask enumeration:** Evaluate every subset mask and aggregate its letter needs; it has the same exponential subset count but naively rebuilding counts adds repeated work.
- **Memoization by remaining counts:** It can merge repeated states, but the state key is larger and the 14-word limit already makes direct backtracking practical.
- **Greedy score ordering:** Choosing the highest-scoring word first can consume letters needed by a better combination and is not correct.
- **Duplicate candidate words:** Each list position is a separate selectable word, while letter multiplicities still limit how many copies can be formed.
- **Unformable word:** Its inclusion branch is skipped without affecting other candidates.
- **Zero scores:** Such letters still consume availability even though they add nothing to the objective.

</details>

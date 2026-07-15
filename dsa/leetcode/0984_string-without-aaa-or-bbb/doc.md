# String Without AAA or BBB

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 984 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/string-without-aaa-or-bbb/) |

## Problem Description

### Goal

Given two integers `a` and `b`, construct any string `s` containing exactly `a` copies of the letter `"a"` and exactly `b` copies of the letter `"b"`.

The resulting string must have length `a + b`. It must not contain `"aaa"` as a substring, and it must not contain `"bbb"` as a substring. Several different arrangements may satisfy these conditions; returning any one of them is valid. The input is guaranteed to admit at least one valid arrangement.

### Function Contract

**Inputs**

- `a`: the required number of `"a"` characters, where $0\le A=\texttt{a}\le100$.
- `b`: the required number of `"b"` characters, where $0\le B=\texttt{b}\le100$.

Let $L=A+B$ be the required output length.

**Return value**

- Any length-$L$ string with exactly $A$ letters `"a"`, exactly $B$ letters `"b"`, and no run of three equal letters.

### Examples

**Example 1**

- Input: `a = 1, b = 2`
- Output: `"abb"`
- Explanation: `"bab"` and `"bba"` are also valid.

**Example 2**

- Input: `a = 4, b = 1`
- Output: `"aabaa"`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Prefer the more plentiful letter:** When the current suffix does not force a choice, append whichever letter has the larger remaining count. Spending from the larger supply prevents it from becoming impossible to separate later.

**Break a run before it reaches three:** If the last two output characters are equal, the next character must be the other letter. Append that other letter regardless of which remaining count is larger. Otherwise choose the current majority, breaking a tie consistently. Decrement the chosen count and continue until both supplies are empty.

At every step the explicit suffix rule prevents a third equal character, so the constructed prefix remains valid. When no suffix rule applies, choosing the majority reduces the largest imbalance; choosing the minority instead could only make the harder-to-place supply even more dominant. When two equal characters force the minority, the existence guarantee ensures that required separator is available. Thus the process consumes all $A+B$ characters without getting stuck and preserves both exact counts.

#### Complexity detail

The loop appends exactly $L$ characters and does constant work for each, so time is $O(L)$. The returned character list and final string use $O(L)$ space; the counters use constant auxiliary space.

#### Alternatives and edge cases

- **Dynamic programming over remaining counts:** Feasibility states can construct a valid answer but require $O(AB)$ states for a problem with a direct greedy choice.
- **Exhaustive backtracking:** Trying both letters at every position can revisit exponentially many prefixes unless memoized.
- **One count is zero:** The existence guarantee means the other count is at most two, so the sole-letter string is valid.
- **Equal counts:** Alternating the letters naturally avoids forbidden runs; either starting letter works.
- **Multiple valid outputs:** Correctness depends on counts and forbidden substrings, not equality with one sample arrangement.

</details>

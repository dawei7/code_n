# Can Make Palindrome from Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1177 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/can-make-palindrome-from-substring/) |

## Problem Description

### Goal

You are given a lowercase English string `s` and queries of the form `[left, right, k]`. For each query independently, take the inclusive substring `s[left:right + 1]`. You may rearrange its characters in any order and then replace at most `k` individual characters with any lowercase English letters.

Decide whether those operations can turn the queried substring into a palindrome. Return the Boolean answers in query order. Each replacement affects one character occurrence, and no query changes the original string used by any other query.

### Function Contract

**Inputs**

- `s`: A lowercase English string with $1 \leq \lvert s\rvert \leq 10^5$.
- `queries`: Between $1$ and $10^5$ triples `[left, right, k]`, where $0 \leq \texttt{left} \leq \texttt{right} < \lvert s\rvert$ and $0 \leq \texttt{k} \leq \lvert s\rvert$.
- Let $n=\lvert s\rvert$ and $q=\lvert\texttt{queries}\rvert$.

**Return value**

- A length-$q$ Boolean array whose entry $i$ is `True` exactly when query $i$ can produce a palindrome using at most its replacement budget.

### Examples

**Example 1**

- Input: `s = "abcda"`, `queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]`
- Output: `[true,false,false,true,true]`

For `[0,3,2]`, the four distinct letters require two replacements; for `[0,4,1]`, changing one of the three unpaired character types is enough.

**Example 2**

- Input: `s = "lyb"`, `queries = [[0,1,0],[2,2,1]]`
- Output: `[false,true]`

**Example 3**

- Input: `s = "aaa"`, `queries = [[0,2,0],[0,2,2]]`
- Output: `[true,true]`

### Required Complexity

- **Time:** $O(n+q)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Keep only frequency parity.** Rearrangement makes character order irrelevant. A palindrome can pair every character occurrence except possibly one center occurrence, so only the characters with odd frequencies matter. If a substring has $x$ odd-frequency character types, one replacement can turn two odd frequencies even by changing an occurrence of one type into another. The minimum replacements is therefore $\lfloor x/2\rfloor$.

**Encode a prefix in 26 bits.** Assign one bit to each lowercase letter. Begin with prefix mask `0`; for every character, XOR its bit into the previous mask. A bit is set exactly when that character has appeared an odd number of times in the prefix.

**Cancel the part before each query.** For `[left, right, k]`, compute `masks[right + 1] ^ masks[left]`. Equal prefix parities cancel under XOR, leaving precisely the odd-frequency bits in the inclusive substring. `bit_count()` yields $x$, and the answer is whether `x // 2 <= k`. The string remains unchanged, so the same prefix masks answer every query.

#### Complexity detail

Building $n+1$ prefix masks takes $O(n)$ time. Each query uses a constant number of integer bit operations over the fixed 26-letter alphabet, so all queries take $O(q)$ time. The total is $O(n+q)$ time and the prefix array uses $O(n)$ auxiliary space; the returned answers are output storage.

#### Alternatives and edge cases

- **Count each queried substring directly:** This is correct but costs time proportional to every substring length and can take $O(nq)$ overall.
- **Twenty-six prefix-count arrays:** Subtracting counts per letter also gives $O(n+q)$ time because the alphabet is fixed, but uses more storage and operations than parity masks.
- **Odd-length substring:** One odd-frequency character may occupy the center without any replacement.
- **Even-length substring:** Every frequency must ultimately be even, which is still captured by `x // 2` because $x$ is even for an even total length.
- **Single character:** It is already a palindrome, even with `k = 0`.
- **Large budget:** A budget at least half the substring length always suffices.
- **Independent queries:** A replacement considered for one answer never modifies `s` for a later query.

</details>

# Construct String with Minimum Cost (Easy)

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3253 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Uncategorized |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-string-with-minimum-cost-easy/) |

## Problem Description

### Goal

Start with an empty string \`s\`. The arrays \`words\` and \`costs\` have equal length, and choosing index \`i\` appends \`words[i]\` to the end of \`s\` while charging \`costs[i]\`. Any index may be chosen repeatedly, and operations may be performed any number of times.

Find the minimum total cost of a sequence of appends that makes \`s\` exactly equal to \`target\`. Every append must therefore match the next unbuilt portion of the target; extra or different characters cannot be removed. Return \`-1\` when no sequence of available words constructs the complete target.

### Function Contract

**Inputs**

- \`target\`: A lowercase English string of length $n$, where $1 \le n \le 2000$.
- \`words\`: Between 1 and 50 lowercase English strings; every word has length from 1 through $n$.
- \`costs\`: A parallel list in which \`costs[i]\`, between 1 and $10^5$, is the cost of appending \`words[i]\`.

Let

$$
S=\sum_{w \in \operatorname{distinct}(\texttt{words})}\lvert w\rvert.
$$

**Return value**

- The minimum cost to concatenate available words into \`target\`, or \`-1\` if construction is impossible.

### Examples

**Example 1**

- Input: \`target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]\`
- Output: \`7\`

Appending \`"abc"\`, \`"d"\`, and \`"ef"\` costs $1+1+5=7$.

**Example 2**

- Input: \`target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]\`
- Output: \`-1\`

No available word matches even the first target character.

**Example 3**

- Input: \`target = "abc", words = ["ab","a","bc","c"], costs = [10,1,1,1]\`
- Output: \`2\`

Appending \`"a"\` and then \`"bc"\` is cheaper than using \`"ab"\` and \`"c"\`.

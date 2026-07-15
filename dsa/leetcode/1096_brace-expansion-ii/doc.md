# Brace Expansion II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1096 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Stack, Breadth-First Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/brace-expansion-ii/) |

## Problem Description

### Goal

Under the specified grammar, an expression represents a set of lowercase words, denoted by $R(e)$. A lowercase letter `x` represents the singleton set containing `x`. A comma-delimited group of at least two expressions represents the union of their sets, so duplicate words appear only once.

Adjacent expressions represent concatenation: combine every word from the left set with every word from the right set. Braces may nest, allowing union and concatenation to occur at multiple levels. Given a valid expression containing lowercase letters, braces, and commas, return all distinct words in $R(e)$ in lexicographic order.

### Function Contract

**Inputs**

- `expression`: a valid grammar expression of length $E$, where $1 \leq E \leq 60$ and every character is a lowercase English letter, `{`, `}`, or `,`.

Let $R$ be the number of distinct generated words, let $L$ be their maximum length, and define the total output text size as

$$
S = \sum_{w \in R(e)} \lvert w \rvert.
$$

**Return value**

The lexicographically sorted list of all distinct words represented by `expression`.

### Examples

**Example 1**

- Input: `expression = "{a,b}{c,{d,e}}"`
- Output: `["ac", "ad", "ae", "bc", "bd", "be"]`

**Example 2**

- Input: `expression = "{{a,z},a{b,c},{ab,z}}"`
- Output: `["a", "ab", "ac", "z"]`

The alternatives generate `ab` and `z` more than once, but the result is a set.

### Required Complexity

- **Time:** $O(E + S + RL \log R)$
- **Space:** $O(E + S)$

<details>
<summary>Approach</summary>

#### General

**Match the grammar with two parser levels.** Parse a union as one or more concatenation expressions separated by commas. Parse a concatenation as one or more adjacent factors. A factor is either a lowercase letter or a brace containing another union. Stopping a nested parser at `}` lets the recursive structure mirror the braces exactly.

**Use sets at every intermediate node.** Union applies set union. Concatenation forms `{prefix + suffix}` for every prefix in the accumulated left set and suffix in the next factor's set. Deduplicating immediately is important: the same word may arise through different alternatives, and carrying those copies into later Cartesian products can multiply useless work.

**Respect precedence through parser boundaries.** Concatenation binds within each comma-separated branch, while the union parser combines only completed branches. For `{a,b}{c,{d,e}}`, the first factor yields `a` or `b`, the second yields `c`, `d`, or `e`, and their Cartesian product gives the six results. Sorting the final set supplies the required order.

Each factor parser consumes exactly one valid grammatical unit. The concatenation parser therefore computes the Cartesian product prescribed for adjacent expressions, and the union parser combines exactly the branches prescribed by commas. Structural induction over nested braces shows that every parser result equals $R(e)$ for its consumed expression; set storage removes duplicates without removing any represented word.

#### Complexity detail

Parsing consumes the $E$ input characters. Hashing and materializing distinct intermediate and final strings is output-sensitive; for the final result this contributes $O(S)$. Sorting $R$ strings costs at most $O(RL \log R)$ character work. Thus the stated bound is $O(E + S + RL \log R)$, with $O(E)$ recursion and parser state plus $O(S)$ stored distinct text.

#### Alternatives and edge cases

- **Operator stacks:** Insert an explicit concatenation operator and evaluate union and Cartesian product by precedence. This avoids recursion but requires careful handling of implicit operators and braces.
- **Repeated textual expansion:** Expanding innermost braces into a list can be correct, but postponing deduplication may retain exponentially many duplicate candidates.
- **Single literal:** It forms a one-word set without braces or commas.
- **Nested duplicate unions:** Different branches can generate the same word; sets must remove it before the sorted result is built.
- **Adjacent brace groups:** They are concatenated even though no operator character appears between them.
- **Comma scope:** A comma ends the current concatenation branch only at its own brace depth.

</details>

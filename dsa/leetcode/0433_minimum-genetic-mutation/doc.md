# Minimum Genetic Mutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 433 |
| Difficulty | Medium |
| Topics | Hash Table, String, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-genetic-mutation/) |

## Problem Description
### Goal
Genes are eight-character strings over `A`, `C`, `G`, and `T`. One mutation changes exactly one character. Starting from `startGene`, reach `endGene` through a sequence in which every newly produced gene is present in the allowed bank.

Return the minimum number of mutations needed, or `-1` when no valid sequence reaches the target. The starting gene need not be in the bank, while the target and all intermediates after it must be allowed unless the start already equals the target. Each step preserves the other seven positions, and revisiting genes cannot improve a shortest sequence.

### Function Contract
**Inputs**

- `startGene`: the starting gene over `A`, `C`, `G`, and `T`
- `endGene`: the target gene of the same length
- `bank`: the list of allowed mutated genes

**Return value**

- Return the minimum number of mutations, or `-1` when the target cannot be reached through bank genes.

### Examples
**Example 1**

- Input: `startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]`
- Output: `1`

**Example 2**

- Input: `startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]`
- Output: `2`

**Example 3**

- Input: `startGene = "AAAAACCC", endGene = "AACCCCCC", bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]`
- Output: `3`
